'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const i18n = require('./i18n');

const UPSTREAM_COMMIT = 'a62d0e53f77bc53d0b1941e6baf89403ed25a129';

const SCRIPT_ORDER = [
  'EventTarget.js',
  'Room.js',
  'Item.js',
  'GameObjects.js',
  'Level.js',
  'GameState.js',
  'Game.js'
];

const IMAGE_PREFIX = './static/img/';

class TerminusEngine {
  constructor(options) {
    const opts = options || {};
    this.root = opts.root || path.resolve(__dirname, '..');
    this.scriptDir = path.join(this.root, 'vendor', 'terminus', 'js');
    this.imageDir = path.join(this.root, 'vendor', 'terminus', 'img');
    this.cookie = opts.cookie || '';
    this.lang = i18n.normalizeLanguage(opts.lang) || 'en';
    this.loaded = false;
    this.lastImage = null;
    this.imageSrc = null;
    this.wantExit = false;
    this.sandbox = this._createSandbox();
    this._load();
    this._ensureValidRoom();
    if (this.lang === 'es') {
      i18n.es.installHooks(this.sandbox);
      i18n.es.localizeGame(this.sandbox);
    }
  }

  _createSandbox() {
    const engine = this;
    const sandbox = {};

    sandbox.window = sandbox;
    sandbox.self = sandbox;
    sandbox.console = console;
    sandbox.document = { cookie: this.cookie };

    const scene = {
      attributes: {},
      attr(name, value) {
        if (value === undefined) {
          return this.attributes[name];
        }
        this.attributes[name] = value;
        if (name === 'src') {
          engine._setImage(value);
        }
        return this;
      },
      ready() {
        return this;
      },
      keyup() {
        return this;
      },
      click() {
        return this;
      },
      terminal() {
        return {
          history() {
            return { clear() {} };
          },
          get_command() {
            return '';
          },
          set_command() {},
          echo() {}
        };
      }
    };

    function jquery() {
      return scene;
    }

    jquery.grep = function (array, predicate) {
      return Array.prototype.filter.call(array, predicate);
    };
    jquery.extend = function (target) {
      for (let i = 1; i < arguments.length; i++) {
        const source = arguments[i];
        for (const key of Object.keys(source)) {
          target[key] = source[key];
        }
      }
      return target;
    };

    sandbox.$ = jquery;
    sandbox.jQuery = jquery;
    sandbox.open = function () {};
    sandbox.close = function () {
      engine.wantExit = true;
    };

    vm.createContext(sandbox, { name: 'terminus-game' });
    return sandbox;
  }

  _load() {
    // Game.js creates the player state and moves into the saved room on
    // evaluation, so the save must be validated before it runs.
    for (const file of SCRIPT_ORDER.slice(0, -1)) {
      this._runScript(file);
    }
    this._sanitizeCookie();
    this._runScript(SCRIPT_ORDER[SCRIPT_ORDER.length - 1]);
    this.loaded = true;
  }

  _runScript(file) {
    const filePath = path.join(this.scriptDir, file);
    const source = fs.readFileSync(filePath, 'utf8');
    vm.runInContext(source, this.sandbox, { filename: filePath });
  }

  _sanitizeCookie() {
    const cookie = this.sandbox.document.cookie || '';
    const match = cookie.match(/(?:^|;\s*)terminuscookie=([^;]*)/);
    if (!match) {
      return;
    }
    const roomName = match[1].split('=')[0];
    const Room = this.sandbox.Room;
    const candidate = this.sandbox[roomName];
    if (typeof Room === 'function' && candidate instanceof Room) {
      return;
    }
    this.sandbox.document.cookie = cookie
      .replace(/(?:^|;\s*)terminuscookie=[^;]*/, '')
      .replace(/^;\s*/, '');
  }

  _ensureValidRoom() {
    const room = this.sandbox.current_room;
    const Room = this.sandbox.Room;
    if (typeof Room === 'function' && room instanceof Room) {
      return;
    }
    // Corrupt or unknown save: fall back to the starting room.
    vm.runInContext('enterRoom(Home);', this.sandbox, {
      filename: 'terminus-game-reset-room'
    });
    this.lastImage = null;
  }

  _setImage(src) {
    this.imageSrc = src;
    if (typeof src !== 'string') {
      this.lastImage = null;
      return;
    }
    const base = src.split('/').pop();
    if (!base || base === 'none.gif') {
      this.lastImage = null;
      return;
    }
    this.lastImage = base;
  }

  imagePath(fileName) {
    if (!fileName) {
      return null;
    }
    return path.join(this.imageDir, path.basename(fileName));
  }

  room() {
    return this.sandbox.current_room;
  }

  roomName() {
    const room = this.room();
    return room ? room.room_name : 'Unknown';
  }

  stateString() {
    const state = this.sandbox.state;
    if (!state || !state.currentRoom) {
      return '';
    }
    // Same format as GameState.getState(), but drop the empty parameter the
    // upstream cookie parser adds when a room has no puzzle flags.
    const parts = [];
    for (const key of Object.keys(state.params)) {
      if (key) {
        parts.push(key + ':' + state.params[key] + '=');
      }
    }
    return state.currentRoom.toString() + '=' + parts.join('');
  }

  cookieString() {
    return this.sandbox.document.cookie || '';
  }

  manPages() {
    return this.sandbox.man_pages || {};
  }

  command(input) {
    const sandbox = this.sandbox;
    const output = [];
    const echo = (text) => {
      output.push(String(text));
    };

    this.lastImage = null;
    this.imageSrc = null;
    this.wantExit = false;

    const split = String(input).split(' ');
    const command = split[0].toString();
    const args = split.splice(1, split.length);
    let exec = true;

    if (sandbox.current_room.commands.indexOf(command) > -1) {
      let prevRoom = sandbox.current_room;

      if (args.length > 0 && args[0].indexOf('/') > 0) {
        const roomsInOrder = args[0].split('/');
        let currentRoom = sandbox.current_room;

        for (let i = 0; i < roomsInOrder.length; i++) {
          prevRoom = currentRoom;
          const roomToCd = roomsInOrder[i];

          if (i > 0 && roomsInOrder[i - 1] === '~') {
            currentRoom = sandbox.Home.can_cd(roomToCd);
          } else if (roomToCd === '~') {
            currentRoom = sandbox.Home;
          } else {
            currentRoom = currentRoom.can_cd(roomToCd);
          }

          if (!currentRoom) {
            echo('That is not reachable from here.');
            exec = false;
            break;
          }
        }

        if (exec) {
          args[0] = currentRoom.room_name;
        }
      }

      if (exec) {
        const text = prevRoom[command](args);
        if (text) {
          echo(text);
        }
        if (command in sandbox.current_room.cmd_text) {
          echo(sandbox.current_room.cmd_text[command]);
        }
      }
    } else {
      echo("Command '" + command + "' not found in room '" +
        sandbox.current_room.room_name + "'");
    }

    let text = output.join('\n');
    if (this.lang === 'es') {
      i18n.es.localizeGame(this.sandbox);
      text = i18n.es.translate(text);
    }
    return {
      output: text,
      image: this.lastImage,
      room: this.roomName(),
      exit: this.wantExit
    };
  }
}

module.exports = {
  TerminusEngine,
  UPSTREAM_COMMIT,
  IMAGE_PREFIX
};

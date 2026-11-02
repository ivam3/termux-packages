'use strict';

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const { TerminusEngine, UPSTREAM_COMMIT } = require('./engine');
const image = require('./image');
const saveStore = require('./save');
const i18n = require('./i18n');

const VERSION = '1.0.0';

const GREETING = 'Welcome! If you are new to the game, here are some tips: \n\n' +
  'Look at your surroundings with the command "ls". \n' +
  'Move to a new location with the command "cd LOCATION" \n' +
  'You can backtrack with the command "cd ..". \n' +
  'Interact with things in the world with the command "less ITEM" \n\n' +
  'If you forget where you are, type "pwd" \n\n' +
  'Go ahead, explore. We hope you enjoy what you find. Do ls as your first command.\n';

const GREETING_ES = '¡Bienvenido! Si eres nuevo en el juego, aquí tienes algunos consejos: \n\n' +
  'Mira a tu alrededor con el comando "ls". \n' +
  'Muévete a una nueva ubicación con el comando "cd LUGAR". \n' +
  'Puedes retroceder con el comando "cd ..". \n' +
  'Interactúa con las cosas del mundo con el comando "less OBJETO". \n\n' +
  'Si olvidas dónde estás, escribe "pwd". \n\n' +
  'Adelante, explora. Esperamos que disfrutes lo que encuentres. ' +
  'Haz ls como tu primer comando.\n';

const HELP = `Usage: terminus-game [OPTIONS]

Terminal port of Terminus, the Linux learning adventure game by Michele Pratusevich.

Options:
  --reset             Start a new game (removes the current save)
  --no-save           Do not read or write a save file
  --save FILE         Use FILE as the save file
  --script FILE       Run commands from FILE and exit
  --images MODE       Image rendering: auto, chafa, open, off (default: auto)
  --esp               Show the game in Spanish (same as --lang es)
  --lang LANG         Game language: en or es (default: en)
  --version, -V       Show version information
  --help, -h          Show this help

Environment:
  TERMINUS_SAVE       Default save file path
                      (default: $XDG_DATA_HOME/terminus-game/save.json)
  TERMINUS_ROOT       Terminus data directory
  TERMINUS_LANG       Default game language: en or es
`;

const HELP_ES = `Uso: terminus-game [OPCIONES]

Port a terminal de Terminus, el juego de aventuras para aprender Linux de Michele Pratusevich.

Opciones:
  --reset             Empezar una partida nueva (borra la partida actual)
  --no-save           No leer ni escribir archivo de partida
  --save ARCHIVO      Usar ARCHIVO como archivo de partida
  --script ARCHIVO    Ejecutar los comandos de ARCHIVO y salir
  --images MODO       Renderizado de imágenes: auto, chafa, open, off (por defecto: auto)
  --esp               Mostrar el juego en español (igual que --lang es)
  --lang IDIOMA       Idioma del juego: en o es (por defecto: en)
  --version, -V       Mostrar información de versión
  --help, -h          Mostrar esta ayuda

Entorno:
  TERMINUS_SAVE       Ruta del archivo de partida por defecto
                      (por defecto: $XDG_DATA_HOME/terminus-game/save.json)
  TERMINUS_ROOT       Directorio de datos de Terminus
  TERMINUS_LANG       Idioma del juego por defecto: en o es
`;

function parseImages(value) {
  const modes = ['auto', 'chafa', 'open', 'off'];
  if (modes.indexOf(value) === -1) {
    throw new Error("invalid --images value '" + value + "' (expected auto, chafa, open or off)");
  }
  return value;
}

function parseLanguage(value) {
  if (!value) {
    throw new Error("invalid language '" + value + "' (expected en or es)");
  }
  const language = i18n.normalizeLanguage(value);
  if (!language) {
    throw new Error("invalid language '" + value + "' (expected en or es)");
  }
  return language;
}

function parseArgs(argv, defaultLanguage) {
  const options = {
    reset: false,
    save: true,
    savePath: null,
    script: null,
    images: 'auto',
    imagesExplicit: false,
    lang: i18n.normalizeLanguage(defaultLanguage) || 'en',
    help: false,
    version: false
  };

  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--help' || arg === '-h') {
      options.help = true;
    } else if (arg === '--version' || arg === '-V') {
      options.version = true;
    } else if (arg === '--reset') {
      options.reset = true;
    } else if (arg === '--no-save') {
      options.save = false;
    } else if (arg === '--save') {
      options.savePath = argv[++i];
      if (!options.savePath) {
        throw new Error('--save requires a file path');
      }
    } else if (arg.startsWith('--save=')) {
      options.savePath = arg.slice('--save='.length);
    } else if (arg === '--script') {
      options.script = argv[++i];
      if (!options.script) {
        throw new Error('--script requires a file path');
      }
    } else if (arg.startsWith('--script=')) {
      options.script = arg.slice('--script='.length);
    } else if (arg === '--images') {
      options.images = parseImages(argv[++i]);
      options.imagesExplicit = true;
    } else if (arg.startsWith('--images=')) {
      options.images = parseImages(arg.slice('--images='.length));
      options.imagesExplicit = true;
    } else if (arg === '--esp') {
      options.lang = 'es';
    } else if (arg === '--lang') {
      const value = argv[++i];
      if (!value) {
        throw new Error('--lang requires a language (en or es)');
      }
      options.lang = parseLanguage(value);
    } else if (arg.startsWith('--lang=')) {
      options.lang = parseLanguage(arg.slice('--lang='.length));
    } else if (arg === '--') {
      break;
    } else {
      throw new Error("unknown option '" + arg + "' (use --help)");
    }
  }

  return options;
}

class Runner {
  constructor(root, options) {
    this.root = root;
    this.options = options;
    this.savePath = options.savePath || saveStore.defaultSavePath();
    this.scriptMode = Boolean(options.script);
    this.lastImage = null;
    this.imageMode = image.resolveMode(
      options.images,
      Boolean(process.stdout.isTTY) && !this.scriptMode
    );
    this.engine = null;
  }

  start() {
    if (this.options.reset) {
      saveStore.clear(this.savePath);
    }

    let state = null;
    if (this.options.save) {
      const saved = saveStore.load(this.savePath);
      if (saved) {
        state = saved.state;
      }
    }

    const cookie = state ? 'terminuscookie=' + state : '';
    this.engine = new TerminusEngine({
      root: this.root,
      cookie,
      lang: this.options.lang
    });
  }

  persist() {
    if (!this.options.save || !this.engine) {
      return;
    }
    try {
      saveStore.write(this.savePath, this.engine.stateString());
    } catch (error) {
      process.stderr.write('terminus-game: could not write save file: ' +
        error.message + '\n');
    }
  }

  renderImage(result) {
    if (!result.image) {
      this.lastImage = null;
      return;
    }
    if (result.image === this.lastImage) {
      return;
    }
    this.lastImage = result.image;
    const rendered = image.render(
      path.join(this.root, 'vendor', 'terminus', 'img'),
      result.image,
      this.imageMode,
      { enabled: Boolean(process.stdout.isTTY) && !this.scriptMode }
    );
    if (rendered) {
      process.stdout.write(rendered + '\n');
    }
  }

  runCommand(line) {
    const result = this.engine.command(line);
    if (result.output) {
      process.stdout.write(result.output + '\n');
    }
    this.renderImage(result);
    this.persist();
    return result;
  }

  runScript(file) {
    let contents;
    try {
      contents = fs.readFileSync(file, 'utf8');
    } catch (error) {
      process.stderr.write("terminus-game: cannot read script '" + file + "': " +
        error.message + '\n');
      return 1;
    }

    const lines = contents.split(/\r?\n/);
    for (const raw of lines) {
      const line = raw.trim();
      if (!line || line.startsWith('#')) {
        continue;
      }
      process.stdout.write('> ' + line + '\n');
      const result = this.runCommand(line);
      if (result.exit) {
        break;
      }
    }
    this.persist();
    return 0;
  }

  runInteractive() {
    const greeting = this.options.lang === 'es' ? GREETING_ES : GREETING;
    process.stdout.write(greeting + '\n');

    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
      terminal: Boolean(process.stdin.isTTY)
    });

    rl.setPrompt('> ');

    const finish = () => {
      this.persist();
      try {
        rl.close();
      } catch (error) {
        // already closed
      }
    };

    rl.on('line', (line) => {
      const trimmed = line.trim();
      if (trimmed) {
        const result = this.runCommand(trimmed);
        if (result.exit) {
          finish();
          return;
        }
      }
      rl.prompt();
    });

    rl.on('SIGINT', () => {
      process.stdout.write('\n');
      finish();
    });

    rl.on('close', () => {
      this.persist();
    });

    rl.prompt();
  }
}

function main() {
  let options;
  try {
    options = parseArgs(process.argv.slice(2), process.env.TERMINUS_LANG);
  } catch (error) {
    process.stderr.write('terminus-game: ' + error.message + '\n');
    return 2;
  }

  if (options.help) {
    process.stdout.write(options.lang === 'es' ? HELP_ES : HELP);
    return 0;
  }

  if (options.version) {
    process.stdout.write('terminus-game ' + VERSION +
      ' (Terminus ' + UPSTREAM_COMMIT.slice(0, 7) + ')\n');
    return 0;
  }

  const root = process.env.TERMINUS_ROOT || path.resolve(__dirname, '..');
  const runner = new Runner(root, options);

  try {
    runner.start();
  } catch (error) {
    process.stderr.write('terminus-game: failed to start: ' + error.message + '\n');
    return 1;
  }

  if (runner.scriptMode) {
    return runner.runScript(options.script);
  }

  runner.runInteractive();
  return 0;
}

if (require.main === module) {
  process.exitCode = main();
}

module.exports = {
  main,
  parseArgs,
  Runner,
  GREETING,
  GREETING_ES,
  HELP,
  HELP_ES,
  VERSION
};

'use strict';

const fs = require('fs');
const os = require('os');
const path = require('path');

function dataHome() {
  return process.env.XDG_DATA_HOME ||
    path.join(process.env.HOME || os.homedir(), '.local', 'share');
}

function defaultSavePath() {
  return process.env.TERMINUS_SAVE ||
    path.join(dataHome(), 'terminus-game', 'save.json');
}

function load(savePath) {
  try {
    const raw = fs.readFileSync(savePath, 'utf8');
    const data = JSON.parse(raw);
    if (data && typeof data.state === 'string' && data.state.length > 0) {
      return data;
    }
  } catch (error) {
    return null;
  }
  return null;
}

function write(savePath, state) {
  const directory = path.dirname(savePath);
  fs.mkdirSync(directory, { recursive: true });
  const payload = {
    version: 1,
    state,
    updated: new Date().toISOString()
  };
  const temporary = savePath + '.tmp';
  fs.writeFileSync(temporary, JSON.stringify(payload, null, 2) + '\n', 'utf8');
  fs.renameSync(temporary, savePath);
}

function clear(savePath) {
  try {
    fs.unlinkSync(savePath);
    return true;
  } catch (error) {
    return false;
  }
}

module.exports = {
  defaultSavePath,
  load,
  write,
  clear,
  dataHome
};

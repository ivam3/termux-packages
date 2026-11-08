'use strict';

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

function commandExists(command) {
  const result = spawnSync('sh', ['-c', 'command -v ' + command], {
    stdio: ['ignore', 'pipe', 'ignore']
  });
  return result.status === 0;
}

function terminalSize() {
  const columns = process.stdout.columns || 80;
  const rows = process.stdout.rows || 24;
  return { columns, rows };
}

function chafaSize() {
  const { columns, rows } = terminalSize();
  const width = Math.max(20, Math.min(columns - 2, 64));
  const height = Math.max(8, Math.min(Math.floor(rows * 0.6), 32));
  return { width, height };
}

function renderWithChafa(file, options) {
  const opts = options || {};
  const size = opts.size || chafaSize();
  const result = spawnSync('chafa', [
      file
    // '--format=symbols',
    // '--animate=off',
    // '--size=' + size.width + 'x' + size.height,
    // '--margin-bottom=0',
    // '--margin-right=0',
    // file
  ], {
    encoding: 'utf8',
    maxBuffer: 16 * 1024 * 1024,
    stdio: ['ignore', 'pipe', 'ignore']
  });

  if (result.error || result.status !== 0 || !result.stdout) {
    return null;
  }
  return result.stdout.replace(/\s+$/, '');
}

function openWithTermux(file) {
  const result = spawnSync('termux-open', [file], {
    stdio: ['ignore', 'ignore', 'ignore']
  });
  return !result.error && result.status === 0;
}

function resolveMode(mode, enabled) {
  if (mode === 'off') {
    return 'off';
  }
  if (mode === 'chafa' || mode === 'open') {
    return mode;
  }
  if (mode === 'auto') {
    if (!enabled) {
      return 'off';
    }
    if (commandExists('chafa')) {
      return 'chafa';
    }
    return 'off';
  }
  return 'off';
}

function render(imageDir, fileName, mode, options) {
  const opts = options || {};
  if (!fileName || mode === 'off') {
    return null;
  }

  const file = path.join(imageDir, path.basename(fileName));
  if (!fs.existsSync(file)) {
    return null;
  }

  if (mode === 'open') {
    return openWithTermux(file) ? '' : null;
  }

  if (!commandExists('chafa')) {
    return null;
  }
  return renderWithChafa(file, opts);
}

module.exports = {
  render,
  resolveMode,
  commandExists,
  chafaSize,
  terminalSize
};

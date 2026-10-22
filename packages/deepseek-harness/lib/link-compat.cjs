'use strict';

const fs = require('node:fs');
const fsp = fs.promises;
const FALLBACK_CODES = new Set(['EACCES', 'EPERM', 'ENOTSUP', 'EOPNOTSUPP', 'EMLINK']);

if (!globalThis.__dshLinkCompatInstalled) {
  globalThis.__dshLinkCompatInstalled = true;

  const isFallback = (error) => Boolean(error && typeof error === 'object' && FALLBACK_CODES.has(error.code));

  const copyLinkFallback = async (existingPath, newPath) => {
    const st = await fsp.lstat(existingPath);
    if (st.isSymbolicLink()) {
      await fsp.symlink(await fsp.readlink(existingPath), newPath);
      return;
    }
    if (!st.isFile()) {
      const error = new Error(`link fallback supports only files and symlinks: ${existingPath}`);
      error.code = 'EPERM';
      throw error;
    }
    await fsp.copyFile(existingPath, newPath, fs.constants.COPYFILE_EXCL);
    const handle = await fsp.open(newPath, 'r+');
    try {
      await handle.sync();
    } finally {
      await handle.close();
    }
    await fsp.chmod(newPath, st.mode & 0o7777);
  };

  const originalPromisesLink = fsp.link.bind(fsp);
  fsp.link = async function linkCompat(existingPath, newPath) {
    try {
      return await originalPromisesLink(existingPath, newPath);
    } catch (error) {
      if (!isFallback(error)) throw error;
      return copyLinkFallback(existingPath, newPath);
    }
  };

  fs.link = function linkCompatCallback(existingPath, newPath, callback) {
    const done = typeof callback === 'function' ? callback : () => {};
    fsp.link(existingPath, newPath).then(
      () => process.nextTick(done, null),
      (error) => process.nextTick(done, error),
    );
  };

  const originalLinkSync = fs.linkSync.bind(fs);
  fs.linkSync = function linkCompatSync(existingPath, newPath) {
    try {
      return originalLinkSync(existingPath, newPath);
    } catch (error) {
      if (!isFallback(error)) throw error;
      const st = fs.lstatSync(existingPath);
      if (st.isSymbolicLink()) {
        fs.symlinkSync(fs.readlinkSync(existingPath), newPath);
        return;
      }
      if (!st.isFile()) {
        const unsupported = new Error(`link fallback supports only files and symlinks: ${existingPath}`);
        unsupported.code = 'EPERM';
        throw unsupported;
      }
      fs.copyFileSync(existingPath, newPath, fs.constants.COPYFILE_EXCL);
      const fd = fs.openSync(newPath, 'r+');
      try {
        fs.fsyncSync(fd);
      } finally {
        fs.closeSync(fd);
      }
      fs.chmodSync(newPath, st.mode & 0o7777);
    }
  };
}

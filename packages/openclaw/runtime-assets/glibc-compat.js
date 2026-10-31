/**
 * glibc-compat.js - Minimal compatibility shim for glibc Node.js on Android
 *
 * This is the successor to bionic-compat.js, drastically reduced for glibc.
 *
 * What's NOT needed anymore (glibc handles these):
 * - process.platform override (glibc Node.js reports 'linux' natively)
 * - renameat2 / spawn.h stubs (glibc includes them)
 * - CXXFLAGS / GYP_DEFINES overrides (glibc is standard Linux)
 *
 * What's still needed (kernel/Android-level restrictions, not libc):
 * - os.cpus() fallback: SELinux blocks /proc/stat on Android 8+
 * - os.networkInterfaces() safety: EACCES on some Android configurations
 * - /bin/sh path shim: Android 7-8 lacks /bin/sh (Android 9+ has it)
 *
 * Loaded via node wrapper script: node --require <path>/glibc-compat.js
 */

'use strict';

const os = require('os');
const fs = require('fs');
const path = require('path');

// ─── process.execPath fix ────────────────────────────────────
// When node runs via grun (ld.so node.real), process.execPath points to
// ld.so instead of the node wrapper. Apps that spawn child node processes
// using process.execPath (e.g., openclaw) will call ld.so directly,
// bypassing the wrapper's LD_PRELOAD unset and compat loading.
// Fix: point process.execPath to the wrapper script.

const _wrapperPath = process.env._OA_WRAPPER_PATH || path.join(
  process.env.HOME || '/data/data/com.termux/files/home',
  '.openclaw-android', 'bin', 'node'
);
try {
  if (fs.existsSync(_wrapperPath)) {
    Object.defineProperty(process, 'execPath', {
      value: _wrapperPath,
      writable: true,
      configurable: true,
    });
  }
} catch {}


// ─── LD_PRELOAD restore for child processes ─────────────────
// The node wrapper unsets LD_PRELOAD to prevent bionic libtermux-exec.so
// from loading into the glibc node.real process. However, bionic child
// processes (/bin/sh, etc.) need libtermux-exec for path translation
// (e.g., /usr/bin/env → $PREFIX/bin/env in shebang resolution).
// Restore LD_PRELOAD after node.real has loaded — this only affects
// child processes, not the already-running node.real.

if (process.env._OA_ORIG_LD_PRELOAD) {
  // New wrapper (v1.0.12+): saved original LD_PRELOAD before unsetting
  process.env.LD_PRELOAD = process.env._OA_ORIG_LD_PRELOAD;
  delete process.env._OA_ORIG_LD_PRELOAD;
} else if (!process.env.LD_PRELOAD) {
  // Old wrapper (pre-v1.0.12): unset LD_PRELOAD without saving — detect directly
  const _termuxExec = (process.env.PREFIX || '/data/data/com.termux/files/usr')
    + '/lib/libtermux-exec-ld-preload.so';
  try { if (fs.existsSync(_termuxExec)) process.env.LD_PRELOAD = _termuxExec; } catch {}
}


// ─── os.cpus() fallback ─────────────────────────────────────
// Android 8+ (API 26+) blocks /proc/stat via SELinux + hidepid=2.
// libuv reads /proc/stat for CPU info → returns empty array.
// Tools using os.cpus().length for parallelism (e.g., make -j) break with 0.

const _originalCpus = os.cpus;

os.cpus = function cpus() {
  const result = _originalCpus.call(os);
  if (result.length > 0) {
    return result;
  }
  // Return a single fake CPU entry so .length is at least 1
  return [{ model: 'unknown', speed: 0, times: { user: 0, nice: 0, sys: 0, idle: 0, irq: 0 } }];
};

// ─── os.networkInterfaces() safety ──────────────────────────
// Some Android configurations throw EACCES when reading network
// interface information. Wrap with try-catch to prevent crashes.
//
// Additionally, Android/Termux typically only exposes the loopback
// interface (`lo`) to Node.js. In that situation, OpenClaw's Bonjour
// advertiser can't send multicast announcements and logs noisy
// "Announcement failed as of socket errors!" repeatedly.
// Auto-disable Bonjour via OPENCLAW_DISABLE_BONJOUR when only
// loopback interfaces are visible.

const _originalNetworkInterfaces = os.networkInterfaces;

function _createLoopbackInterfaces() {
  return {
    lo: [
      {
        address: '127.0.0.1',
        netmask: '255.0.0.0',
        family: 'IPv4',
        mac: '00:00:00:00:00:00',
        internal: true,
        cidr: '127.0.0.1/8',
      },
    ],
  };
}

function _hasNonLoopbackInterface(interfaces) {
  try {
    return Object.values(interfaces).some(entries =>
      Array.isArray(entries) && entries.some(entry => entry && entry.internal === false)
    );
  } catch {
    return false;
  }
}

os.networkInterfaces = function networkInterfaces() {
  let interfaces;
  try {
    interfaces = _originalNetworkInterfaces.call(os);
  } catch {
    interfaces = _createLoopbackInterfaces();
  }
  if (!process.env.OPENCLAW_DISABLE_BONJOUR && !_hasNonLoopbackInterface(interfaces)) {
    process.env.OPENCLAW_DISABLE_BONJOUR = '1';
  }
  return interfaces;
};

// ─── /bin/sh path shim (Android 7-8 only) ───────────────────
// Android 9+ (API 28+) has /bin → /system/bin symlink, so /bin/sh exists.
// Android 7-8 lacks /bin/sh entirely.
// Node.js child_process hardcodes /bin/sh as the default shell on Linux.
// With glibc (platform='linux'), LD_PRELOAD is unset, so libtermux-exec.so
// path translation is not available.
//
// This shim only activates if /bin/sh doesn't exist.

if (!fs.existsSync('/bin/sh')) {
  const child_process = require('child_process');
  const termuxSh = (process.env.PREFIX || '/data/data/com.termux/files/usr') + '/bin/sh';

  if (fs.existsSync(termuxSh)) {
    // Override exec/execSync to use Termux shell
    const _originalExec = child_process.exec;
    const _originalExecSync = child_process.execSync;

    child_process.exec = function exec(command, options, callback) {
      if (typeof options === 'function') {
        callback = options;
        options = {};
      }
      options = options || {};
      if (!options.shell) {
        options.shell = termuxSh;
      }
      return _originalExec.call(child_process, command, options, callback);
    };

    child_process.execSync = function execSync(command, options) {
      options = options || {};
      if (!options.shell) {
        options.shell = termuxSh;
      }
      return _originalExecSync.call(child_process, command, options);
    };
  }
}

// ─── DNS resolver fix ────────────────────────────────────────
// glibc's getaddrinfo() reads /data/data/com.termux/files/usr/glibc/etc/resolv.conf
// for DNS servers. This file may be missing or inaccessible:
// - Standalone APK: runs under com.openclaw.android, can't access com.termux paths
// - Termux: resolv-conf package may not be installed
// Without a valid resolv.conf, dns.lookup() fails with EAI_AGAIN errors.
//
// Fix: Override both dns.lookup (callback) and dns.promises.lookup (promise)
// to use c-ares resolver (dns.resolve) which respects dns.setServers(),
// then fall back to getaddrinfo.

try {
  const dns = require('dns');

  // Read DNS servers from our resolv.conf or use Google DNS as fallback
  let dnsServers = ['8.8.8.8', '8.8.4.4'];
  try {
    const resolvConf = fs.readFileSync(
      (process.env.PREFIX || '/data/data/com.termux/files/usr') + '/etc/resolv.conf',
      'utf8'
    );
    const parsed = resolvConf.match(/^nameserver\s+(.+)$/gm);
    if (parsed && parsed.length > 0) {
      dnsServers = parsed.map(l => l.replace(/^nameserver\s+/, '').trim());
    }
  } catch {}

  // Set DNS servers for c-ares resolver
  try { dns.setServers(dnsServers); } catch {}

  // Override dns.lookup (callback API) to use c-ares resolver
  const _originalLookup = dns.lookup;
  dns.lookup = function lookup(hostname, options, callback) {
    if (typeof options === 'function') {
      callback = options;
      options = {};
    }
    const originalOptions = options;
    const opts = typeof options === 'number' ? { family: options } : (options || {});
    const wantAll = opts.all === true;
    const family = opts.family || 0;

    const resolve = (fam, cb) => {
      const fn = fam === 6 ? dns.resolve6 : dns.resolve4;
      fn(hostname, cb);
    };

    const tryResolve = (fam) => {
      resolve(fam, (err, addresses) => {
        if (!err && addresses && addresses.length > 0) {
          const resFam = fam === 6 ? 6 : 4;
          if (wantAll) {
            callback(null, addresses.map(a => ({ address: a, family: resFam })));
          } else {
            callback(null, addresses[0], resFam);
          }
        } else if (family === 0 && fam === 4) {
          tryResolve(6);
        } else {
          _originalLookup.call(dns, hostname, originalOptions, callback);
        }
      });
    };

    tryResolve(family === 6 ? 6 : 4);
  };

  // Override dns.promises.lookup (promise API) to use c-ares resolver.
  // OpenClaw's SSRF guard uses this API for web_search DNS resolution.
  const _originalPromiseLookup = dns.promises.lookup;
  dns.promises.lookup = async function lookup(hostname, options) {
    const opts = typeof options === 'number' ? { family: options } : (options || {});
    const wantAll = opts.all === true;
    const family = opts.family || 0;

    const resolve = (fam) => {
      return new Promise((res, rej) => {
        const fn = fam === 6 ? dns.resolve6 : dns.resolve4;
        fn(hostname, (err, addresses) => err ? rej(err) : res(addresses));
      });
    };

    const tryResolve = async (fam) => {
      try {
        const addresses = await resolve(fam);
        if (addresses && addresses.length > 0) {
          const resFam = fam === 6 ? 6 : 4;
          if (wantAll) {
            return addresses.map(a => ({ address: a, family: resFam }));
          }
          return { address: addresses[0], family: resFam };
        }
      } catch {}
      if (family === 0 && fam === 4) return tryResolve(6);
      return _originalPromiseLookup.call(dns.promises, hostname, options);
    };

    return tryResolve(family === 6 ? 6 : 4);
  };
} catch {}

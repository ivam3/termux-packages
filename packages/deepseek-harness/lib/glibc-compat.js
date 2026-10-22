'use strict';

const fs = require('fs');
const os = require('os');

const fallbackWrapper = '/data/data/com.termux/files/usr/bin/dsh-node';
const wrapperPath = process.env._DSH_WRAPPER_PATH || fallbackWrapper;

// When Node runs through ld.so, /proc/self/exe points at the loader. Point it
// back at dsh-node so child Node processes use the glibc wrapper again.
try {
  if (fs.existsSync(wrapperPath)) {
    Object.defineProperty(process, 'execPath', {
      value: wrapperPath,
      writable: true,
      configurable: true,
    });
  }
} catch {}

// Bionic children such as bash need the original LD_PRELOAD for Termux path
// translation. The glibc Node process itself must not inherit it.
if (process.env._DSH_ORIG_LD_PRELOAD) {
  process.env.LD_PRELOAD = process.env._DSH_ORIG_LD_PRELOAD;
  delete process.env._DSH_ORIG_LD_PRELOAD;
}

if (process.env._DSH_ORIG_LD_LIBRARY_PATH) {
  process.env.LD_LIBRARY_PATH = process.env._DSH_ORIG_LD_LIBRARY_PATH;
  delete process.env._DSH_ORIG_LD_LIBRARY_PATH;
}

// Android's SELinux policy can hide /proc/stat from libuv.
const originalCpus = os.cpus;
os.cpus = function cpus() {
  const result = originalCpus.call(os);
  if (result.length > 0) {
    return result;
  }
  return [{
    model: 'unknown',
    speed: 0,
    times: { user: 0, nice: 0, sys: 0, idle: 0, irq: 0 },
  }];
};

// Some Android configurations deny network-interface enumeration.
const originalNetworkInterfaces = os.networkInterfaces;
os.networkInterfaces = function networkInterfaces() {
  try {
    return originalNetworkInterfaces.call(os);
  } catch {
    return {
      lo: [{
        address: '127.0.0.1',
        netmask: '255.0.0.0',
        family: 'IPv4',
        mac: '00:00:00:00:00:00',
        internal: true,
        cidr: '127.0.0.1/8',
      }],
    };
  }
};

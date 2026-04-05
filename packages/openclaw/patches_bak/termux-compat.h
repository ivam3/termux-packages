/*
 * termux-compat.h - Compatibility shim for missing libc declarations in Termux
 *
 * Android Bionic lacks some glibc/POSIX functions that native modules expect.
 * This header provides syscall-based wrappers or stubs for them.
 *
 * Usage: CXXFLAGS="-include /path/to/termux-compat.h"
 *        This force-includes the header before every source file.
 */

#ifndef _TERMUX_COMPAT_H_
#define _TERMUX_COMPAT_H_

#include <sys/syscall.h>
#include <unistd.h>
#include <linux/fs.h>

/* renameat2() - available in kernel 3.15+ but Bionic only exposes it in API 30+ */
#ifndef __RENAME_NOREPLACE_DEFINED
static inline int renameat2(int olddirfd, const char *oldpath,
                            int newdirfd, const char *newpath,
                            unsigned int flags) {
    return syscall(__NR_renameat2, olddirfd, oldpath, newdirfd, newpath, flags);
}
#endif

#endif /* _TERMUX_COMPAT_H_ */

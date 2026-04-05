/*
 * spawn.h - POSIX spawn stub header for Termux
 *
 * Android Bionic supports posix_spawn() since API 28 (Android 9.0),
 * but Termux's NDK headers may not include spawn.h.
 * This stub provides the necessary declarations so native modules
 * (e.g. koffi) can compile and link against the system libc.
 *
 * Based on Android Open Source Project (Apache-2.0 / BSD)
 */

#ifndef _SPAWN_H_
#define _SPAWN_H_

#include <sys/cdefs.h>
#include <sys/types.h>
#include <sched.h>
#include <signal.h>

__BEGIN_DECLS

#define POSIX_SPAWN_RESETIDS        1
#define POSIX_SPAWN_SETPGROUP       2
#define POSIX_SPAWN_SETSIGDEF       4
#define POSIX_SPAWN_SETSIGMASK      8
#define POSIX_SPAWN_SETSCHEDPARAM   16
#define POSIX_SPAWN_SETSCHEDULER    32
#define POSIX_SPAWN_SETSID          128
#define POSIX_SPAWN_CLOEXEC_DEFAULT 256

typedef struct __posix_spawnattr* posix_spawnattr_t;
typedef struct __posix_spawn_file_actions* posix_spawn_file_actions_t;

int posix_spawn(pid_t* __pid, const char* __path, const posix_spawn_file_actions_t* __actions, const posix_spawnattr_t* __attr, char* const* __argv, char* const* __env);
int posix_spawnp(pid_t* __pid, const char* __file, const posix_spawn_file_actions_t* __actions, const posix_spawnattr_t* __attr, char* const* __argv, char* const* __env);

int posix_spawnattr_init(posix_spawnattr_t* __attr);
int posix_spawnattr_destroy(posix_spawnattr_t* __attr);
int posix_spawnattr_setflags(posix_spawnattr_t* __attr, short __flags);
int posix_spawnattr_getflags(const posix_spawnattr_t* __attr, short* __flags);
int posix_spawnattr_setpgroup(posix_spawnattr_t* __attr, pid_t __pgroup);
int posix_spawnattr_getpgroup(const posix_spawnattr_t* __attr, pid_t* __pgroup);
int posix_spawnattr_setsigmask(posix_spawnattr_t* __attr, const sigset_t* __mask);
int posix_spawnattr_getsigmask(const posix_spawnattr_t* __attr, sigset_t* __mask);
int posix_spawnattr_setsigdefault(posix_spawnattr_t* __attr, const sigset_t* __mask);
int posix_spawnattr_getsigdefault(const posix_spawnattr_t* __attr, sigset_t* __mask);
int posix_spawnattr_setschedparam(posix_spawnattr_t* __attr, const struct sched_param* __param);
int posix_spawnattr_getschedparam(const posix_spawnattr_t* __attr, struct sched_param* __param);
int posix_spawnattr_setschedpolicy(posix_spawnattr_t* __attr, int __policy);
int posix_spawnattr_getschedpolicy(const posix_spawnattr_t* __attr, int* __policy);

int posix_spawn_file_actions_init(posix_spawn_file_actions_t* __actions);
int posix_spawn_file_actions_destroy(posix_spawn_file_actions_t* __actions);
int posix_spawn_file_actions_addopen(posix_spawn_file_actions_t* __actions, int __fd, const char* __path, int __flags, mode_t __mode);
int posix_spawn_file_actions_addclose(posix_spawn_file_actions_t* __actions, int __fd);
int posix_spawn_file_actions_adddup2(posix_spawn_file_actions_t* __actions, int __fd, int __new_fd);

__END_DECLS

#endif

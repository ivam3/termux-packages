#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <sys/stat.h>

#define TERMUX_HOME "/data/data/com.termux/files/home"

static void set_path(const char *name, const char *home, const char *suffix) {
    char path[PATH_MAX];
    snprintf(path, sizeof(path), "%s/%s", home, suffix);
    mkdir(path, 0700);
    setenv(name, path, 1);
}

int main(int argc, char **argv) {
    unsetenv("LD_PRELOAD");
    unsetenv("LD_LIBRARY_PATH");

    const char *home = getenv("HOME");
    if (home == NULL || *home == '\0') {
        home = TERMUX_HOME;
    }

    char base[PATH_MAX];
    snprintf(base, sizeof(base), "%s/.opencode-v2", home);
    mkdir(base, 0700);

    set_path("XDG_CONFIG_HOME", home, ".opencode-v2/config");
    set_path("XDG_DATA_HOME", home, ".opencode-v2/data");
    set_path("XDG_CACHE_HOME", home, ".opencode-v2/cache");
    set_path("XDG_STATE_HOME", home, ".opencode-v2/state");
    set_path("TMPDIR", home, ".opencode-v2/tmp");

    setenv("SSL_CERT_FILE", "/data/data/com.termux/files/usr/etc/tls/cert.pem", 1);
    /* The package owns the patched binary: never let v2 replace it. */
    setenv("OPENCODE_DISABLE_AUTOUPDATE", "1", 1);

    char real_bin[PATH_MAX];
    snprintf(real_bin, sizeof(real_bin), "%s/.local/share/opencode-v2/opencode.real", home);

    if (access(real_bin, X_OK) != 0) {
        fprintf(stderr, "opencode-v2: binary not found at %s\n", real_bin);
        fprintf(stderr, "opencode-v2: reinstall the package: pkg install --reinstall opencode-v2\n");
        return 1;
    }

    char **new_argv = malloc((argc + 1) * sizeof(char *));
    if (new_argv == NULL) {
        return 1;
    }

    new_argv[0] = real_bin;
    for (int i = 1; i < argc; i++) {
        new_argv[i] = argv[i];
    }
    new_argv[argc] = NULL;

    execv(real_bin, new_argv);

    perror("opencode-v2: execv");
    free(new_argv);
    return 1;
}

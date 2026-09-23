#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <libgen.h>
#include <limits.h>
#include <stdio.h>

int main(int argc, char** argv) {
    // 1. Clear conflicting Android Bionic preloads and search paths
    // (glibc binary cannot use Bionic libtermux-exec)
    unsetenv("LD_PRELOAD");
    unsetenv("LD_LIBRARY_PATH");

    // 2. Set dynamic Go resolver and SSL configurations for Termux environment
    setenv("GODEBUG", "netdns=cgo", 1);
    setenv("SSL_CERT_FILE", "/data/data/com.termux/files/usr/etc/tls/cert.pem", 1);

    // 3. Export wrapper path for the freebuff terminal-command broker.
    // Bun's process.execPath under `ld-linux … freebuff.real` resolves to the
    // loader ($PREFIX/glibc/lib/ld-linux-aarch64.so.1), so a broker spawn of
    // process.execPath with `--terminal-command-broker` fails and the TUI
    // reports "terminal command broker protocol response was missing".
    // The bundled freebuff.real is binary-patched (postinst) so yiT() uses
    // process.env.FB instead; it must always point at this native wrapper.
    setenv("FB", "/data/data/com.termux/files/usr/bin/freebuff", 1);

    // 4. Resolve HOME dynamically (never hardcode /data/.../home).
    const char* home = getenv("HOME");
    if (!home || !*home) {
        home = "/data/data/com.termux/files/home";
    }

    // 5. Construct paths for the glibc loader and the real binary.
    // In our deb structure, freebuff.real lives in ~/.local/share/freebuff/
    // and this bootstrapper is installed as $PREFIX/bin/freebuff.
    char* loader = "/data/data/com.termux/files/usr/glibc/lib/ld-linux-aarch64.so.1";
    char lib_path[] = "/data/data/com.termux/files/usr/glibc/lib";
    char real_bin[PATH_MAX];
    snprintf(real_bin, sizeof(real_bin), "%s/.local/share/freebuff/freebuff.real", home);

    // 6. Construct argument array for execv
    // Format: [loader, --library-path, lib_path, real_bin, ...original_args]
    char** new_argv = malloc((argc + 4) * sizeof(char*));
    if (!new_argv) {
        return 1;
    }

    new_argv[0] = loader;
    new_argv[1] = "--library-path";
    new_argv[2] = lib_path;
    new_argv[3] = real_bin;

    for (int i = 1; i < argc; i++) {
        new_argv[i + 3] = argv[i];
    }
    new_argv[argc + 3] = NULL;

    // 7. Execute the glibc loader to run the real binary
    execv(loader, new_argv);

    // If execv returns, an error occurred
    perror("execv");
    free(new_argv);
    return 1;
}

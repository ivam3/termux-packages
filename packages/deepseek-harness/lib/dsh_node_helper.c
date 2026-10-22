/*
 * dsh_node_helper.c - Bionic bootstrap for the glibc Node runtime used by dsh.
 *
 * The helper keeps the Termux/bionic environment clean, points Node at the
 * Termux glibc loader, and leaves a wrapper path behind so glibc-compat.js can
 * repair process.execPath for child Node processes.
 */

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TERMUX_PREFIX "/data/data/com.termux/files/usr"
#define TERMUX_HOME "/data/data/com.termux/files/home"

static const char *env_or(const char *name, const char *fallback) {
    const char *value = getenv(name);
    return (value != NULL && *value != '\0') ? value : fallback;
}

static void save_and_unset(const char *name, const char *save_name) {
    const char *value = getenv(name);
    if (value != NULL && *value != '\0') {
        setenv(save_name, value, 1);
    }
    unsetenv(name);
}

static void set_default(const char *name, const char *value) {
    if (getenv(name) == NULL) {
        setenv(name, value, 1);
    }
}

static void resolve_self(char *buffer, size_t size, const char *fallback) {
    ssize_t length = readlink("/proc/self/exe", buffer, size - 1);
    if (length > 0 && (size_t)length < size) {
        buffer[length] = '\0';
        return;
    }
    if (strlen(fallback) < size) {
        strcpy(buffer, fallback);
    } else {
        buffer[0] = '\0';
    }
}

int main(int argc, char **argv) {
    const char *prefix = env_or("PREFIX", TERMUX_PREFIX);
    const char *home = env_or("HOME", TERMUX_HOME);

    char share_dir[PATH_MAX];
    char node_bin[PATH_MAX];
    char loader[PATH_MAX];
    char glibc_lib[PATH_MAX];
    char compat[PATH_MAX];
    char wrapper[PATH_MAX];
    char cert[PATH_MAX];
    char script_shell[PATH_MAX];
    char npm_cache[PATH_MAX];
    char fallback_wrapper[PATH_MAX];

    snprintf(share_dir, sizeof(share_dir), "%s/.local/share/deepseek-harness", home);
    snprintf(node_bin, sizeof(node_bin), "%s/node/bin/node.real", share_dir);
    snprintf(loader, sizeof(loader), "%s/glibc/lib/ld-linux-aarch64.so.1", prefix);
    snprintf(glibc_lib, sizeof(glibc_lib), "%s/glibc/lib", prefix);
    snprintf(compat, sizeof(compat), "%s/share/deepseek-harness/glibc-compat.js", prefix);
    snprintf(cert, sizeof(cert), "%s/etc/tls/cert.pem", prefix);
    snprintf(script_shell, sizeof(script_shell), "%s/bin/sh", prefix);
    snprintf(npm_cache, sizeof(npm_cache), "%s/npm-cache", share_dir);
    snprintf(fallback_wrapper, sizeof(fallback_wrapper), "%s/bin/dsh-node", prefix);

    resolve_self(wrapper, sizeof(wrapper), fallback_wrapper);
    if (wrapper[0] == '\0') {
        snprintf(wrapper, sizeof(wrapper), "%s", fallback_wrapper);
    }

    if (access(loader, X_OK) != 0) {
        fprintf(stderr, "dsh-node: glibc loader not found at %s\n", loader);
        fprintf(stderr, "dsh-node: run 'apt install glibc-repo' and retry\n");
        return 1;
    }
    if (access(node_bin, X_OK) != 0) {
        fprintf(stderr, "dsh-node: Node runtime not found at %s\n", node_bin);
        fprintf(stderr, "dsh-node: reinstall the package: apt install --reinstall deepseek-harness\n");
        return 1;
    }

    save_and_unset("LD_PRELOAD", "_DSH_ORIG_LD_PRELOAD");
    save_and_unset("LD_LIBRARY_PATH", "_DSH_ORIG_LD_LIBRARY_PATH");

    setenv("_DSH_WRAPPER_PATH", wrapper, 1);
    set_default("SSL_CERT_FILE", cert);
    set_default("npm_config_script_shell", script_shell);
    set_default("npm_config_cache", npm_cache);
    set_default("npm_config_update_notifier", "false");

    const char *existing_options = getenv("NODE_OPTIONS");
    if (existing_options == NULL || strstr(existing_options, compat) == NULL) {
        size_t needed = strlen(compat) + 5;
        if (existing_options != NULL) {
            needed += strlen(existing_options) + 1;
        }
        char *options = malloc(needed);
        if (options == NULL) {
            perror("dsh-node: malloc");
            return 1;
        }
        if (existing_options != NULL && *existing_options != '\0') {
            snprintf(options, needed, "-r %s %s", compat, existing_options);
        } else {
            snprintf(options, needed, "-r %s", compat);
        }
        setenv("NODE_OPTIONS", options, 1);
        free(options);
    }

    char **new_argv = calloc((size_t)argc + 5, sizeof(char *));
    if (new_argv == NULL) {
        perror("dsh-node: calloc");
        return 1;
    }

    int index = 0;
    new_argv[index++] = loader;
    new_argv[index++] = "--library-path";
    new_argv[index++] = glibc_lib;
    new_argv[index++] = node_bin;
    for (int i = 1; i < argc; i++) {
        new_argv[index++] = argv[i];
    }
    new_argv[index] = NULL;

    execv(loader, new_argv);
    perror("dsh-node: execv");
    free(new_argv);
    return 1;
}

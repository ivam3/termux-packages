#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(int argc, char** argv) {
    // Static --help/--version: no Electron, instant, no X
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--help") == 0 || strcmp(argv[i], "-h") == 0) {
            printf("ZCode 3.10.2 — AI vibe coding harness (GLM-5.3)\n");
            printf("Usage: zcode [options] [path]\n\n");
            printf("Options:\n");
            printf("  --help, -h          Show this help message\n");
            printf("  --version, -v       Show version\n");
            printf("  --no-sandbox        Disable Chrome sandbox (required on Termux)\n\n");
            printf("CLI:\n");
            printf("  zcode --help        Show this help\n");
            printf("  zcode --version     Show version\n\n");
            printf("GUI (requires termux-x11):\n");
            printf("  termux-x11 :0 & DISPLAY=:0 zcode [path]\n");
            printf("  More: https://zcode.z.ai  |  https://t.me/Ivam3_Bot\n");
            return 0;
        }
        if (strcmp(argv[i], "--version") == 0 || strcmp(argv[i], "-v") == 0) {
            printf("zcode 3.10.2\n");
            return 0;
        }
    }

    unsetenv("LD_PRELOAD");
    setenv("GODEBUG", "netdns=cgo", 1);
    setenv("SSL_CERT_FILE", "/data/data/com.termux/files/usr/etc/tls/cert.pem", 1);
    setenv("ELECTRON_DISABLE_SANDBOX", "1", 1);
    setenv("CHROME_DISABLE_SANDBOX", "1", 1);
    // Stable rendering on Termux: software GL + X11 ozone
    setenv("LIBGL_ALWAYS_SOFTWARE", "1", 1);
    setenv("GDK_BACKEND", "x11", 1);
    setenv("ELECTRON_OZONE_PLATFORM_HINT", "x11", 1);
    setenv("FONTCONFIG_PATH", "/data/data/com.termux/files/usr/glibc/etc/fonts", 1);
    // Dark theme default (ZCode is dark UI; light Adwaita gives white window + white text)
    if (getenv("GTK_THEME") == NULL || strlen(getenv("GTK_THEME")) == 0) {
        setenv("GTK_THEME", "Adwaita:dark", 1);
    }

    char real_bin[] = "/data/data/com.termux/files/home/.local/share/zcode/zcode.real";
    char lib_path[] = "/data/data/com.termux/files/home/.local/share/zcode/lib";
    setenv("LD_LIBRARY_PATH", lib_path, 1);

    // zcode without args -> tip (GUI requires X)
    if (argc == 1) {
        fprintf(stderr, "zcode: GUI requires X11. Run: zcode --help for CLI help\n");
        fprintf(stderr, "For GUI: termux-x11 :0 & DISPLAY=:0 zcode [path]\n");
        fprintf(stderr, "More: https://zcode.z.ai\n");
        return 0;
    }

    // For any GUI launch, require DISPLAY
    int has_display = (getenv("DISPLAY") != NULL && strlen(getenv("DISPLAY")) > 0);
    if (!has_display) {
        fprintf(stderr, "zcode: GUI requires X11. No DISPLAY set.\n");
        fprintf(stderr, "Run: termux-x11 :0 & DISPLAY=:0 zcode [path]\n");
        fprintf(stderr, "For CLI: zcode --help\n");
        return 1;
    }

    // Has DISPLAY, launch Electron directly (native glibc)
    // Force software rendering: Mali/Adreno + Mesa glibc fails without swiftshader -> black window
    int has_no_sandbox = 0, has_disable_shm = 0, has_disable_gpu = 0, has_gl = 0, has_angle = 0, has_in_process = 0;
    for (int i=1;i<argc;i++) {
        if (strcmp(argv[i],"--no-sandbox")==0) has_no_sandbox=1;
        if (strcmp(argv[i],"--disable-dev-shm-usage")==0) has_disable_shm=1;
        if (strcmp(argv[i],"--disable-gpu")==0) has_disable_gpu=1;
        if (strncmp(argv[i],"--use-gl=",9)==0) has_gl=1;
        if (strncmp(argv[i],"--use-angle=",12)==0) has_angle=1;
        if (strcmp(argv[i],"--in-process-gpu")==0) has_in_process=1;
    }
    int extra = (has_no_sandbox?0:1) + (has_disable_shm?0:1) + (has_disable_gpu?0:1) + (has_gl?0:1) + (has_angle?0:1) + (has_in_process?0:1);
    char **new_argv = malloc((argc + 1 + extra) * sizeof(char*));
    if (!new_argv) return 1;
    new_argv[0]=real_bin;
    int j=1;
    if (!has_no_sandbox) new_argv[j++]="--no-sandbox";
    if (!has_disable_shm) new_argv[j++]="--disable-dev-shm-usage";
    if (!has_disable_gpu) new_argv[j++]="--disable-gpu";
    if (!has_gl) new_argv[j++]="--use-gl=angle";
    if (!has_angle) new_argv[j++]="--use-angle=swiftshader";
    if (!has_in_process) new_argv[j++]="--in-process-gpu";
    for (int i=1;i<argc;i++) new_argv[j++]=argv[i];
    new_argv[j]=NULL;

    // /dev/shm workaround via proot if needed (no root to chmod 1777 /dev/shm)
    if (access("/dev/shm", W_OK) != 0) {
        char shm_tmp[PATH_MAX];
        const char *tmpdir = getenv("TMPDIR");
        if (!tmpdir) tmpdir = "/data/data/com.termux/files/usr/tmp";
        snprintf(shm_tmp, sizeof(shm_tmp), "%s/shm", tmpdir);
        mkdir(shm_tmp, 0777);
        if (access("/data/data/com.termux/files/usr/bin/proot", X_OK)==0) {
            int proot_extra = 4;
            char **proot_argv = malloc((j + proot_extra + 1) * sizeof(char*));
            if (proot_argv) {
                int k=0;
                proot_argv[k++]="proot";
                proot_argv[k++]="-b";
                char bind_arg[PATH_MAX*2];
                snprintf(bind_arg, sizeof(bind_arg), "%s:/dev/shm", shm_tmp);
                proot_argv[k++]=bind_arg;
                for (int t=0; t<j; t++) proot_argv[k++]=new_argv[t];
                proot_argv[k]=NULL;
                execvp("proot", proot_argv);
            }
        }
    }
    execv(real_bin, new_argv);
    perror("execv");
    free(new_argv);
    return 1;
}

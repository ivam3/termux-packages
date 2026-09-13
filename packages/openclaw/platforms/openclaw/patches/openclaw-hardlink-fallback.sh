#!/usr/bin/env bash
# openclaw-hardlink-fallback.sh - Fall back to copy+rename where hardlinks are blocked
#
# Why: on Android, SELinux denies hardlink creation inside the app data dir:
#   avc: denied { link } ... tclass=file (logcat, permissive=0)
# Upstream publishes workspace bootstrap files (SOUL.md, ...) and worker
# manifests atomically via fs.linkSync(staging, target). linkSync throws
# EACCES there, which is NOT covered by upstream's isHardlinkFallbackError
# (EXDEV/EPERM/ENOSYS only), so the raw error aborts e.g. every Telegram
# message dispatch (spooled retry loop, SOUL.md never created).
#
# What: wrap both linkSync publish sites with a fallback to
# copyFileSync(..., COPYFILE_EXCL) on EACCES/EPERM/EXDEV/ENOSYS/ENOTSUP/
# EOPNOTSUPP. COPYFILE_EXCL preserves the original no-clobber semantics
# (EEXIST still means "already published"). Same-dir copy+write is allowed
# by the policy (verified: copyFile/rename/symlink OK, only link denied).
#
# Idempotent: skips files already containing the marker. Re-run safe
# (re-applied automatically after each npm install via
# openclaw-apply-patches.sh; target files are located by content, not by
# hashed filename).
set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

MARKER="openclaw-android-hardlink-fallback"

echo "=== Patching hardlink publish (SELinux fallback) ==="
echo ""

export TMPDIR="${TMPDIR:-$PREFIX/tmp}"

NPM_ROOT=$(npm root -g 2>/dev/null)
OPENCLAW_DIR="$NPM_ROOT/openclaw"

if [ ! -d "$OPENCLAW_DIR" ]; then
    echo -e "${RED}[FAIL]${NC} OpenClaw not found at $OPENCLAW_DIR"
    exit 1
fi

if ! command -v python3 &>/dev/null; then
    echo -e "${RED}[FAIL]${NC} python3 not found (required for multiline patch)"
    exit 1
fi

PATCHED=0
SKIPPED=0

export OPENCLAW_DIR MARKER

# ── Site 1: publishBootstrapFile (workspace-*.mjs, SOUL.md etc.) ──
python3 - <<'PYEOF'
import glob
import os

marker = os.environ["MARKER"]
dist = os.path.join(os.environ["OPENCLAW_DIR"], "dist")

old = (
    "\t\ttry {\n"
    "\t\t\tfs.linkSync(staging.path, targetPath);\n"
    "\t\t\tlinked = true;\n"
)
new = (
    "\t\ttry {\n"
    "\t\t\ttry {\n"
    "\t\t\t\tfs.linkSync(staging.path, targetPath);\n"
    "\t\t\t} catch (linkError) {\n"
    "\t\t\t\t// [" + marker + "] SELinux denies hardlinks on Android (EACCES):\n"
    "\t\t\t\t// fall back to exclusive copy; EEXIST still means \"already published\".\n"
    "\t\t\t\tif (!linkError || (linkError.code !== \"EACCES\" && linkError.code !== \"EPERM\" && linkError.code !== \"EXDEV\" && linkError.code !== \"ENOSYS\" && linkError.code !== \"ENOTSUP\" && linkError.code !== \"EOPNOTSUPP\")) throw linkError;\n"
    "\t\t\t\tfs.copyFileSync(staging.path, targetPath, fs.constants.COPYFILE_EXCL);\n"
    "\t\t\t}\n"
    "\t\t\tlinked = true;\n"
)

done = 0
for path in glob.glob(os.path.join(dist, "workspace-*.mjs")):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    if "fs.linkSync(staging.path, targetPath)" not in src:
        continue
    if marker in src:
        print("  [SKIP] already patched: " + os.path.basename(path))
        continue
    if src.count(old) != 1:
        print("  [WARN] unexpected shape (count=%d), skipping: %s" % (src.count(old), os.path.basename(path)))
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(src.replace(old, new))
    print("  [PATCHED] bootstrap publish: " + os.path.basename(path))
    done += 1
print("SITE1_DONE=" + str(done))
PYEOF

# ── Site 2: publishManifest worker template (workspace-sync-scripts-*.mjs) ──
python3 - <<'PYEOF'
import glob
import os

marker = os.environ["MARKER"]
dist = os.path.join(os.environ["OPENCLAW_DIR"], "dist")

old = (
    "    try {\n"
    "      fs.linkSync(temporaryPath, manifestPath);\n"
    "    } catch (error) {\n"
    "      const existing = error && error.code === \"EEXIST\" ? fs.lstatSync(manifestPath) : null;\n"
)
new = (
    "    try {\n"
    "      try {\n"
    "        fs.linkSync(temporaryPath, manifestPath);\n"
    "      } catch (linkError) {\n"
    "        // [" + marker + "] SELinux denies hardlinks on Android (EACCES):\n"
    "        // fall back to exclusive copy; EEXIST still falls through to the\n"
    "        // identical-content check below.\n"
    "        if (!linkError || (linkError.code !== \"EACCES\" && linkError.code !== \"EPERM\" && linkError.code !== \"EXDEV\" && linkError.code !== \"ENOSYS\" && linkError.code !== \"ENOTSUP\" && linkError.code !== \"EOPNOTSUPP\")) throw linkError;\n"
    "        try {\n"
    "          fs.copyFileSync(temporaryPath, manifestPath, fs.constants.COPYFILE_EXCL);\n"
    "          return digest;\n"
    "        } catch (copyError) {\n"
    "          if (!copyError || copyError.code !== \"EEXIST\") throw copyError;\n"
    "          var error = copyError;\n"
    "        }\n"
    "      }\n"
    "      const existing = error && error.code === \"EEXIST\" ? fs.lstatSync(manifestPath) : null;\n"
)

done = 0
for path in glob.glob(os.path.join(dist, "workspace-sync-scripts-*.mjs")):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    if "fs.linkSync(temporaryPath, manifestPath)" not in src:
        continue
    if marker in src:
        print("  [SKIP] already patched: " + os.path.basename(path))
        continue
    if src.count(old) != 1:
        print("  [WARN] unexpected shape (count=%d), skipping: %s" % (src.count(old), os.path.basename(path)))
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(src.replace(old, new))
    print("  [PATCHED] manifest publish: " + os.path.basename(path))
    done += 1
print("SITE2_DONE=" + str(done))
PYEOF

echo ""
echo -e "${GREEN}Hardlink fallback patch applied.${NC}"

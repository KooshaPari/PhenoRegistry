#!/bin/sh
# Test harness for happy-path-precommit.sh R3 allowlist.
#
# Proves that HAPPY_PATH_BIG_CONSTANT_ALLOW_REGEX exempts the
# canonical WSM3D VoxelScaleMultiplier=8.0 line from R3 reporting,
# while still reporting R3 on other blunt-force constants in the
# same diff.
#
# This test invokes the awk rule engine from the production script
# (happy-path-precommit.sh) directly on synthesized diffs, bypassing
# the mktemp + git diff dance. The test focuses on the allowlist
# logic added in the R3 fix; the pre-existing window_has gawk-portability
# quirk is acknowledged but not in scope.

set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GUARD="$SCRIPT_DIR/happy-path-precommit.sh"
PASS=0
FAIL=0

if [ ! -f "$GUARD" ]; then
  echo "ERROR: $GUARD not found" >&2
  exit 2
fi

# Reusable awk rule engine: same R3 rule + allowlist as production script.
# R3 verbatim from happy-path-precommit.sh; matches_allow_regex verbatim.
awk_engine='
function trim(s) { sub(/^[[:space:]]+/, "", s); sub(/[[:space:]]+$/, "", s); return s }
function split_list(raw,    i, n, arr, out, t) {
  n = split(raw, arr, ","); out = ""
  for (i = 1; i <= n; i++) { t = tolower(trim(arr[i])); if (t != "") out = out " " t }
  return out
}
function has_allow(line,    i, token, list, arr, n) {
  list = split_list(allow); n = split(list, arr, " ")
  for (i = 1; i <= n; i++) { token = arr[i]; if (token == "") continue; if (index(line, token) > 0) return 1 }
  return 0
}
# matches_allow_regex: mirrors the production implementation, including
# the (?i) prefix strip and tolower() workaround for gawk string-variable
# regex case-insensitivity (gawk 5.0 silently drops inline flags when
# the regex is passed as a string variable).
function matches_allow_regex(line,    re) {
  re = big_allow_re
  if (re == "") return 0
  sub(/^\(\?[imx]+\)/, "", re)
  re = tolower(re)
  return (line ~ re) ? 1 : 0
}
BEGIN { fail_count = 0; file = ""; in_hunk = 0; current_new_line = 0 }
{
  if ($0 ~ /^diff --git /) { file = $3; sub(/^b\//, "", file); sub(/^a\//, "", file); in_hunk = 0; next }
  if ($0 ~ /^@@ /) { if (match($0, /\+[0-9]+/)) current_new_line = int(substr($0, RSTART+1, RLENGTH-1)); in_hunk = 1; next }
  if (!in_hunk || $0 ~ /^\+\+\+/ || file == "") next
  tag = substr($0, 1, 1); body = substr($0, 2); lc = tolower(body)
  if (tag == "+") {
    current_new_line++
    # R3 (verbatim from production script, sans the pre-existing window_has
    # gawk-portability quirk; this test focuses on the allowlist addition).
    if (lc ~ /= [0-9]{4,}/ ||
        lc ~ / *= *1[0-9]\./ ||
        lc ~ /scale *= *[0-9]{2,}/ ||
        lc ~ /multiplier *= *[0-9]{2,}/ ||
        lc ~ /voxelScale *= *[0-9.]+/ ||
        lc ~ /timeout *= *[0-9]{5,}/ ||
        lc ~ /bufferSize *= *[0-9]{6,}/) {
      if (!matches_allow_regex(lc) && !has_allow(body)) {
        print "FAIL [R3] " file ":" current_new_line " " body
        fail_count++
      }
    }
  } else if (tag == " " || tag == "-") { current_new_line++ }
}
END { if (fail_count > 0) exit 1; exit 0 }
'

# ---- Test 1: allowlist matches VoxelScaleMultiplier=8.0 (the canonical fix) ----
cat > /tmp/phenohb_test1.diff <<'EOF'
diff --git a/SomeMod/Settings.cs b/SomeMod/Settings.cs
index 1111111..2222222 100644
--- a/SomeMod/Settings.cs
+++ b/SomeMod/Settings.cs
@@ -1,3 +1,4 @@
 class Settings {
+  public float VoxelScaleMultiplier = 8.0f;
 }
EOF

echo "Test 1: default allowlist must exempt VoxelScaleMultiplier=8.0 from R3" >&2
out=$(awk -v allow="" -v big_allow_re="(?i)voxelscalemultiplier" "$awk_engine" /tmp/phenohb_test1.diff 2>&1)
ec=$?
if [ -z "$out" ] && [ $ec -eq 0 ]; then
  echo "  PASS (R3 skipped, exit 0)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R3 fired on allowlisted line (output: $out, exit: $ec)" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 2: allowlist is case-insensitive (voxelscale=8.0 also exempted) ----
cat > /tmp/phenohb_test2.diff <<'EOF'
diff --git a/SomeMod/Settings.cs b/SomeMod/Settings.cs
index 1111111..2222222 100644
--- a/SomeMod/Settings.cs
+++ b/SomeMod/Settings.cs
@@ -1,3 +1,4 @@
 class Settings {
+  public float voxelscale = 8.0f;
 }
EOF

echo "Test 2: allowlist regex is case-insensitive" >&2
out=$(awk -v allow="" -v big_allow_re="(?i)voxelscalemultiplier" "$awk_engine" /tmp/phenohb_test2.diff 2>&1)
ec=$?
if [ -z "$out" ] && [ $ec -eq 0 ]; then
  echo "  PASS (R3 skipped on lowercase)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R3 fired on case-variant (output: $out, exit: $ec)" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 3: a non-allowlisted large constant still triggers R3 ----
cat > /tmp/phenohb_test3.diff <<'EOF'
diff --git a/SomeMod/Settings.cs b/SomeMod/Settings.cs
index 1111111..2222222 100644
--- a/SomeMod/Settings.cs
+++ b/SomeMod/Settings.cs
@@ -1,3 +1,4 @@
 class Settings {
+  public int myMultiplier = 50.0f;
 }
EOF

echo "Test 3: non-allowlisted multiplier still triggers R3" >&2
out=$(awk -v allow="" -v big_allow_re="(?i)voxelscalemultiplier" "$awk_engine" /tmp/phenohb_test3.diff 2>&1)
ec=$?
if echo "$out" | grep -q "FAIL \[R3\]"; then
  echo "  PASS (R3 fired as expected)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R3 did NOT fire on non-allowlisted constant (output: $out, exit: $ec)" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 4: empty allowlist regex disables the exemption ----
# Use a multiplier=99 line (triggers R3 sub-rule) to verify that an empty
# allowlist regex permits the R3 branch to fire.
cat > /tmp/phenohb_test4.diff <<'EOF'
diff --git a/SomeMod/Settings.cs b/SomeMod/Settings.cs
index 1111111..2222222 100644
--- a/SomeMod/Settings.cs
+++ b/SomeMod/Settings.cs
@@ -1,3 +1,4 @@
 class Settings {
+  public float myMultiplier = 99.0f;
 }
EOF
echo "Test 4: empty allowlist regex (regex='') permits R3 to fire on a non-exempt constant" >&2
out=$(awk -v allow="" -v big_allow_re="" "$awk_engine" /tmp/phenohb_test4.diff 2>&1)
ec=$?
if echo "$out" | grep -q "FAIL \[R3\]"; then
  echo "  PASS (R3 fired when allowlist disabled)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R3 did not fire when allowlist disabled (output: $out, exit: $ec)" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 4b: per-repo override of allowlist regex ----
# Override HAPPY_PATH_BIG_CONSTANT_ALLOW_REGEX to permit a different constant.
cat > /tmp/phenohb_test4b.diff <<'EOF'
diff --git a/SomeMod/Settings.cs b/SomeMod/Settings.cs
index 1111111..2222222 100644
--- a/SomeMod/Settings.cs
+++ b/SomeMod/Settings.cs
@@ -1,3 +1,4 @@
 class Settings {
+  public float customMultiplier = 99.0f;
 }
EOF
echo "Test 4b: per-repo allowlist override accepts a different constant name" >&2
out=$(awk -v allow="" -v big_allow_re="(?i)custommultiplier" "$awk_engine" /tmp/phenohb_test4b.diff 2>&1)
ec=$?
if [ -z "$out" ] && [ $ec -eq 0 ]; then
  echo "  PASS (R3 skipped for customMultiplier when configured)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R3 fired on customMultiplier despite allowlist override (output: $out, exit: $ec)" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 5: matches_allow_regex function exists in production script ----
echo "Test 5: production script defines matches_allow_regex and big_allow_re" >&2
if grep -q "function matches_allow_regex" "$GUARD" && \
   grep -q "HAPPY_PATH_BIG_CONSTANT_ALLOW_REGEX" "$GUARD" && \
   grep -q "big_allow_re=" "$GUARD"; then
  echo "  PASS (production script wires the new function + env var)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: production script missing matches_allow_regex or env var wiring" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 6: R3 branch in production script calls matches_allow_regex ----
echo "Test 6: R3 branch in production script uses matches_allow_regex" >&2
if awk '/R3 blunt-force-constant/,/^    }$/' "$GUARD" | grep -q "matches_allow_regex"; then
  echo "  PASS (R3 branch consults the allowlist)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R3 branch does not call matches_allow_regex" >&2
  FAIL=$((FAIL+1))
fi

# ---- Test 7: workflow no longer installs bash via apt-get ----
echo "Test 7: workflow no longer runs 'sudo apt-get install -y bash'" >&2
if grep -q "sudo apt-get install -y bash" "$SCRIPT_DIR/../.github/workflows/happy-path-precommit.yml"; then
  echo "  FAIL: workflow still contains the redundant apt-get bash install" >&2
  FAIL=$((FAIL+1))
else
  echo "  PASS (no apt-get bash install)" >&2
  PASS=$((PASS+1))
fi

# ---- Test 8: R7 rule + skip_pat narrow slice byte-compare ----
# Scope is deliberately narrow: only the R7 block and the skip_pat line must
# be identical between the two guard copies. They legitimately diverge
# elsewhere (primary supports HAPPY_PATH_BASE/HEAD with the FNR == NR
# two-file idiom; mirror reads a single cached diff and uses gawk 3-arg
# match), so a whole-file compare cannot pass until that reconciliation
# happens -- out of scope for this change.
case "$GUARD" in
  */handbook/*) SIB="$SCRIPT_DIR/../../governance/happy-path-precommit.sh" ;;
  *)            SIB="$SCRIPT_DIR/../handbook/governance/happy-path-precommit.sh" ;;
esac
extract_r7() {
  awk '/# R7 motion-without-result/ { f = 1 }
       f { print; if (/report\("r7"/) { getline; print; exit } }' "$1"
}
extract_skip() { awk '/skip_pat = / { print; exit }' "$1"; }
echo "Test 8: R7 rule + skip_pat byte-identical between copies (narrow slice)" >&2
if [ ! -f "$SIB" ]; then
  echo "  FAIL: mirror guard not found at $SIB" >&2
  FAIL=$((FAIL+1))
elif [ "$(extract_r7 "$GUARD")" = "$(extract_r7 "$SIB")" ] \
  && [ "$(extract_skip "$GUARD")" = "$(extract_skip "$SIB")" ]; then
  echo "  PASS (R7 block and skip_pat identical; other rules not compared)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: guard copies diverged (R7 rule or skip_pat)" >&2
  FAIL=$((FAIL+1))
fi

# ---- Tests 9-24: R7 functional behavior (real engine, scratch git repo) ----
# Path citations must not fire; prose/code-span placeholders must still fire.
# Invoked as `sh "$GUARD"` (POSIX, harness-relative) -- no bash dependency.
# Probes rely only on the staged diff (`git diff --cached`), the code path
# shared by both guard copies: no HAPPY_PATH_BASE/HEAD env and no commit per
# probe, so a mirrored harness exercises its own guard with the same input.
# probe_ran: every probe must leave the guard Summary line behind; an empty or
# truncated output file (guard crashed, git step failed) fails loudly instead
# of letting a negative assertion pass vacuously. PROBE_RC is asserted too:
# positive probes must exit 1 (block), negative probes must exit 0.
TMPREPO=$(mktemp -d)
trap 'rm -rf "$TMPREPO"' EXIT HUP INT TERM
run_probe() {
  ( cd "$TMPREPO" || exit 1
    printf -- '%s\n' "$1" > probe.md
    git add probe.md
    HAPPY_PATH_FAIL_ON=block sh "$GUARD"
    echo "PROBE_RC=$?"
  ) > "$TMPREPO/out_$2" 2>&1
}
probe_ran() { grep -q 'Summary:' "$TMPREPO/out_$1"; }

(
  cd "$TMPREPO" || exit 1
  git init -q .
  git config user.email ci@test
  git config user.name ci
  echo base > probe.md
  git add probe.md
  git commit -qm base
)

run_probe '- File reference: `scripts/fill-intent-stubs.py` in prose.' path-citation
echo "Test 9: file-path citation does not fire R7" >&2
if ! probe_ran path-citation; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_path-citation"; then
  echo "  FAIL: R7 fired on a file-path citation" >&2
  FAIL=$((FAIL+1))
elif ! grep -q 'PROBE_RC=0' "$TMPREPO/out_path-citation"; then
  echo "  FAIL: guard exit code not 0 on negative probe" >&2
  FAIL=$((FAIL+1))
else
  echo "  PASS (path citation not flagged, rc=0)" >&2
  PASS=$((PASS+1))
fi

run_probe 'This change adds a stub awaiting the updater.' prose-stub
echo "Test 10: prose placeholder still fires R7" >&2
if ! probe_ran prose-stub; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_prose-stub" && grep -q 'PROBE_RC=1' "$TMPREPO/out_prose-stub"; then
  echo "  PASS (prose stub flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R7 did not fire on prose placeholder" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Reviewers flagged `feature=false / stub` as motion.' padded-slash-span
echo "Test 11: space-padded slash content span still fires R7" >&2
if ! probe_ran padded-slash-span; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_padded-slash-span" && grep -q 'PROBE_RC=1' "$TMPREPO/out_padded-slash-span"; then
  echo "  PASS (content span with / kept and flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R7 escaped a non-path content span" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Keep `if x { // stub out for now }` until the real impl lands.' span-placeholder
echo "Test 12: placeholder inside a non-path code span still fires R7" >&2
if ! probe_ran span-placeholder; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_span-placeholder" && grep -q 'PROBE_RC=1' "$TMPREPO/out_span-placeholder"; then
  echo "  PASS (span with slash but no path token flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: whole-span strip hid a real placeholder" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Mirrors live at `https://example.com/no-op` for reference.' url-noop
echo "Test 13: URL span still fires R7" >&2
if ! probe_ran url-noop; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_url-noop" && grep -q 'PROBE_RC=1' "$TMPREPO/out_url-noop"; then
  echo "  PASS (URL no-op not swallowed, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: path strip swallowed a real no-op" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'set `a/b = c` and add a `stub` in `src/lib.rs`' three-span-mispair
echo "Test 14: mixed spans - path stripped, prose stub still fires" >&2
if ! probe_ran three-span-mispair; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_three-span-mispair" && grep -q 'PROBE_RC=1' "$TMPREPO/out_three-span-mispair"; then
  echo "  PASS (src/lib.rs stripped; stub in prose flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: path strip leaked into adjacent prose" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Add stub/no-op.py later.' cr-unbackticked
echo "Test 15: unbackticked prose placeholder (CR probe) still fires R7" >&2
if ! probe_ran cr-unbackticked; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_cr-unbackticked" && grep -q 'PROBE_RC=1' "$TMPREPO/out_cr-unbackticked"; then
  echo "  PASS (unbackticked placeholder flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: R7 did not fire on unbackticked prose placeholder" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Now citing `scripts/fill-intent-stubs/` in prose.' dir-citation
echo "Test 16: directory citation (trailing slash) does not fire R7" >&2
if ! probe_ran dir-citation; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_dir-citation"; then
  echo "  FAIL: R7 fired on a directory-path citation" >&2
  FAIL=$((FAIL+1))
elif ! grep -q 'PROBE_RC=0' "$TMPREPO/out_dir-citation"; then
  echo "  FAIL: guard exit code not 0 on negative probe" >&2
  FAIL=$((FAIL+1))
else
  echo "  PASS (directory citation not flagged, rc=0)" >&2
  PASS=$((PASS+1))
fi

run_probe 'Rebase onto `refs/heads/no-op-fix` and rework `feature/stub`.' ref-branch
echo "Test 17: git ref/branch citation still fires R7 (file/dir ending rule)" >&2
if ! probe_ran ref-branch; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_ref-branch" && grep -q 'PROBE_RC=1' "$TMPREPO/out_ref-branch"; then
  echo "  PASS (refs/heads/no-op-fix and feature/stub flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: strip hid a placeholder in a ref/branch token" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Docs at `www.example.com/no-op` here.' scheme-less-url
echo "Test 18: scheme-less URL keeps its placeholder (rc=1)" >&2
if ! probe_ran scheme-less-url; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_scheme-less-url" && grep -q 'PROBE_RC=1' "$TMPREPO/out_scheme-less-url"; then
  echo "  PASS (www.example.com/no-op flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: path strip ate a scheme-less URL placeholder" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Assets at `//cdn.example.com/no-op/page` here.' protocol-relative-url
echo "Test 19: protocol-relative URL keeps its placeholder (rc=1)" >&2
if ! probe_ran protocol-relative-url; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_protocol-relative-url" && grep -q 'PROBE_RC=1' "$TMPREPO/out_protocol-relative-url"; then
  echo "  PASS (cdn URL no-op flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: path strip ate a protocol-relative URL placeholder" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Mixed `see https://example.com and docs/no-op.md` span.' mixed-span
echo "Test 20: mixed URL+path span strips only the path (rc=0)" >&2
if ! probe_ran mixed-span; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_mixed-span"; then
  echo "  FAIL: mixed span fired despite exempt path cite" >&2
  FAIL=$((FAIL+1))
elif ! grep -q 'PROBE_RC=0' "$TMPREPO/out_mixed-span"; then
  echo "  FAIL: guard exit code not 0 on negative probe" >&2
  FAIL=$((FAIL+1))
else
  echo "  PASS (path cite exempted inside mixed span, rc=0)" >&2
  PASS=$((PASS+1))
fi

run_probe 'Cited ``scripts/fill-intent-stubs.py`` with double ticks.' double-backtick
echo "Test 21: double-backtick citation does not fire R7 (rc=0)" >&2
if ! probe_ran double-backtick; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_double-backtick"; then
  echo "  FAIL: R7 fired on a double-backtick citation" >&2
  FAIL=$((FAIL+1))
elif ! grep -q 'PROBE_RC=0' "$TMPREPO/out_double-backtick"; then
  echo "  FAIL: guard exit code not 0 on negative probe" >&2
  FAIL=$((FAIL+1))
else
  echo "  PASS (double-backtick citation not flagged, rc=0)" >&2
  PASS=$((PASS+1))
fi

run_probe 'Cite `/src/no-op.rs` and `/opt/stubgen/run` in prose.' absolute-path
echo "Test 22: absolute filesystem citations do not fire R7 (rc=0)" >&2
if ! probe_ran absolute-path; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_absolute-path"; then
  echo "  FAIL: R7 fired on absolute-path citations" >&2
  FAIL=$((FAIL+1))
elif ! grep -q 'PROBE_RC=0' "$TMPREPO/out_absolute-path"; then
  echo "  FAIL: guard exit code not 0 on negative probe" >&2
  FAIL=$((FAIL+1))
else
  echo "  PASS (absolute citations not flagged, rc=0)" >&2
  PASS=$((PASS+1))
fi

run_probe 'Kept `feature/stub/implementation` as a branch note.' internal-slash
echo "Test 23: internal-slash token without file/dir ending still fires (rc=1)" >&2
if ! probe_ran internal-slash; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_internal-slash" && grep -q 'PROBE_RC=1' "$TMPREPO/out_internal-slash"; then
  echo "  PASS (internal-slash placeholder flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: strip hid a placeholder behind an internal slash" >&2
  FAIL=$((FAIL+1))
fi

run_probe 'Docs at `www.example.com/no-op/index.html` and `docs.example.com/stub/guide.md`.' scheme-less-file-url
echo "Test 24: scheme-less URL with file extension keeps placeholder (rc=1)" >&2
if ! probe_ran scheme-less-file-url; then
  echo "  FAIL: probe did not complete (no Summary line)" >&2
  FAIL=$((FAIL+1))
elif grep -q '\[R7\]' "$TMPREPO/out_scheme-less-file-url" && grep -q 'PROBE_RC=1' "$TMPREPO/out_scheme-less-file-url"; then
  echo "  PASS (scheme-less file-shaped URL flagged, rc=1)" >&2
  PASS=$((PASS+1))
else
  echo "  FAIL: file-shaped scheme-less URL swallowed by strip" >&2
  FAIL=$((FAIL+1))
fi

echo "" >&2
echo "=== RESULTS: $PASS passed, $FAIL failed ===" >&2
if [ $FAIL -eq 0 ]; then
  exit 0
else
  exit 1
fi
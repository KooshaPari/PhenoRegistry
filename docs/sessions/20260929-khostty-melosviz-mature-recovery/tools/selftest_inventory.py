#!/usr/bin/env python3
import json, subprocess, tempfile
from pathlib import Path
from source_inventory import inventory

def main():
 with tempfile.TemporaryDirectory(prefix="inventory-selftest-") as td:
  root=Path(td);repo=root/"repo";repo.mkdir()
  def cmd(*args):
   return subprocess.run(["git","-C",str(repo),*args],check=True,capture_output=True).stdout.decode().strip()
  cmd("init","-q");cmd("config","user.name","Recovery fixture");cmd("config","user.email","fixture@example.invalid")
  (repo/"same.txt").write_text("same");(repo/"change.txt").write_text("before");(repo/"gone.txt").write_text("old")
  (repo/"odd\nname.bin").write_bytes(b"\0\xff");(repo/"link").symlink_to("same.txt")
  cmd("add",".");cmd("commit","-qm","baseline");base=cmd("rev-parse","HEAD")
  (repo/"change.txt").write_text("after");(repo/"gone.txt").unlink();(repo/"new.txt").write_text("new")
  cmd("add","-A");cmd("commit","-qm","source");source=cmd("rev-parse","HEAD")
  report=inventory(repo,"SYNTHETIC_TEST_NOT_PRODUCT",source,base);rows={x["path"]:x for x in report["rows"]}
  tests={"current_entries":report["tracked_source_entries"]==5,"removed_entry_retained":rows["gone.txt"]["delta"]=="removed",
   "modified":rows["change.txt"]["delta"]=="modified","inherited":rows["same.txt"]["delta"]=="unchanged",
   "added":rows["new.txt"]["delta"]=="added","newline_filename":rows["odd\nname.bin"]["kind"]=="blob",
   "symlink_mode":rows["link"]["mode"]=="120000","no_semantic_false_green":all(not any(x["resolution_checks"].values()) for x in report["rows"])}
  try: inventory(repo,"SYNTHETIC", "main");tests["moving_ref_rejected"]=False
  except ValueError:tests["moving_ref_rejected"]=True
  out=dict(subject="INVENTORY_TOOL_SELFTEST_NOT_PRODUCT",checks=tests,all_passed=all(tests.values()))
  print(json.dumps(out,indent=2));return out
if __name__=="__main__":
 r=main();Path(__file__).with_name("inventory-selftest.json").write_text(json.dumps(r,indent=2)+"\n")
 raise SystemExit(0 if r["all_passed"] else 1)

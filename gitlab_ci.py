#!/usr/bin/env python3
import os
from old_versions import OLD_VERSIONS, main

main()


def run(c):
    print(f"RUN {c}")
    os.system(c)


run("mkdir .public")
run("cp *txt *.html .public/")
run("cp -r html .public/")
run("cp -r pdf .public/")
for ov in OLD_VERSIONS:
    run(f"cp -r {ov} .public/")
run("rm -rf public")
run("mv .public public")

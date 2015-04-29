#!/usr/bin/env python
# fixes the static links in sphinx

# !!! ONLY RUN THIS ONCE !!!

import os
import subprocess as sp
os.chdir(os.path.expanduser("~/documentation/html/"))
ROOT = os.path.abspath(os.curdir)

for link in sp.Popen("find -type l -name _static".split(), stdout=sp.PIPE).stdout:
  d = os.path.normpath(os.path.join(ROOT, link.rsplit("/", 1)[0]))
  print d
  os.chdir(d)
  os.system(r'find -type f -name "*.html" -exec sed -i "s/_static/..\/_static/" {} \;')


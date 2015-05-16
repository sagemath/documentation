#!/usr/bin/env python
# index for the documentation
from glob import glob
from collections import defaultdict

LANG = {
    "en": "English",
  "hu": "Hungarian",
  "pt": "Portuguese",
  "de": "German",
  "ru": "Russian",
  "fr": "French",
  "it": "Italian",
  "ca": "Catalan"
}

output = ["""\
<!DOCTYPE html>
<head>
<link rel="stylesheet" href="html/en/website/_static/sage.css" type="text/css" />
<style>
html {margin: 20px; }
body { background-color: white; }
</style>
<link rel="shortcut icon" href="html/en/website/_static/favicon.ico"/>
</head>
<body>
"""]

pages = {"html": defaultdict(list), "pdf": defaultdict(list)}

for path in glob("*/*"):
    what, lang = path.split("/")

    for path2 in glob(path + "/*"):
        if what == "html":
            EXT = "/index.html"
            for fn in glob(path2 + EXT):
                pages[what][lang].append(fn)
        elif what == "pdf":
            for EXT in ["/*.pdf", "/*/*.pdf"]:
                for fn in glob(path2 + EXT):
                    pages[what][lang].append(fn)


output.append("<h1>Documentation</h1>")

for what in sorted(pages.keys()):
    output.append("<h2>%s</h2>" % what.upper())
    output.append("<ul>")
    for lang, entries in sorted(pages[what].iteritems()):
        output.append("<li>%s</li>" % LANG.get(lang, lang))
        output.append("<ul>")
        for entry in entries:
            if what == "html":
                fn = entry.split("/")[-2].replace("_", " ").title()
            elif what == "pdf":
                fn = entry.split(
                    "/")[-1][:-4].replace("_",
                                          " ").title() + " (PDF)"
            output.append("<li><a href='{path}'>{fn}</a></li>".format(
                          path=entry,
                          lang=LANG.get(lang, lang),
                          fn=fn))
        output.append("</ul>")
    output.append("</ul>")
    output.append("</body></html>")

with open("index.html", "w") as index:
    index.write("\n".join(output))

import sys
if len(sys.argv) > 1 and sys.argv[1] == "fix":
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
        os.system(
            r'find -type f -name "*.html" -exec sed -i "s/_static/..\/_static/" {} \;')

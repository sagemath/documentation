#!/usr/bin/env python3
# Custom index for the SageMath Documentation
# Purpose: It generates the index files needed for the CDN.
#
# Usage:
# Run it only **once** (!) with the argument "fix" to repair all those
# relative static links. That's necessary to work well with the CDN
# network at GitHub. (later, run it without "fix")
#
# After indexing, check the index.html file and maybe blacklist more PDFs (many are just pictures)
# by appending to the `filter_ref` list.
#
# Note: the script assumes the html and pdf files are copied after
# running doc-html and doc-pdf targets. e.g. like this:
# $ nice ionice -c 3 sh -c 'make -j4 && make doc-html && make doc-pdf'
# then copy
# $ cp -alR $SAGE_ROOT/local/share/doc/sage/pdf .
# $ cp -alR $SAGE_ROOT/local/share/doc/sage/html .
#
# License: Apache 2.0
# Author: Harald Schilly <harald.schilly@gmail.com>

from glob import glob
from collections import defaultdict

LANG = {
    "en": "English",
    "es": "Spanish",
    "hu": "Hungarian",
    "pt": "Portuguese",
    "de": "German",
    "ru": "Russian",
    "fr": "French",
    "it": "Italian",
    "ca": "Catalan",
    "tr": "Turkish",
    "ja": "Japanese",
}

intro = """\
<!DOCTYPE html>
<head>
<title>SageMath Documentation %(path)s</title>
<link rel="stylesheet" href="/html/en/website/_static/sage.css" type="text/css" />
<style>
html {margin: 20px; font-family: sans-serif; }
body { background-color: white; }
h2 { margin: 0;}
a {text-decoration: none;}
a:hover {text-decoration: underline; }
div.table { display: table; }
div.row { display: table-row; margin: 0.5em 0; }
div.row:hover {background: #eef; }
div.cell { display: table-cell; padding: 0 2em 0 0; line-height: 2em;}
div.lang {font-weight: bold; }
div.row.en {border: 1px solid #ccf;}
div.row.last {height: 3em;}
div.entry {margin: 1em 1em 1em 0; display: inline; white-space: nowrap;}
div.entry.lang-en {font-weight: bold;}
</style>
<link rel="shortcut icon" href="/html/en/website/_static/favicon.ico"/>
</head>
<body>
<a href="http://www.sagemath.org/">
<img width="350" alt="SageMath Logo"
style="border-radius: 10px;"
src="http://www.sagemath.org/pix/sage_logo_new_l_hc_edgy-nq8.png"
title="SageMath Mathematical Software">
</a>
"""

filter_ref = [
    "graph-",
    "graph_plot-",
    "shapes-",
    "plot3d-",
    "platonic-",
    "knot-",
    "graph_generators-",
    "dyck_word-",
    "hyperbolic_regular_polygon-",
    "plot-",
    "generic_graph-",
    "fully_packed_loop",
    "link-",
    "complex_plot-",
    "hyperbolic_geodesic-",
    "contour_plot-",
    "density_plot-",
    "plot_field-",
    "chart-",
    "point_configuration-",
    "text-",
    "point-",
    "parametric_plot3d-",
    "revolution_plot3d-",
    "ordered_tree-",
    "implicit_plot3d-",
    "polygon-",
    "streamline_plot-",
    "vectorfield-",
    "tangent_vector-",
    "curve-",
    'hyperbolic_polygon-',
    "arrow-",
    "circle-",
    "bezier_path-",
    "mv_polytopes-",
    "set_partition-",
    "finite_coxeter_groups-",
    "integrated_curve-",
    "list_plot3d-",
    "calculus-",
    "index_face_set-",
    "multigraphics-",
    "vector_calc_cartesian-",
    "vector_calc_change-",
    "vector_calc_plane-",
]
filter_html = [("en", "website")]

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

output = [intro % {"path": ""}]
output.append("<h1>Documentation</h1>")

output.append('<div class="table">')
for what in sorted(pages.keys()):
    output.append('<div class="row first">')
    output.append("<div class='cell'><h2>%s</h2></div>" % what.upper())
    first_row = True
    for lang, entries in sorted(pages[what].items()):
        if not first_row:
            output.append(f'<div class="row {lang}"><div class="cell"></div>')
        else:
            first_row = False
        output.append('<div class="cell lang"><a href="%s/%s">%s</a></div>' %
                      (what, lang, LANG.get(lang, lang)))
        output.append('<div class="cell doc">')
        for entry in sorted(entries):
            entries = entry.split("/")
            if what == "html":
                if tuple(entries[-3:-1]) in filter_html:
                    continue
                fn = entries[-2].replace("_", " ").title()
                subcat = ""
            elif what == "pdf":
                if any(entries[-1].startswith(_) for _ in filter_ref):
                    continue
                fn = entries[-1][:-4] \
                    .replace("_", " ") \
                    .title()# + " (pdf)"
                if len(entries) >= 5:
                    subcat = entries[2].title()[:3] + ": "
                else:
                    subcat = ""
            output.append(
                "<div class='entry lang-{lang}'><a href='{path}'>{subcat}{fn}</a></div>"
                .format(
                    path=entry,
                    lang=lang,
                    # lang=LANG.get(lang, lang),
                    subcat=subcat,
                    fn=fn))
        output.append("</div></div>")
    output.append('<div class="row last"></div>')
output.append("</div>")
output.append("</body></html>")

with open("index.html", "w") as index:
    index.write("\n".join(output))

# create minimal index.html files in subdirectories
IDX_TOKEN = "<!-- generated by index.py -->"  # to recognize it later on!
from os import walk, sep
from os.path import join
for subdir in ["html", "pdf"]:
    for root, path, filenames in walk(subdir + sep):
        # ignore files in _static, ...
        root_dirs = root.split(sep)
        if any(_.startswith("_") for _ in root_dirs):
            continue
        # if there is no index.html file
        idxfn = join(root, "index.html")
        if "index.html" not in filenames or IDX_TOKEN in open(idxfn,
                                                              "r").read():
            # now we have to write our index.html file
            print(f"{root_dirs} >>> {idxfn}")
            index = [intro % {"path": root}]
            index.append(IDX_TOKEN)
            if len(root_dirs) > 1:
                index.append('<p><a href="%s">Home</a></p>' %
                             '/'.join([".."] * (len(root_dirs) - 1)))
            index.append('<p><a href="../index.html">Parent Directory</a></p>')
            path = list(filter(lambda _: not _.startswith("_"), path))
            if len(path) > 0:
                index.append('<h2>Sub-Directories</h2>')
                for p in sorted(path):
                    is_lang_list = len(root_dirs) == 1 or (
                        len(root_dirs) == 2 and root_dirs[1] == '')
                    name = LANG.get(p, p) if is_lang_list else p
                    index.append('<p><a href="%(p)s/">%(name)s</a></p>' % {
                        "p": p,
                        "name": name
                    })

            def f_op(fn):
                return not (fn == "index.html" or fn.startswith("genindex-")
                            or fn.startswith("."))

            filenames = list(filter(f_op, filenames))
            if len(filenames) > 0:
                index.append('<h2>Documents</h2>')
                for fn in sorted(filenames):
                    index.append('<p><a href="%(fn)s">%(fn)s</a></p>' %
                                 {"fn": fn})
            # print "    ", path, filenames
            index.append("</body></html>")
            with open(idxfn, "w") as outidx:
                outidx.write("\n".join(index))

import sys
if len(sys.argv) > 1 and sys.argv[1] == "fix":
    print(' fix the static links in sphinx _static files '.center(100, "#"))
    print(' ONLY RUN THIS ONCE '.center(100, "!"))

    import os
    import subprocess as sp
    os.chdir(os.path.join(os.path.dirname(__file__), "html"))
    ROOT = os.path.abspath(os.curdir)

    files_cmd = sp.Popen("find -type l -name _static".split(), stdout=sp.PIPE)
    for link in files_cmd.stdout:
        d = os.path.normpath(os.path.join(ROOT, link.rsplit("/", 1)[0]))
        print(d)
        os.chdir(d)
        os.system(
            r'find -type f -name "*.html" -exec sed -i "s/_static/..\/_static/" {} \;'
        )

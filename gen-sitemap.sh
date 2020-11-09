#!/usr/bin/env bash

echo 'https://doc.sagemath.org/index.html' > sitemap-html-html.txt
find -name '*.html' | cut -c2- | grep '^\/html\/' | grep -v '\/genindex-' | xargs -n1 printf 'https://doc.sagemath.org%s\n' >> sitemap-html-html.txt
find -name '*.html' | cut -c2- | grep '^\/pdf\/'  | xargs -n1 printf 'https://doc.sagemath.org%s\n' > sitemap-pdf-html.txt
find -name '*.pdf'  | cut -c2- | grep '^\/pdf\/'  | xargs -n1 printf 'https://doc.sagemath.org%s\n' > sitemap-pdf-pdf.txt


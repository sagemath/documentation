# SageMath Documentation Publication

This repository creates a GitHub page hosting the generated documentation files of [SageMath](https://sagemath.org).

**Bug reports and changes to the documentation itself have to go to http://trac.sagemath.org under the category "doc".**

## Purpose

The purpose of this repo is to do these things:

1. Apply a couple of patches on top of what SageMath provides (analytics code, disabling "thebe", ...).
2. Generated additional index pages (a CDN does not provide dynamically generated index pages, hence we have to create them on our own)
3. There are symlinks, causing all sorts of problems with CDNs, and hence some of the generated output has to be fixed.
4. Provide sitemaps to guide search engines with their quest to index the entire WWW!

## Usage

Please read the header doc of [index.py](index.py)

## License

In case anyone wonders, this is all Apache 2.0 and in particular, compatible with however SageMath is licensed.


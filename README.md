# SageMath Documentation Publication

The purpose of this repository is to create GitHub pages for the generated documentation pages of [SageMath](https://sagemath.org).

**Changes to the documentation itself should go to http://trac.sagemath.org under the category "doc".**

Besides that, the goal here is to do these things:

1. Apply a couple of patches on top of what SageMath provides (analytics code, disabling some "thebe", ...).
2. Generated additional index pages (a CDN does not provide dynamically generated index pages, hence we have to create them on our own)
3. There are symlinks, causing all sorts of problems with CDNs, and hence some of the genreated output has to be fixed.
4. Provide sitemaps to guide search engines with their quest to index the entire WWW!

## License

In case anyone wonders, this is all Apache 2.0 and in particular, compatible with what SageMath is licensed.


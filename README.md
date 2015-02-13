This repository contains the source for the paper:

Dembia, C., Moore, J. K., Hubbard, M. "An object oriented implementation of the
Yeadon human inertial model", 2014, DOI:
[10.12688/f1000research.5292.1](http://dx.doi.org/10.12688/f1000research.5292.1).

The paper is published at F1000Research:

http://f1000research.com/articles/3-223

A rendered version of the draft in this repository can be viewed at
[ShareLaTeX](htt://www.sharelatex.com):

[![PDF Status](https://www.sharelatex.com/github/repos/chrisdembia/python-yeadon-paper/builds/latest/badge.svg)](https://www.sharelatex.com/github/repos/chrisdembia/python-yeadon-paper/builds/latest/output.pdf)

License
=======

This work is licensed under a Creative Commons Attribution 4.0 International
License (http://creativecommons.org/licenses/by/4.0).

Build Instructions
==================

The LaTeX document requires these additional packages to be install alongside
LaTeX:

- hyperref
- cprotect
- float
- todonotes

The included `f1000_styles.sty` requires these packages: authblk, babel,
inputenc, fontenc, mathdesign, colortbl, xcolor, amsmath, graphicx, fancyhdr,
setspace, caption, lastpage, xifthen, todonotes, todonotes, geometry, titlesec.

To build, simply call make:

```
$ make
```

And view with your preferred pdf viewer, e.g.:

```
$ evince main.pdf
```

The extraneous files can removed with:

```
$ make clean
```

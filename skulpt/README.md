# Skulpt

Skulpt is a Javascript implementation of Python. This repository is a duplicate of [skulpt](https://github.com/skulpt/skulpt), created as it is no longer possible to make private versions of public forks on GitHub.

See the ORIG-README.md file for original comments from the original skulpt developers.

## Using Skulpt

Skulpt was duplicated and is used here for the addition of a python programming mode to the [Ocargo Coding for Life project](https://github.com/ocadotechnology/ocargo).

As set out in the rather minimal [skulpt documentation](http://www.skulpt.org/static/developer.html), addition of modules happens in src/lib. Here, there is a new van module to be developed to allow control of vans in the game. Fuller details of how to work and debug are given in HACKING, however minimal details are as follows:

1. Modules are defined in src/lib/<module_name>.
2. ``skulpt.py`` contains a range of functions for working with skulpt.
3. In particular, ``skulpt.py dist`` creates the two javascript files necessary for using the implementation: skulpt.min.js and skulpt-stdlib.js. These may be found under the dist directory.

## Dependencies

These aren't well documented! However, you will absolutely need Java and [GitPython](https://pythonhosted.org/GitPython/0.3.1/intro.html#) for creating the Javascript files as above.

## Information on including into a webpage

TODO!
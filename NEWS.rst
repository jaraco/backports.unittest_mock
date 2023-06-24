v1.5.1
======

No significant changes.


1.5
===

Refresh project metadata.

1.4
===

Package refresh. Added Pytest Trove classifier.

1.3
===

Merge with skeleton.

Use ``pkgutil`` for backports namespace package.

1.2.1
=====

Bump setuptools_scm and other skeleton updates, including:

- Drop support for `setup.py build_sphinx` because that usage
  conflicts with the usage required by readthedocs, which
  always runs the docs build from `./docs/` instead of `./`.
  Also drop support for build_sphinx because the dependency
  resolution of that command relies on easy_install, which is
  also deprecated. The proper way to build docs now is to
  install the requirements in docs/requirements.txt and then
  invoke sphinx natively.

1.2
===

Add support for Python 2.6 and 3.2.

1.1.1
=====

Issue #1: Added a test.

1.1
===

Moved hosting to Github.

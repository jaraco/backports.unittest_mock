.. image:: https://img.shields.io/pypi/v/backports.unittest_mock.svg
   :target: https://pypi.org/project/backports.unittest_mock

.. image:: https://img.shields.io/pypi/pyversions/backports.unittest_mock.svg

.. image:: https://img.shields.io/pypi/dm/backports.unittest_mock.svg

.. image:: https://img.shields.io/travis/jaraco/backports.unittest_mock/master.svg
   :target: http://travis-ci.org/jaraco/backports.unittest_mock

Provides a function "install()" which makes the "mock" module
available as "unittest.mock" on Python 3.2 and earlier.

Also advertises a pytest plugin which configures unittest.mock
automatically.


License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Docs
====

There's `no good mechanism for publishing documentation
<https://github.com/pypa/python-packaging-user-guide/pull/266>`_
easily. If there's a documentation link above, it's probably
stale because PyPI-based documentation is deprecated. This
project may have documentation published at ReadTheDocs, but
probably not. Good luck finding it.

Usage
=====

If using pytest, simply require this package in your test environment,
and `unittest.mock` will be available.

Otherwise, it must be invoked imperatively::

    import backports.unittest_mock
    backports.unittest_mock.install()

    import unittest.mock

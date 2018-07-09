.. image:: https://img.shields.io/pypi/v/backports.unittest_mock.svg
   :target: https://pypi.org/project/backports.unittest_mock

.. image:: https://img.shields.io/pypi/pyversions/backports.unittest_mock.svg

.. image:: https://img.shields.io/travis/jaraco/backports.unittest_mock/master.svg
   :target: https://travis-ci.org/jaraco/backports.unittest_mock

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/backports-unittest_mock/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/backports-unittest_mock/branch/master

.. image:: https://readthedocs.org/projects/backportsunittest_mock/badge/?version=latest
   :target: https://backportsunittest_mock.readthedocs.io/en/latest/?badge=latest

Provides a function "install()" which makes the "mock" module
available as "unittest.mock" on Python 3.2 and earlier.

Also advertises a pytest plugin which configures unittest.mock
automatically.

Usage
=====

If using pytest, simply require this package in your test environment,
and `unittest.mock` will be available.

Otherwise, it must be invoked imperatively::

    import backports.unittest_mock
    backports.unittest_mock.install()

    import unittest.mock

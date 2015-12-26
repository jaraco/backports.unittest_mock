backports.unittest_mock
=======================

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

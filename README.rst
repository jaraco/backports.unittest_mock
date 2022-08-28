.. image:: https://img.shields.io/pypi/v/backports.unittest_mock.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/backports.unittest_mock.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/backports.unittest_mock

.. image:: https://github.com/jaraco/backports.unittest_mock/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/jaraco/backports.unittest_mock/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

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

.. image:: https://img.shields.io/pypi/v/backports.unittest_mock.svg
   :target: https://pypi.org/project/backports.unittest_mock

.. image:: https://img.shields.io/pypi/pyversions/backports.unittest_mock.svg

.. image:: https://github.com/jaraco/backports.unittest_mock/workflows/tests/badge.svg
   :target: https://github.com/jaraco/backports.unittest_mock/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://readthedocs.org/projects/backportsunittest_mock/badge/?version=latest
   :target: https://backportsunittest_mock.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2023-informational
   :target: https://blog.jaraco.com/skeleton

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

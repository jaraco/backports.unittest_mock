import sys
import unittest


def install():
    "make mock appear from the future"
    if sys.version_info > (3,3):
        return

    mock = __import__('mock')
    sys.modules['unittest.mock'] = unittest.mock = mock


def pytest_configure():
	install()

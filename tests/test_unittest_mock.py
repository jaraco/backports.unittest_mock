def test_installed():
	"""
	Because tests are run under pytest, and because the pytest
	plugin would have been invoked before running this test,
	the import of `unittest.mock` should always succeed.
	"""
	__import__('unittest.mock')

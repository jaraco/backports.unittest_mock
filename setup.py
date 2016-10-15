#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

needs_wheel = set(['release', 'bdist_wheel', 'dists']).intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

name = 'backports.unittest_mock'
description = ''

setup_params = dict(
	name=name,
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/jaraco/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=[
	],
	extras_require={
		':python_version=="2.7" or'
		' python_version=="2.6" or'
		' python_version=="3.2"': [
			"mock",
		],
	},
	setup_requires=[
		'setuptools_scm==1.13.0',
	] + wheel,
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.2",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
	],
	entry_points={
		'pytest11': [
			"unittest_mock = backports.unittest_mock",
		],
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)

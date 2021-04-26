#!/usr/bin/env python

import io
import os
import re

from setuptools import setup


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering :: Visualization",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
]


def _read(*parts, **kwargs):
    filepath = os.path.join(os.path.dirname(__file__), *parts)
    encoding = kwargs.pop('encoding', 'utf-8')
    with io.open(filepath, encoding=encoding) as fh:
        text = fh.read()
    return text


def get_version():
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        _read('svgpath2mpl.py'),
        re.MULTILINE).group(1)
    return version


def get_long_description():
    return _read('README.rst')


install_requires = ['numpy', 'matplotlib']
tests_require = ['pytest']

setup(
    name='svgpath2mpl',
    author='Nezar Abdennur',
    author_email='nabdennur@gmail.com',
    version=get_version(),
    license='BSD',
    description='SVG path parser for matplotlib',
    long_description=get_long_description(),
    keywords=['svg', 'path', 'matplotlib', 'plotting', 'visualization'],
    url='https://github.com/nvictus/svgpath2mpl',
    py_modules=['svgpath2mpl'],
    zip_safe=False,
    classifiers=classifiers,
    install_requires=install_requires,
    tests_require=tests_require
)

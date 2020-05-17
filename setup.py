# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from setuptools import setup, find_packages

PKG_NAME = "jsbc.compat"


def get_version():
    with open('jsbc/compat/__init__.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=PKG_NAME,
    version=get_version(),
    author="jonisb",
    author_email="github.com@JsBComputing.se",
    description="Python compatibility library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonisb/jsbc.compat",
    #packages=[PKG_NAME],
    packages=find_packages(),
    #python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    namespace_packages=['jsbc']
)

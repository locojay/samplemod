# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='samplemod',
    version='0.0.1',
    description='',
    long_description=readme,
    author='locojay',
    author_email='locojay@locojaydev',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


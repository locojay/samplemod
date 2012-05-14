# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


install_requires = []
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
    install_requires=install_requires,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

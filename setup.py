#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='adspy',
    version="0.0.1",
    packages=find_packages(),
    description='engine for parsing ADwords in ADsPy django',
    author='Gabriele Santucci',
    maintainer='Gabriele Santucci',
    maintainer_email='gabrielesantucci1983@gmail.com',
    url='https://github.com/huli1984/adspy_public',
    license='',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=['requests', 'numpy', 'bs4', 'selenium', 'pandas'],
    tests_require=['requests', 'numpy', 'bs4', 'selenium', 'pandas'],
)

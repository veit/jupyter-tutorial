# !/usr/bin/env python

from __future__ import print_function

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name='jupyter-tutorial',
    packages=[],
    version='0.1.29',
    description='Jupyter Tutorial',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='Veit Schiele',
    license='BSD',
    author_email='veit@cusy.io',
    url='https://github.com/veit/cookiecutter-namespace-template',
    keywords=['jupyter', 'ipython',],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'Natural Language :: German',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Topic :: Desktop Environment',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development',
    ],
    install_requires=[
        'sphinx',
        'jupyter',
        'nbsphinx',
        'jupyter-sphinx',
        'pandas',
        'matplotlib',
        'cython',
        'memory-profiler',
        'pytest',
        'ipytest',
        'ipython-unittest',
        'jupyter-contrib-nbextensions',
        'widgetsnbextension',
        'yapf',
        'jupyter-latex-envs',
        'bqplot',
        'pythreejs',
        'ipyvolume',
        'ipyleaflet',
        'networkx',
        'autopep8',
        'numpy',
        'plotly<4',
        'cufflinks',
        'ipysheet',
        'jupyterhub',
    ],
)

if any(bdist in sys.argv for bdist in ['bdist_wheel', 'bdist_egg']):
    import setuptools

if __name__ == '__main__':
    setup(**setup_args)


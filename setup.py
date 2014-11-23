#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os.path as op
import io
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from pip.req import parse_requirements
from install_deps import get_requirements


#long description
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


# Get version without importing, which avoids dependency issues
module_name = find_packages(exclude=['tests'])[0]
version_pyfile = op.join(module_name, 'version.py')
exec(compile(read(version_pyfile), version_pyfile, 'exec'))


req_files = ['requirements.txt', 'pip_requirements.txt']

LICENSE = 'new BSD'


setup_dict = dict(
    name=module_name,
    version='0.1.0',
    description='Python code for ERD/ERS analysis of EEG.',
    long_description=read('README.rst', 'HISTORY.rst'),
    author='Miren Urteaga',
    author_email='mirenurteaga@gmail.com',
    maintainer='Alexandre M. Savio',
    maintainer_email='alexsavio@gmail.com',

    url='https://github.com/mirenurteaga/neurosync',
    extra_files=['HISTORY.rst', 'LICENSE', 'README.rst'],
    install_requires=get_requirements(*req_files),

    packages=[
        'neurosync',
        'neurosync.utils'
    ],
    package_dir={'neurosync':
                 'neurosync'},

    license=LICENSE,

    keywords='EEG',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    extras_require={
        'testing': ['pytest', 'pytest-cov'],
    }
)


# Python3 support keywords
if sys.version_info >= (3,):
    setup_dict['use_2to3'] = False
    setup_dict['convert_2to3_doctests'] = ['']
    setup_dict['use_2to3_fixers'] = ['']


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup_dict.update(dict(tests_require=['pytest'],
                       cmdclass={'test': PyTest}))


if __name__ == '__main__':
    setup(**setup_dict)

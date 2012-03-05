#!/usr/bin/env python
#
# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).


from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name = 'dcuolfg',
    version = __version__,
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    maintainer = 'Deryck Hodge',
    description = '',
    license = '',
    url = '',
    install_requires = [
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)

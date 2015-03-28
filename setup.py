#!/usr/bin/env python
# coding: utf-8

"""
    djangocms-widgets distutils setup
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyleft: 2015 by the djangocms-widgets team, see AUTHORS for more details.
    :created: by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import absolute_import, division, print_function


import os
import sys

from setuptools import setup, find_packages

from djangocms_widgets import VERSION_STRING


PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))


# convert creole to ReSt on-the-fly, see also:
# https://code.google.com/p/python-creole/wiki/UseInSetup
try:
    from creole.setup_utils import get_long_description
except ImportError as err:
    if "check" in sys.argv or "register" in sys.argv or "sdist" in sys.argv or "--long-description" in sys.argv:
        raise ImportError("%s - Please install python-creole >= v0.8 - e.g.: pip install python-creole" % err)
    long_description = None
else:
    long_description = get_long_description(PACKAGE_ROOT)


def get_authors():
    try:
        with open(os.path.join(PACKAGE_ROOT, "AUTHORS"), "r") as f:
            authors = [l.strip(" *\r\n") for l in f if l.strip().startswith("*")]
    except Exception as err:
        authors = "[Error: %s]" % err
    return authors



setup_info = dict(
    name='djangocms-widgets',
    version=VERSION_STRING,
    description='Widget plugin for django CMS',
    long_description=long_description,
    author=get_authors(),
    maintainer="Jens Diemer",
    url='',
    download_url = '',
    packages=find_packages(),
    include_package_data=True, # include package data under version control
    zip_safe=False,
    classifiers=[
       'Development Status :: 1 - Planning',
#        'Development Status :: 2 - Pre-Alpha',
#        'Development Status :: 3 - Alpha',
#         "Development Status :: 4 - Beta",
#         "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
#        "Intended Audience :: Education",
#        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        'Framework :: Django',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Operating System :: OS Independent",
    ]
)
setup(**setup_info)

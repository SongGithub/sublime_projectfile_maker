#!/usr/bin/env python

PROJECT = 'virtualenvwrapper-sublime'
VERSION = '0.0.5'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup,  find_packages

from distutils.util import convert_path
from fnmatch import fnmatchcase

import os
import sys

try:
    long_description = open('README', 'rt').read()
except IOError:
    long_description = ''

################################################################################
# find_package_data is an Ian Bicking creation.

# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build',
                                './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(
    where='.', package='',
    exclude=standard_exclude,
    exclude_directories=standard_exclude_directories,
    only_in_packages=True,
    show_ignored=False):
    """
    Return a dictionary suitable for use in ``package_data``
    in a distutils ``setup.py`` file.

    The dictionary looks like::

        {'package': [files]}

    Where ``files`` is a list of all the files in that package that
    don't match anything in ``exclude``.

    If ``only_in_packages`` is true, then top-level directories that
    are not packages won't be included (but directories under packages
    will).

    Directories matching any pattern in ``exclude_directories`` will
    be ignored; by default directories with leading ``.``, ``CVS``,
    and ``_darcs`` will be ignored.

    If ``show_ignored`` is true, then all the files that aren't
    included in package data are shown on stderr (for debugging
    purposes).

    Note patterns use wildcards, or can be exact paths (including
    leading ``./``), and all searching is case-insensitive.
    
    This function is by Ian Bicking.
    """

    out = {}
    stack = [(convert_path(where), '', package, only_in_packages)]
    while stack:
        where, prefix, package, only_in_packages = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "Directory %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                    stack.append((fn, '', new_package, False))
                else:
                    stack.append((fn, prefix + name + '/', package, only_in_packages))
            elif package or not only_in_packages:
                # is a file
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "File %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out
################################################################################

setup(
    name = PROJECT,
    version = VERSION,

    author='Song Jin',
    author_email='songjin@hotmail.com',
    url = 'https://github.com/SongGithub/sublime_projectfile_maker',

    classifiers = [ 'Development Status :: 5 - Production/Stable',
                'License :: OSI Approved :: BSD License',
                'Programming Language :: Python',
                'Intended Audience :: Developers',
                'Environment :: Console',
                ],

    platforms = ['Any'],

    provides=['virtualenvwrapper.sublime',
              ],
    requires=['virtualenv',
              'virtualenvwrapper (>=2.0)',
              ],
    description=('It create sublime project file ' 
                'as creating new virtualenv using mkproject'),
    #long_description=open('README.md').read(),
    
     
    namespace_packages = [ 'virtualenvwrapper' ],
    packages=find_packages(),
    include_package_data = True,
    # Scan the input for package information
    # to grab any data files (text, images, etc.) 
    # associated with sub-packages.
    package_data = find_package_data('virtualenvwrapper', 
                                     package='virtualenvwrapper',
                                     only_in_packages=False,
                                     ),

    entry_points = 
        {
    	'virtualenvwrapper.project.post_mkproject': 
            [
    	       'user_scripts = virtualenvwrapper.sublime:post_mkproject',
    	    ]
        },
    )
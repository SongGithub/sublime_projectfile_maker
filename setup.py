#!/usr/bin/env python

PROJECT = 'virtualenvwrapper-sublime'
VERSION = '0.0.6'

# Bootstrap installation of Distribute
from setuptools import setup,  find_packages

setup(
    name=PROJECT,
    version=VERSION,
    author='Song Jin',
    author_email='songjin@hotmail.com',
    url='https://github.com/SongGithub/sublime_projectfile_maker',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    platforms=['Any'],
    provides=['virtualenvwrapper.sublime'],
    requires=['virtualenv', 'virtualenvwrapper (>=2.0)'],
    description=(
        'It create sublime project file '
        'as creating new virtualenv using mkproject'
    ),
    long_description=open('README.rst').read(),
    namespace_packages=['virtualenvwrapper'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'virtualenvwrapper.project.post_mkproject': [
            'user_scripts = virtualenvwrapper.sublime:post_mkproject',
        ]
    },
)

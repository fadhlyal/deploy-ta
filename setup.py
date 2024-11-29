#!/usr/bin/env python

from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension
import os
import numpy

# Get the absolute path to the current directory (project root)
project_root = os.path.abspath(os.path.dirname(__file__))

extensions = Extension(
    'clara.pylpsolve',
    ['clara/pylpsolve.pyx'],
    libraries=['lpsolve55'],
    library_dirs=[
        project_root,  # Add project root to library search path
        os.path.join(project_root, 'lpsolve')
    ],
    include_dirs=[
        project_root,  # Project root
        os.path.join(project_root, 'lpsolve'),  # Specific lpsolve folder
        numpy.get_include()
    ],
    define_macros=[
        ('WIN32', None),
        ('NOMINMAX', None),
        ('_USRDLL', None),
        ('_MBCS', None),
        ('_CRT_SECURE_NO_WARNINGS', None),
        ('YY_NO_UNISTD_H', None),
        ('_WINDLL', None),
        ('_hypot', 'hypot'),
    ]
)

setup(name='clara',
      version='1.0',
      description='CLuster And RepAir tool for introductory programming assignments',
      author='Ivan Radicek',
      author_email='radicek@forsyte.at',
      url='https://github.com/iradicek/clara',
      packages=['clara'],
      ext_modules = cythonize(extensions),
      install_requires=['numpy', 'pycparser', 'zss'],
      scripts=['bin/clara'],
      entry_points={
          'console_scripts': [
              'clara=clara.cli:main',
            ],
      },
)

#!/usr/bin/env python

from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension
import os
import numpy

lpsolve_path = os.path.join(os.path.dirname(__file__), 'lpsolve')

extensions = Extension('clara.pylpsolve',
                       ['clara/pylpsolve.pyx'],
                       libraries=['lpsolve55'],
                       library_dirs=[lpsolve_path],
                       include_dirs=[
                           lpsolve_path,
                           numpy.get_include()],
                       define_macros=[
                           ('WIN32', None),
                           ('NOMINMAX', None),
                           ('_USRDLL', None),
                           ('_MBCS', None),
                           ('_CRT_SECURE_NO_WARNINGS', None),
                           ('YY_NO_UNISTD_H', None),
                           ('_WINDLL', None),
                           ('_hypot', 'hypot'),  # This prevents the macro redefinition
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

#!/usr/bin/env python3
# encoding: UTF-8


from distutils.core import setup

desc = """\
iPython Kepler Magic Function
==============
This pakcge will enhase ipython to use kepler workflows.

Kepler website:
https://kepler-project.org/

More inforamtion about this package:
https://github.com/hamidre13/IPython-Kepler-Magic-Function

This package is property of Words Group San Diego Super Computer Center:
http://words.sdsc.edu/
"""
setup(name='KeplerMagic',
      version='1.0',
      author  ='Hamid Tavakoli',
      author_email= 'stavakol@ucsd.edu',
      url='https://github.com/hamidre13/IPython-Kepler-Magic-Function',
      long_description=desc,
      py_modules=['KeplerMagicFunction','KeplerMagicLib'],
      )
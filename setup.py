#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

from django_forgiving_collectstatic import __version__

setup(
    name='django-forgiving-collectstatic',
    version=__version__,
    author='Tim Kamanin',
    author_email='tim@timonweb.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/timonweb/django-forgiving-collectstatic',
    license='MIT',
    description='An extension of the django.contrib.staticfiles.storage.ManifestStaticFilesStorage that skips missing files and assets during the python manage.py collectstatic command run.',
    long_description=open('README.md').read(),
    install_requires=[],
)
#!/usr/bin/env python

import os

from setuptools import find_packages, setup

from django_react_streamfield import __version__

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_PATH, "requirements.txt")) as f:
    required = f.read().splitlines()


setup(
    name="django-react-streamfield",
    version=__version__,
    author="Alex",
    author_email="alex@alexnewby.com",
    url="https://github.com/globophobe/django-react-streamfield",
    description="The brand new Wagtail StreamField!",
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
    license="BSD",
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    zip_safe=False,
)

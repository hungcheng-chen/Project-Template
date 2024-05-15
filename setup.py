#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

setup(
    author="HungCheng Chen",
    author_email="hcchen.nick@gmail.com",
    name="Project-Template",
    keywords="Project-Template",
    packages=find_packages(include=["Project-Template", "Project-Template.*"]),
    license="MIT license",
    version="0.1.0",
)

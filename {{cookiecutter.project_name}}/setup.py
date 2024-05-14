#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

setup(
    author="{{cookiecutter.full_name.replace('\"', '\\\"')}}",
    author_email="{{cookiecutter.email}}",
    name="{{cookiecutter.project_slug}}",
    license="{{cookiecutter.open_source_license}}",
    keywords="{{cookiecutter.project_slug}}",
    name="{{cookiecutter.project_slug}}",
    packages=find_packages(
        include=["{{cookiecutter.project_slug}}", "{{cookiecutter.project_slug}}.*"]
    ),
    test_suite="tests",
    version="{{cookiecutter.version}}",
)

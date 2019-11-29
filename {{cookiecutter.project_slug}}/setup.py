#!/usr/bin/env python

"""The setup script."""

from typing import List

from setuptools import find_packages
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements: List[str] = []

setup_requirements: List[str] = []

test_requirements: List[str] = []

{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}

setup(
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        "console_scripts": ["{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main"]
    },
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    zip_safe=False,
)

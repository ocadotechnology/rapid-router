# -*- coding: utf-8 -*-
import re
import sys

from setuptools import find_packages, setup

with open("game/__init__.py", "r") as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name="rapid-router",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django==3.2.20",
        "django-csp==3.7",
        "django-js-reverse==0.9.1",
        "django-pipeline==2.0.8",
        "djangorestframework==3.13.1",
        "more-itertools==8.7.0",
        "pyhamcrest==2.0.2",
        "libsass==0.22.0",
        "cfl-common",
    ],
    classifiers=["Programming Language :: Python", "Programming Language :: Python :: 3.8", "Framework :: Django"],
    version=version,
    zip_safe=False,
)

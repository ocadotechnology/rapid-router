# -*- coding: utf-8 -*-
import re
import sys

from setuptools import find_packages, setup

with open("game/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

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
        "django-reverse-js==0.1.7",
        "pyhamcrest==2.0.2",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: " "Python :: 3.12",
        "Framework :: Django",
    ],
    version=version,
    zip_safe=False,
)

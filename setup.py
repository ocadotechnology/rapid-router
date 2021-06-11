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
        "django==2.2.24",
        "django-js-reverse==0.9.1",
        "django-foundation-statics==5.4.7",
        "django-pipeline==1.6.14",  # Setting this to 1.6.14 as 1.7 causes issue with compiling SCSS files
        "djangorestframework==3.12.2",
        "more-itertools==8.6.0",
        "pyhamcrest==2.0.2",
        "libsass==0.20.1",
        "future==0.18.2",
        "cfl-common",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
    ],
    version=version,
    zip_safe=False,
)

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
        "django>=1.10.8, <= 1.11.24",
        "django-autoconfig >= 0.3.6, < 1.0.0",
        "django-js-reverse==0.9.1",
        "django-foundation-statics==5.4.7",
        "django-pipeline==1.6.14",
        "djangorestframework>=3.8.2, <3.9.0",
        "six==1.11.0",
        "more-itertools==5.0.0",
        "pyhamcrest==1.8.3",
        "libsass",
        "future",
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

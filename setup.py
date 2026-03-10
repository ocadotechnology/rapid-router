# -*- coding: utf-8 -*-
import json
import os
import re
import sys
import typing as t
from pathlib import Path

from setuptools import find_packages, setup

with open("game/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)


# Get the absolute path of the package.
PACKAGE_DIR = os.path.dirname(__file__)


def get_data_files(target_dir: Path):
    """Get the path of all files in a target directory relative to where they
    are located in the package. All subdirectories will be walked.

    Args:
        target_dir: The directory within the package to walk.

    Returns:
        A tuple where the values are (the absolute path to the target directory,
        the paths of all files within the target directory relative to their
        location in the package).
    """
    relative_file_paths: t.List[str] = []
    for dir_path, _, file_names in os.walk(target_dir):
        # Get the relative directory of the current directory.
        relative_dir = os.path.relpath(dir_path, PACKAGE_DIR)
        # Get the relative file path for each file in the current directory.
        relative_file_paths += [
            os.path.join(relative_dir, file_name) for file_name in file_names
        ]

    return str(target_dir), relative_file_paths


def parse_requirements(packages: t.Dict[str, t.Dict[str, t.Any]]):
    """Parse a group of requirements from `Pipfile.lock`.

    https://setuptools.pypa.io/en/latest/userguide/dependency_management.html

    Args:
        packages: The group name of the requirements.

    Returns:
        The requirements as a list of strings, required by `setuptools.setup`
    """

    requirements: t.List[str] = []
    for name, package in packages.items():
        requirement = name
        if "git" in package:
            requirement += f" @ git+{package['git']}"
            if "ref" in package:
                requirement += f"@{package['ref']}"
            if "subdirectory" in package:
                requirement += f"#subdirectory={package['subdirectory']}"
        elif "version" in package:
            if "extras" in package:
                requirement += f"[{','.join(package['extras'])}]"
            requirement += package["version"]
            if "markers" in package:
                requirement += f"; {package['markers']}"
        requirements.append(requirement)

    return requirements


# Parse Pipfile.lock into strings.
with open("Pipfile.lock", "r", encoding="utf-8") as pipfile_lock:
    lock = json.load(pipfile_lock)
    install_requires = parse_requirements(lock["default"])
    dev_requires = parse_requirements(lock["develop"])

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name="rapid-router",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: " "Python :: 3.12",
        "Framework :: Django",
    ],
    data_files=[
        get_data_files(Path(PACKAGE_DIR).joinpath("game/fixtures")),
    ],
    version=version,
    zip_safe=False,
)

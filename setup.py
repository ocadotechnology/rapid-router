# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import versioneer

setup(name='rapid-router',
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'django==1.7',
        'django-foundation-icons==3.1',
        'django-bourbon==3.1.8',
        'django-autoconfig==0.1.2',
        'django-jquery==1.9.1',
        'django-compressor==1.4',
        'django-foundation-statics==5.1.1',
        'django-appconf==0.6',
        'django-casper==0.0.2',
        'djangorestframework==3.1.3',
        'unittest2==0.5.1',
        'pyyaml==3.11',
        'six==1.6.1',
        'docutils==0.11',
        'Pillow==2.5.1',
    ],
    version=versioneer.get_version(),
)

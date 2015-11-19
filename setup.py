# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import versioneer

setup(name='rapid-router',
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'django==1.8.2',
        'django-foundation-icons==3.1',
        'django-bourbon==3.1.8',
        'django-autoconfig==0.3.6',
        'django-jquery==1.9.1',
        'django-js-reverse==0.6.1',
        'django-foundation-statics==5.4.7',
        'django-pipeline==1.5.4',
        'django-appconf==1.0.1',
        'django-casper==0.0.3',
        'djangorestframework==3.1.3',
        'unittest2==0.5.1',
        'pyyaml==3.11',
        'six==1.9.0',
        'docutils==0.12',
        'Pillow==2.8.2',
        'pyhamcrest==1.8.3',
    ],
    tests_require=[
        'django-setuptest',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    version=versioneer.get_version(),
)

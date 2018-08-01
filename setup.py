# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import versioneer

setup(name='rapid-router',
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'django>=1.8.3, <=1.9.13',
        'django-foundation-icons==3.1',
        'django-bourbon==3.1.8',
        'django-autoconfig >= 0.3.6, < 1.0.0',
        'django-jquery==1.9.1',
        'django-js-reverse==0.6.1',
        'django-foundation-statics==5.4.7',
        'django-pipeline==1.5.4',
        'django-appconf==1.0.1',
        'django-casper==0.0.3',
        'djangorestframework>=3.1.3, <=3.2.3',
        'six==1.11.0',
        'docutils==0.12',
        'pyhamcrest==1.8.3',
    ],
    tests_require=[
        'django-selenium-clean==0.2.1',
        'selenium==3.7.0',
    ],
    test_suite='test_utils.test_suite.DjangoAutoTestSuite',
    version=versioneer.get_version(),
    zip_safe=False,
)

from django_autoconfig.autoconfig import OrderingRelationship

RELATIONSHIPS = [
    OrderingRelationship(
        'INSTALLED_APPS',
        'django_autoconfig.tests.app_relationship',
        before=['django_autoconfig.tests.app1'],
    ),
    OrderingRelationship(
        'INSTALLED_APPS',
        'django_autoconfig.tests.app_relationship',
        before=['django_autoconfig.tests.app3'],
        add_missing=True,
    ),
    OrderingRelationship(
        'INSTALLED_APPS',
        'django_autoconfig.tests.app_relationship',
        before=['django_autoconfig.tests.app4'],
        add_missing=False,
    ),
    OrderingRelationship(
        'INSTALLED_APPS',
        'django_autoconfig.tests.app2',
        after=['django_autoconfig.tests.app3'],
    ),
]

'''Automatic configuration for Django project.'''

import collections
import copy
from django.core.exceptions import ImproperlyConfigured
from django.conf import global_settings
import operator

from .utils import optional_import

class OrderingRelationship(object):
    '''
    This class defines a relationship between an element in a setting
    that's a list and one or more other entries.

    It's intended to be used in an autoconfig.py file like so::

        RELATIONSHIPS = [
            OrderingRelationship(
                'INSTALLED_APPS',
                'my.app',
                before = [
                    'django.contrib.admin',
                ],
                after = [
                ],
            )
        ]
    '''

    def __init__(
        self,
        setting_name,
        setting_value,
        before=None,
        after=None,
        add_missing=True
    ):
        self.setting_name = setting_name
        self.setting_value = setting_value
        self.before = before or []
        self.after = after or []
        self.add_missing = add_missing

    def apply_changes(self, settings):
        changes = 0

        if self.add_missing:
            for item in [self.setting_value] + self.before + self.after:
                if item not in settings[self.setting_name]:
                    settings[self.setting_name] = list(settings[self.setting_name]) + [item]
                    changes += 1
        elif self.setting_value not in settings[self.setting_name]:
            return changes

        for test, related_items in (
            (operator.gt, self.before),
            (operator.lt, self.after),
        ):
            current_value = settings[self.setting_name]

            for item in related_items:
                if item not in current_value:
                    continue
                if test(
                    current_value.index(self.setting_value),
                    current_value.index(item),
                ):
                    location = current_value.index(item)
                    current_value.remove(self.setting_value)
                    current_value.insert(location, self.setting_value)
                    settings[self.setting_name] = current_value
                    changes += 1

        return changes

def merge_dictionaries(current, new, only_defaults=False):
    '''
    Merge two settings dictionaries, recording how many changes were needed.

    '''
    changes = 0
    for key, value in new.items():
        if key not in current:
            if hasattr(global_settings, key):
                current[key] = getattr(global_settings, key)
            else:
                current[key] = copy.deepcopy(value)
                changes += 1
                continue
        elif only_defaults:
            continue
        current_value = current[key]
        if hasattr(current_value, 'items'):
            changes += merge_dictionaries(current_value, value)
        elif isinstance(current_value, collections.Sequence):
            for element in value:
                if element not in current_value:
                    current[key] = list(current_value) + [element]
                    changes += 1
        else:
            # If we don't know what to do with it, replace it.
            if current_value != value:
                current[key] = value
                changes += 1
    return changes

def configure_settings(settings):
    '''
    Given a settings object, run automatic configuration of all
    the apps in INSTALLED_APPS.
    '''
    changes = 0
    old_changes = None
    num_apps = 0
    old_num_apps = len(settings['INSTALLED_APPS'])

    while changes or old_changes is None:
        changes = 0
        for app_name in settings['INSTALLED_APPS']:
            module = optional_import("%s.autoconfig" % (app_name,))
            if not module:
                continue
            changes += merge_dictionaries(
                settings,
                getattr(module, 'SETTINGS', {}),
            )
            changes += merge_dictionaries(
                settings,
                getattr(module, 'DEFAULT_SETTINGS', {}),
                only_defaults=True,
            )
            for relationship in getattr(module, 'RELATIONSHIPS', []):
                changes += relationship.apply_changes(settings)
        num_apps = len(settings['INSTALLED_APPS'])

        if (
            old_changes is not None and
            changes >= old_changes and
            num_apps == old_num_apps
        ):
            raise ImproperlyConfigured(
                'Autoconfiguration could not reach a consistent state'
            )
        old_changes = changes
        old_num_apps = num_apps

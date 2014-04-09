'''Utilities for autoconfig.'''
import imp
import importlib

def optional_import(package_name):
    '''
        Find the package given, or return None if it doesn't exist.
        e.g.
            Given package_name == 'a.b.c'
            If a.b doesn't exist, raise ImportError
            If a.b.c exists, return it
            If a.b.c doesn't exist, return None
    '''

    if '.' in package_name:
        parent_package_name, subpackage_name = package_name.rsplit('.', 1)
        parent_package = importlib.import_module(parent_package_name)
        parent_package_path = parent_package.__path__
    else:
        parent_package_path = None
        subpackage_name = package_name

    try:
        imp.find_module(subpackage_name, parent_package_path)
    except ImportError:
        return None

    return importlib.import_module(package_name)

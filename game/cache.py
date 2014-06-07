from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from models import Level

ALL_LEVELS_KEY = "model_all_levels"
MAX_LEVEL_KEY = "model_max_level"
LEVEL_PREFIX = "model_level"


def all_levels():
    return Level.objects.filter(default=True).order_by('id')


def max_level():
    return Level.objects.filter(default=True).latest('id').id


def get_level(level):
    return get_object_or_404(Level, id=level)


@receiver(post_save, sender=Level)
@receiver(post_delete, sender=Level)
def clear_level_cache(sender, **kwargs):
    for level in all_levels():
        cache.delete(LEVEL_PREFIX + str(level.id))
    cache.delete(ALL_LEVELS_KEY)
    cache.delete(MAX_LEVEL_KEY)


def cache_or_func(key, func):
    result = cache.get(key)
    if result is None:
        result = func()
        cache.set(key, result)
    return result


def cached_all_levels():
    return cache_or_func(ALL_LEVELS_KEY, all_levels)


def cached_max_level():
    return cache_or_func(MAX_LEVEL_KEY, max_level)


def cached_level(level):
    key = LEVEL_PREFIX + level
    func = lambda: get_level(level)
    return cache_or_func(key, func)

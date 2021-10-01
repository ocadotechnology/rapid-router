from __future__ import absolute_import
from builtins import str
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from .models import Level, Episode, LevelDecor, LevelBlock
from . import level_management


LEVEL_PREFIX = "model_level"
EPISODE_PREFIX = "model_episode"
LEVEL_DECOR_PREFIX = "level_decor"
LEVEL_BLOCKS_PREFIX = "level_blocks"


def get_level(level):
    return get_object_or_404(Level, name=level, default=True)


def get_custom_level(level):
    return get_object_or_404(Level, id=level)


def get_episode(episode):
    return get_object_or_404(Episode, id=episode)


@receiver(post_save, sender=Level)
@receiver(post_delete, sender=Level)
def clear_level_cache(sender, instance, **kwargs):
    cache.delete(LEVEL_PREFIX + str(instance.id))


@receiver(post_save, sender=LevelDecor)
@receiver(post_delete, sender=LevelDecor)
def clear_level_decor_cache(sender, instance, **kwargs):
    cache.delete(LEVEL_DECOR_PREFIX + str(instance.level.id))


@receiver(post_save, sender=LevelBlock)
@receiver(post_delete, sender=LevelBlock)
def clear_level_blocks_cache(sender, instance, **kwargs):
    cache.delete(LEVEL_BLOCKS_PREFIX + str(instance.level.id))


def cache_or_func(key, func):
    result = cache.get(key)
    if result is None:
        result = func()
        cache.set(key, result)
    return result


def cached_default_level(name):
    key = LEVEL_PREFIX + str(name)
    func = lambda: get_level(name)
    return cache_or_func(key, func)


def cached_custom_level(level_id):
    key = LEVEL_PREFIX + str(level_id)
    func = lambda: get_custom_level(level_id)
    return cache_or_func(key, func)


def cached_episode(episode):
    key = EPISODE_PREFIX + episode
    func = lambda: get_episode(episode)
    return cache_or_func(key, func)


def cached_level_decor(level):
    key = LEVEL_DECOR_PREFIX + str(level.id)
    func = lambda: level_management.get_decor(level)
    return cache_or_func(key, func)


def cached_level_blocks(level):
    key = LEVEL_BLOCKS_PREFIX + str(level.id)
    func = lambda: level_management.get_blocks(level)
    return cache_or_func(key, func)

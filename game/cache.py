from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from models import Level, Episode

LEVEL_PREFIX = "model_level"
EPISODE_PREFIX = "model_episode"


def get_level(level):
    return get_object_or_404(Level, id=level)


def get_episode(episode):
    return get_object_or_404(Episode, id=episode)


@receiver(post_save, sender=Level)
@receiver(post_delete, sender=Level)
def clear_level_cache(sender, instance, **kwargs):
    cache.delete(LEVEL_PREFIX + str(instance.id))


def cache_or_func(key, func):
    result = cache.get(key)
    if result is None:
        result = func()
        cache.set(key, result)
    return result


def cached_level(level):
    key = LEVEL_PREFIX + str(level)
    func = lambda: get_level(level)
    return cache_or_func(key, func)


def cached_episode(episode):
    key = EPISODE_PREFIX + episode
    func = lambda: get_episode(episode)
    return cache_or_func(key, func)

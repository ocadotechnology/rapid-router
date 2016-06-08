# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from models import Level, Episode, LevelDecor, LevelBlock
import level_management


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

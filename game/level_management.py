import re
import permissions
import json

from django.forms.models import model_to_dict

from models import Level, Block, LevelBlock, LevelDecor, Decor, Theme, Character


##########
# Levels #
##########

def get_list_of_loadable_levels(user):
    loadable_levels = [level for level in Level.objects.all() if permissions.can_load_level(user, level)]
    owned_levels = [level for level in loadable_levels if level.owner == user.userprofile]
    shared_levels = [level for level in loadable_levels if level.owner != user.userprofile]
    return owned_levels, shared_levels

def get_decor(level):
    """ Helper method parsing decor into a dictionary format 'sendable' to javascript. """
    decorData = []
    for ld in LevelDecor.objects.filter(level=level):
        decor = Decor.objects.get(name=ld.decorName, theme=level.theme)
        decorData.append({
            'x': int(ld.x),
            'y': int(ld.y),
            'decorName': str(ld.decorName),
            'width': int(decor.width),
            'height': int(decor.height),
            'url': str(decor.url),
        })

    return decorData

def set_decor(level, decor):
    """ Helper method creating LevelDecor objects given a list of decor in dictionary form."""
    existingDecor = LevelDecor.objects.filter(level=level).delete()

    for data in decor:
        levelDecor = LevelDecor(
            level=level,
            x=data['x'],
            y=data['y'],
            decorName=data['decorName'],
        )
        levelDecor.save()

def get_blocks(level):
    """ Helper method parsing blocks into a dictionary format 'sendable' to javascript. """
    levelBlocks = LevelBlock.objects.filter(level=level).order_by('type')
    return [{'type':lb.type.type, 'number':lb.number} for lb in levelBlocks]

def set_blocks(level, blocks):
    """ Helper method creating LevelBlock objects given a list of blocks in dictionary form."""
    existingBlocks = LevelBlock.objects.filter(level=level).delete()

    for data in blocks:
        levelBlock = LevelBlock(
            level=level, 
            type=Block.objects.get(type=data['type']), 
            number=data['number'] if 'number' in data else None,
        )
        levelBlock.save()

def save_level(level, data):
    level.name = data['name']
    level.path = data['path']
    level.origin = data['origin']
    level.destinations = data['destinations']
    level.max_fuel = data['max_fuel']
    level.traffic_lights = data['traffic_lights']
    level.blocklyEnabled = data['blocklyEnabled']
    level.pythonEnabled = data['pythonEnabled']
    level.theme = Theme.objects.get(id=data['theme'])
    level.character = Character.objects.get(name=data['character_name'])
    level.save()
    
    set_decor(level, data['decor'])
    set_blocks(level, data['blocks'])


def delete_level(level):
    level.delete()


def share_level(level, user):
    level.shared_with.add(user)


def unshare_level(level, user):
    level.shared_with.remove(user)

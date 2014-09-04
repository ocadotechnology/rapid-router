import re
import permissions

from models import Level, Block, LevelBlock, LevelDecor, Decor, Theme, Character


##########
# Levels #
##########

def get_list_of_loadable_levels(user):
    loadable_levels = [level for level in Level.objects.all() if permissions.can_load_level(user, level)]
    owned_levels = [level for level in loadable_levels if level.owner == user.userprofile]
    shared_levels = [level for level in loadable_levels if level.owner != user.userprofile]
    return owned_levels, shared_levels


def set_level_decor(level, decorString, regex):
    """ Helper method creating LevelDecor objects given a string of all decors."""

    regex = re.compile(regex)
    items = regex.findall(decorString)

    level.decor = decorString
    
    existingDecor = LevelDecor.objects.filter(level=level)
    for levelDecor in existingDecor:
        levelDecor.delete()

    if len(items) > 0 and len(items[0]) > 1 and 'x' in items[0][1]:
        xIndex = 2
        yIndex = 4
    else:
        xIndex = 4
        yIndex = 2

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y" *: *)([0-9]+)(}, *"name" *: *")([a-zA-Z0-9]+)(", *"height" *:)([0-9]+)( *}))')
    items = regex.findall(decorString)

    for item in items:
        name = item[6]
        levelDecor = LevelDecor(level=level, x=item[xIndex], y=item[yIndex], decorName=name)
        levelDecor.save()


def save_level(level, data):
    theme = Theme.objects.get(id=data['theme_id'])
    character = Character.objects.get(name=data['character_name'])

    level.name = data['name']
    level.path = data['path']
    level.origin = data['origin']
    level.destinations = data['destinations']
    level.max_fuel = data['max_fuel']
    level.traffic_lights = data['traffic_lights']
    level.blocklyEnabled = data['blocklyEnabled']
    level.pythonEnabled = data['pythonEnabled']
    level.theme = theme
    level.character = character
    level.save()

    regex = ('(({"coordinate" *:{"x": *)([0-9]+)(,"y" *: *)([0-9]+)(}, *"name" *: *")' +
             '([a-zA-Z0-9]+)(", *"height" *:)([0-9]+)( *}))')
    set_level_decor(level, data['decor'], regex)

    for blockType in data['blockTypes']:
        levelBlock = LevelBlock(level=level, type=Block.objects.get(type=blockType), number=None)
        levelBlock.save()

    level.save()


def delete_level(level):
    level.delete()


def share_level(level, user):
    level.shared_with.add(user)


def unshare_level(level, user):
    level.shared_with.remove(user)

import re
import permissions

from models import Level, Block, LevelDecor, Decor, Theme, Character

##########
# Levels #
##########

def get_list_of_loadable_levels(user):
    loadable_levels = [level for level in Level.objects.all() if permissions.can_load_level(user, level)]
    owned_levels  = [level for level in loadable_levels if level.owner == user.userprofile]
    shared_levels = [level for level in loadable_levels if level.owner != user.userprofile]
    return owned_levels, shared_levels

def save_level(level, data):

    def set_level_decor(level, decorString):
        """ Helper method creating LevelDecor objects given a string of all decors."""

        regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"name": *")([a-zA-Z0-9]+)("}))')
        items = regex.findall(decorString)

        existingDecor = LevelDecor.objects.filter(level=level)
        for levelDecor in existingDecor:
            levelDecor.delete()

        for item in items:
            name = item[6]
            levelDecor = LevelDecor(level=level, x=item[2], y=item[4], decorName=name)
            levelDecor.save()

    theme = Theme.objects.get(id=data['theme_id'])
    character = Character.objects.get(name=data['character_name'])

    level.name = data['name']
    level.path = data['path']
    level.origin = data['origin']
    level.destinations = data['destinations']
    level.max_fuel = data['max_fuel']
    level.traffic_lights = data['traffic_lights']
    level.save()

    set_level_decor(level, data['decor'])

    level.blocks = Block.objects.filter(type__in=data['blockTypes'])
    level.save()

def delete_level(level):
    level.delete()

def share_level(level, user):
    level.shared_with.add(user)

def unshare_level(level, user):
    level.shared_with.remove(user)



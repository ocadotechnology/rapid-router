import permissions

from models import Block, LevelBlock, LevelDecor, Decor, Theme, Character


##########
# Levels #
##########

def get_loadable_levels(user):
    if user.is_anonymous():
        return [], []

    owned_levels = user.userprofile.levels.iterator()
    shared_levels = (level for level in user.shared.iterator() if permissions.can_load_level(user, level))
    return owned_levels, shared_levels


def get_decor(level):
    """ Helper method parsing decor into a dictionary format 'sendable' to javascript. """
    decorData = []
    for ld in LevelDecor.objects.filter(level=level):
        decor = Decor.objects.get(name=ld.decorName, theme=level.theme)
        decorData.append({
            'x': int(ld.x),
            'y': int(ld.y),
            'z': int(decor.z_index),
            'decorName': str(ld.decorName),
            'width': int(decor.width),
            'height': int(decor.height),
            'url': str(decor.url),
        })

    return decorData

def set_decor(level, decor):
    set_decor_inner(level, decor, LevelDecor)

def set_decor_inner(level, decor, LevelDecor):
    """ Helper method creating LevelDecor objects given a list of decor in dictionary form."""
    LevelDecor.objects.filter(level=level).delete()

    level_decors = []
    for data in decor:
        level_decors.append(LevelDecor(
            level_id=level.id,
            x=data['x'],
            y=data['y'],
            decorName=data['decorName']
        ))
    LevelDecor.objects.bulk_create(level_decors)


def get_blocks(level):
    """ Helper method parsing blocks into a dictionary format 'sendable' to javascript. """
    levelBlocks = LevelBlock.objects.filter(level=level).order_by('type')
    return [{'type': lb.type.type, 'number': lb.number} for lb in levelBlocks]

def set_blocks(level, blocks):
    set_blocks_inner(level, blocks, LevelBlock, Block)

def set_blocks_inner(level, blocks, LevelBlock, Block):
    """ Helper method creating LevelBlock objects given a list of blocks in dictionary form."""
    LevelBlock.objects.filter(level=level).delete()

    level_blocks = []
    for data in blocks:
        level_blocks.append(LevelBlock(
            level_id=level.id,
            type=Block.objects.get(type=data['type']),
            number=data['number'] if 'number' in data else None
        ))
    LevelBlock.objects.bulk_create(level_blocks)


def save_level(level, data):
    level.name = data['name']
    level.path = data['path']
    level.origin = data['origin']
    level.destinations = data['destinations']
    level.max_fuel = data['max_fuel']
    level.traffic_lights = data['traffic_lights']
    level.blocklyEnabled = data.get('blocklyEnabled', True)
    level.pythonEnabled = data.get('pythonEnabled', False)
    level.pythonViewEnabled = data.get('pythonViewEnabled', False)
    level.theme = Theme.objects.get(id=data['theme'])
    level.character = Character.objects.get(id=data['character'])
    level.save()

    set_decor(level, data['decor'])
    set_blocks(level, data['blocks'])


def delete_level(level):
    level.delete()


def share_level(level, *users):
    level.shared_with.add(*users)


def unshare_level(level, *users):
    level.shared_with.remove(*users)

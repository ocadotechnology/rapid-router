# Code for Life
#
# Copyright (C) 2015, Ocado Limited
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

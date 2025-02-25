from __future__ import absolute_import

from builtins import str
from itertools import chain

from common.mail import campaign_ids, send_dotdigital_email

from game.character import get_character_by_pk
from game.decor import get_decor_element
from game.theme import get_theme_by_pk
from .models import Block, LevelBlock, LevelDecor


##########
# Levels #
##########


def get_loadable_levels(user):
    levels_owned_by_user = levels_owned_by(user)
    shared_levels = levels_shared_with(user)

    return levels_owned_by_user, shared_levels


def add_related_fields(levels):
    """Add related fields and filter to active users only"""
    return levels.select_related(
        "owner__user", "owner__teacher", "owner__student"
    ).filter(owner__user__is_active=True)


def levels_shared_with(user):
    if user.is_anonymous:
        return []

    shared_levels = user.shared
    shared_levels = add_related_fields(shared_levels)

    if hasattr(user.userprofile, "student"):
        shared_levels = shared_levels.filter(needs_approval=False)

    return shared_levels


def levels_owned_by(user):
    if user.is_anonymous:
        return []

    levels = user.userprofile.levels

    return add_related_fields(levels)


def get_decor(level):
    """Helper method parsing decor into a dictionary format 'sendable' to javascript."""
    decorData = []
    for ld in LevelDecor.objects.filter(level=level):
        decor = get_decor_element(name=ld.decor_name, theme=level.theme)
        decorData.append(
            {
                "x": int(ld.x),
                "y": int(ld.y),
                "z": int(decor.z_index),
                "decorName": str(ld.decor_name),
                "width": int(decor.width),
                "height": int(decor.height),
                "url": str(decor.url),
                "xmas_url": str(decor.xmas_url),
            }
        )

    return decorData


def set_decor(level, decor):
    set_decor_inner(level, decor, LevelDecor)


def set_decor_inner(level, decor, LevelDecor):
    """Helper method creating LevelDecor objects given a list of decor in dictionary form."""
    LevelDecor.objects.filter(level=level).delete()

    level_decors = []
    for data in decor:
        level_decors.append(
            LevelDecor(
                level_id=level.id,
                x=data["x"],
                y=data["y"],
                decor_name=data["decorName"],
            )
        )
    LevelDecor.objects.bulk_create(level_decors)


def get_night_blocks(level):
    """Helper method parsing blocks into a dictionary format 'sendable' to javascript."""
    coreBlockTypes = [
        "move_forwards",
        "turn_left",
        "turn_right",
        "turn_around",
        "controls_repeat",
        "controls_repeat_until",
        "controls_if",
        "at_destination",
        "road_exists",
        "dead_end",
    ]
    coreNightBlocks = Block.objects.filter(type__in=coreBlockTypes)
    coreNightLevelBlocks = [
        LevelBlock(level=level, type=block) for block in coreNightBlocks
    ]
    existingLevelBlocks = LevelBlock.objects.filter(level=level)
    remainingBlocks = existingLevelBlocks.exclude(
        type__type__in=coreBlockTypes
    ).order_by("type")
    levelBlocks = sorted(
        list(chain(coreNightLevelBlocks, remainingBlocks)),
        key=lambda levelBlock: levelBlock.type.id,
    )

    return [{"type": lb.type.type, "number": lb.number} for lb in levelBlocks]


def get_blocks(level):
    """Helper method parsing blocks into a dictionary format 'sendable' to javascript."""
    levelBlocks = LevelBlock.objects.filter(level=level).order_by("type")
    return [{"type": lb.type.type, "number": lb.number} for lb in levelBlocks]


def set_blocks(level, blocks):
    set_blocks_inner(level, blocks, LevelBlock, Block)


def set_blocks_inner(level, blocks, LevelBlock, Block):
    """Helper method creating LevelBlock objects given a list of blocks in dictionary form."""
    LevelBlock.objects.filter(level=level).delete()

    level_blocks = []
    dictionary = blocks_dictionary(blocks, Block)

    for data in blocks:
        level_blocks.append(
            LevelBlock(
                level_id=level.id,
                type=dictionary[data["type"]],
                number=data["number"] if "number" in data else None,
            )
        )
    LevelBlock.objects.bulk_create(level_blocks)


def blocks_dictionary(blocks, Block):
    types = [data["type"] for data in blocks]
    block_objects = Block.objects.filter(type__in=types)
    result = {block.type: block for block in block_objects}
    return result


def save_level(level, data):
    level.name = data["name"]
    level.path = data["path"]
    level.origin = data["origin"]
    level.destinations = data["destinations"]
    level.max_fuel = data["max_fuel"]
    level.traffic_lights = data["traffic_lights"]
    level.cows = data["cows"]
    level.blockly_enabled = data.get("blockly_enabled", True)
    level.python_enabled = data.get("python_enabled", False)
    level.python_view_enabled = data.get("python_view_enabled", False)
    level.theme = get_theme_by_pk(pk=data["theme"])
    level.character = get_character_by_pk(pk=data["character"])
    level.disable_algorithm_score = data.get("disable_algorithm_score", False)
    if data.get("subtitle") != None:
        level.subtitle = data.get("subtitle")
    if data.get("lesson") != None:
        level.lesson = data.get("lesson")
    if data.get("hint") != None:
        level.hint = data.get("hint")

    level.save()

    set_decor(level, data["decor"])
    set_blocks(level, data["blocks"])


def delete_level(level):
    level.delete()


def share_level(level, *users):
    level.shared_with.add(*users)


def unshare_level(level, *users):
    level.shared_with.remove(*users)


def email_new_custom_level(
    teacher_email, moderate_url, level_url, student_name, class_name
):
    # email teacher when a new custom level is created by a pupil, so it can be moderated

    send_dotdigital_email(
        campaign_ids["level_creation"],
        [teacher_email],
        personalization_values={
            "STUDENT_NAME": student_name,
            "CLASS_NAME": class_name,
            "LEVEL_URL": level_url,
            "MODERATE_URL": moderate_url,
        },
    )

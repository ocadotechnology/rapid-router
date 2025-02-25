import game.level_management as level_management
from game.models import Level


multiple_house_data = {
    "origin": '{"coordinate":[3,5],"direction":"S"}',
    "python_enabled": False,
    "decor": [],
    "blockly_enabled": True,
    "blocks": [
        {"type": "move_forwards"},
        {"type": "turn_left"},
        {"type": "turn_right"},
    ],
    "max_fuel": "50",
    "python_view_enabled": False,
    "character": "3",
    "name": "2",
    "theme": 1,
    "anonymous": False,
    "cows": "[]",
    "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0,2]}, {"coordinate": [3,3], "connectedNodes":[1]}]',
    "traffic_lights": "[]",
    "destinations": "[[3,4], [3,3]]",
}


def create_save_level(teacher_or_student, level_name="1", shared_with=None):
    data = {
        "origin": '{"coordinate":[3,5],"direction":"S"}',
        "python_enabled": False,
        "decor": [],
        "blockly_enabled": True,
        "blocks": [
            {"type": "move_forwards"},
            {"type": "turn_left"},
            {"type": "turn_right"},
        ],
        "max_fuel": "50",
        "python_view_enabled": False,
        "character": "3",
        "name": level_name,
        "theme": 1,
        "anonymous": False,
        "cows": "[]",
        "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0]}]',
        "traffic_lights": "[]",
        "destinations": "[[3,4]]",
    }
    level = Level(default=False, anonymous=data["anonymous"])
    level.owner = teacher_or_student.user
    level_management.save_level(level, data)

    if hasattr(level.owner, "teacher"):
        level.needs_approval = False

    level.save()

    if shared_with is not None:
        for user in shared_with:
            level.shared_with.add(user)
        level.save()

    return level

def create_save_level_with_multiple_houses(teacher_or_student, level_name="2", shared_with=None):
    level = Level(default=False, anonymous=multiple_house_data["anonymous"])
    level.owner = teacher_or_student.user
    level_management.save_level(level, multiple_house_data)
    level.save()

    if shared_with is not None:
        for user in shared_with:
            level.shared_with.add(user)
        level.save()

    return level

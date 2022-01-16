import game.level_management as level_management
from game.models import Level


def create_save_level(teacher_or_student, level_name="1", shared_with=None):
    data = {
        "origin": '{"coordinate":[3,5],"direction":"S"}',
        "pythonEnabled": False,
        "decor": [],
        "blocklyEnabled": True,
        "blocks": [
            {"type": "move_forwards"},
            {"type": "turn_left"},
            {"type": "turn_right"},
        ],
        "max_fuel": "50",
        "pythonViewEnabled": False,
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
    level.save()

    if shared_with is not None:
        for user in shared_with:
            level.shared_with.add(user)
        level.save()

    return level.id

import game.level_management as level_management
from game.models import Level


def create_save_level(teacher):
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
        "name": "1",
        "theme": 1,
        "anonymous": False,
        "cows": "[]",
        "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0]}]',
        "traffic_lights": "[]",
        "destinations": "[[3,4]]",
    }
    level = Level(default=False, anonymous=data["anonymous"])
    level.owner = teacher.user.user.userprofile
    level_management.save_level(level, data)
    level.save()

    return level.id

from collections import defaultdict
import json
import random
import math
from models import Level, Block


def create():
    generated_path = generate_random_path()
    level = Level(name=3000, path=generated_path, maxFuel=30)
    level.save()
    level.blocks = Block.objects.all()
    level.save()
    return level

def calculate_node_angle(node1, node2):
    return math.atan2(node2[1] - node1[1], node2[0] - node1[0])

def generate_random_path():
    nodes = [(0, 3)]
    connections = defaultdict(list)

    for _ in xrange(20):
        (old_tile, new_tile) = pick_adjacent_tile(nodes)
        if new_tile:
            nodes.append(new_tile)
            old_index = nodes.index(old_tile)
            new_index = len(nodes) - 1
            connections[old_index].append((new_index, new_tile))
            connections[new_index].append((old_index, old_tile))

    result = []
    for index, node in enumerate(nodes):
        result.append({
            'coordinate': node,
            'connectedNodes': [c[0] for c in sorted(connections[index],
                                                    key=lambda conn: calculate_node_angle(node, conn[1]),
                                                    reverse=True)]
        })

    return json.dumps(result)


def pick_adjacent_tile(tiles):
    for attempts in xrange(5):
        origin = random.choice(tiles)
        possibles = []
        if is_possible((origin[0] - 1, origin[1]), tiles):
            possibles.append((origin[0] - 1, origin[1]))
        if is_possible((origin[0] + 1, origin[1]), tiles):
            possibles.append((origin[0] + 1, origin[1]))
        if is_possible((origin[0], origin[1] - 1), tiles):
            possibles.append((origin[0], origin[1] - 1))
        if is_possible((origin[0], origin[1] + 1), tiles):
            possibles.append((origin[0], origin[1] + 1))

        if possibles:
            return origin, random.choice(possibles)

    return None, None


def is_possible(tile, tiles):
    return (tile not in tiles) and 0 < tile[0] < 10 - 1 and 0 < tile[1] < 8 - 1
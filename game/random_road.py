from collections import defaultdict
import json
import random
import math
from models import Level, Block


def create():
    path = generate_random_path((0, 3), 20, 0.8, 0.0)
    destination = json.dumps(path[-1]['coordinate'])
    level = Level(name=3000, path=json.dumps(path), max_fuel=30, destination=destination)
    level.save()
    level.blocks = Block.objects.all()
    level.save()
    return level


def calculate_node_angle(node1, node2):
    return math.atan2(node2[1] - node1[1], node2[0] - node1[0])


def generate_random_path(start_position, num_road_tiles, straightness_factor, loopiness_factor):
    nodes = [start_position]
    connections = defaultdict(list)

    for _ in xrange(num_road_tiles):
        (previous_node, new_node) = pick_adjacent_node(nodes, straightness_factor)
        if not new_node:
            continue

        nodes.append(new_node)
        connections = add_new_connections(nodes, connections, new_node, previous_node)

    connections = join_up_loops(nodes, connections, loopiness_factor)
    result = []
    for index, node in enumerate(nodes):
        result.append({
            'coordinate': node,
            'connectedNodes': [c[0] for c in sorted(connections[index], # O Noes! This doesn't work with loops!
                                                    key=lambda conn: calculate_node_angle(node, conn[1]),
                                                    reverse=True)]
        })

    return result


def pick_adjacent_node(nodes, straightness_factor):
    for attempts in xrange(5):
        origin = pick_origin_node(nodes, straightness_factor)
        possibles = []
        if is_possible((origin[0] - 1, origin[1]), nodes):
            possibles.append((origin[0] - 1, origin[1]))
        if is_possible((origin[0] + 1, origin[1]), nodes):
            possibles.append((origin[0] + 1, origin[1]))
        if is_possible((origin[0], origin[1] - 1), nodes):
            possibles.append((origin[0], origin[1] - 1))
        if is_possible((origin[0], origin[1] + 1), nodes):
            possibles.append((origin[0], origin[1] + 1))

        if possibles:
            return origin, random.choice(possibles)

    return None, None


def pick_origin_node(nodes, straightness_factor):
    if random.random() > straightness_factor:
        return random.choice(nodes)
    else:
        return nodes[-1]


def join_up_loops(nodes, connections, loopiness_factor):
    for node in nodes:
        for adjacent_node in nodes:  # TODO: This can _surely_ be improved!
            if adjacent_node == node or not are_adjacent(node, adjacent_node):
                continue

            if random.random() < loopiness_factor:
                connections = add_new_connections(nodes, connections, node, adjacent_node)

    return connections


def are_adjacent(node_1, node_2):
    return node_2 == (node_1[0] - 1, node_1[1]) \
           or node_2 == (node_1[0] + 1, node_1[1]) \
           or node_2 == (node_1[0], node_1[1] - 1) \
           or node_2 == (node_1[0], node_1[1] + 1)


def is_possible(node, nodes):
    return (node not in nodes) and 0 < node[0] < 10 - 1 and 0 < node[1] < 8 - 1


def add_new_connections(nodes, connections, node_1, node_2):
    node_1_index = nodes.index(node_1)
    node_2_index = nodes.index(node_2)
    connections[node_1_index].append((node_2_index, node_1))
    connections[node_2_index].append((node_1_index, node_2))

    return connections

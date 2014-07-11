from collections import defaultdict, namedtuple
from django.shortcuts import render, get_object_or_404
import json
import math
from models import Episode, Level, Block
import random

Node = namedtuple('Node', ['x', 'y'])


def create(episode=None):

    if episode is None:
        path = generate_random_path(Node(0, 3), 20, 0.2, 0.1)
        destination = json.dumps(path[-1]['coordinate'])
        level = Level(name=3000, path=json.dumps(path), max_fuel=30, destination=destination)
        
    else:
        print(episode.__dict__)
        path = generate_random_path(Node(0,3), episode.r_num_tiles,episode.r_branchiness,episode.r_loopiness)
        destination = json.dumps(path[-1]['coordinate'])
        level = Level(name="Random level for " + episode.name + ".", path=json.dumps(path), max_fuel=30, destination=destination)

    level.save()
    level.blocks = Block.objects.all()
    level.save()

    return level


def calculate_node_angle(node_1, node_2):
    return math.atan2(node_2.y - node_1.y, node_2.x - node_1.x)


def generate_random_path(start_position, num_road_tiles, branchiness_factor, loopiness_factor):
    nodes = [start_position]
    connections = defaultdict(list)

    for _ in xrange(num_road_tiles):
        (previous_node, new_node) = pick_adjacent_node(nodes, branchiness_factor)
        if not new_node:
            continue

        nodes.append(new_node)
        connections = add_new_connections(nodes, connections, new_node, previous_node)

    connections = join_up_loops(nodes, connections, loopiness_factor)
    result = []
    for index, node in enumerate(nodes):
        result.append({
            'coordinate': node,
            'connectedNodes': sorted(connections[index],
                                     key=lambda conn: calculate_node_angle(node, nodes[conn]),
                                     reverse=True)
        })

    return result


def pick_adjacent_node(nodes, branchiness_factor):
    for attempts in xrange(5):
        origin = pick_origin_node(nodes, branchiness_factor)
        possibles = []

        x = origin.x
        y = origin.y
        for (delta_x, delta_y) in {(-1, 0), (1, 0), (0, -1), (1, 0)}:  # TODO: Make this set a constant
            node = Node(x + delta_x, y + delta_y)
            if is_possible(node, nodes):
                possibles.append(node)

        if possibles:
            return origin, random.choice(possibles)

    return None, None


def pick_origin_node(nodes, branchiness_factor):
    if random.random() < branchiness_factor:
        return random.choice(nodes)
    else:
        return nodes[-1]


def join_up_loops(nodes, connections, loopiness_factor):
    for node_index, node in enumerate(nodes):
        for adjacent_node_index, adjacent_node in enumerate(nodes):  # TODO: This can _surely_ be improved!
            if adjacent_node == node or not are_adjacent(node, adjacent_node) or adjacent_node_index in connections[node_index]:
                continue

            if random.random() < loopiness_factor:
                connections = add_new_connections(nodes, connections, node, adjacent_node)

    return connections


def are_adjacent(node_1, node_2):
    delta_x = node_2.x - node_1.x
    delta_y = node_2.y - node_1.y
    return (delta_x, delta_y) in {(-1, 0), (1, 0), (0, -1), (1, 0)}


def is_possible(node, nodes):
    return (node not in nodes) and 0 < node.x < 10 - 1 and 0 < node.y < 8 - 1


def add_new_connections(nodes, connections, node_1, node_2):
    node_1_index = nodes.index(node_1)
    node_2_index = nodes.index(node_2)
    connections[node_1_index].append(node_2_index)
    connections[node_2_index].append(node_1_index)

    return connections

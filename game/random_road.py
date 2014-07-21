from collections import defaultdict, namedtuple
from django.shortcuts import render, get_object_or_404
import json
import math
from models import Episode, Level, Block
import random

Node = namedtuple('Node', ['x', 'y'])

DIRECTIONS = {(1, 0), (0, 1), (-1, 0), (0, -1)}
WIDTH = 10
HEIGHT = 8

DEFAULT_START_NODE = Node(0,3)
DEFAULT_NUM_TILES = 20
DEFAULT_BRANCHINESS = 0.3
DEFAULT_LOOPINESS = 0.1
DEFAULT_CURVINESS = 0.5

def create(episode=None):

    if episode is None:
        path = generate_random_path(DEFAULT_START_NODE,
                                    DEFAULT_NUM_TILES, 
                                    DEFAULT_BRANCHINESS,
                                    DEFAULT_LOOPINESS,
                                    DEFAULT_CURVINESS)
        destination = json.dumps(path[-1]['coordinate'])
        level = Level(name="Default random level", 
                                    path=json.dumps(path),
                                    max_fuel=30,
                                    destination=destination,
                                    blocklyEnabled=True,
                                    pythonEnabled=False)
        
    else:
        path = generate_random_path(DEFAULT_START_NODE,
                                    episode.r_num_tiles,
                                    episode.r_branchiness,
                                    episode.r_loopiness,
                                    episode.r_curviness)
        destination = json.dumps(path[-1]['coordinate'])
        level = Level(name="Random level for " + episode.name + ".",
                                    path=json.dumps(path), 
                                    max_fuel=30, 
                                    destination=destination,
                                    blocklyEnabled=episode.r_blocklyEnabled,
                                    pythonEnabled=episode.r_pythonEnabled)

    level.save()
    level.blocks = episode.r_blocks.all()
    level.save()

    return level

def generate_random_path(start_position, num_road_tiles, branchiness_factor, loopiness_factor, curviness_factor):
    nodes = [start_position]
    index_by_node = {start_position:0}

    connections = defaultdict(list)

    for _ in xrange(num_road_tiles):
        (previous_node, new_node) = pick_adjacent_node(nodes, connections, branchiness_factor, curviness_factor)
        if new_node:
            nodes.append(new_node)
            index_by_node[new_node] = len(nodes)-1
            connections = add_new_connections(connections, len(nodes)-1, index_by_node[previous_node])

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

def pick_adjacent_node(nodes, connections, branchiness_factor, curviness_factor):
    
    for attempts in xrange(5):
        origin = pick_origin_node(nodes, branchiness_factor)
        possibles = []

        x = origin.x
        y = origin.y
        for (delta_x, delta_y) in DIRECTIONS:
            node = Node(x + delta_x, y + delta_y)
            if is_possible(node, nodes):
                possibles.append(node)

        if possibles:
            return origin, pick_destination_node(nodes, connections, origin, possibles, curviness_factor)

    return None, None

def pick_origin_node(nodes, branchiness_factor):
    if random.random() < branchiness_factor:
        return random.choice(nodes)
    else:
        return nodes[-1]

def pick_destination_node(nodes, connections, origin, possibles, curviness_factor):
    existing_connections = [nodes[nodeIndex] for nodeIndex in connections[nodes.index(origin)]]
    existing_connection_directions = [(node.x-origin.x,node.y-origin.y) for node in existing_connections]
    linear = [node for node in possibles if (origin.x-node.x,origin.y-node.y) in existing_connection_directions]
    curved = [node for node in possibles if (origin.x-node.x,origin.y-node.y) not in existing_connection_directions]

    if linear and curved:
        if random.random() < curviness_factor:
            pick_from = curved
        else:
            pick_from = linear
    else:
        pick_from = possibles

    return random.choice(pick_from)


def join_up_loops(nodes, connections, loopiness_factor):
    nodes_by_location = {(node.x,node.y):(index,node) for index, node in enumerate(nodes)}

    for node_index, node in enumerate(nodes):
        for location in get_neighbouring_locations(node):
            if location in nodes_by_location:
                adjacent_node_index, adjacent_node = nodes_by_location[location]
                if adjacent_node_index not in connections[node_index] and random.random() < loopiness_factor:
                    connections = add_new_connections(connections, node_index, adjacent_node_index)
    return connections

def add_new_connections(connections, node_1_index, node_2_index):
    connections[node_1_index].append(node_2_index)
    connections[node_2_index].append(node_1_index)

    return connections


def are_adjacent(node_1, node_2):
    delta_x = node_2.x - node_1.x
    delta_y = node_2.y - node_1.y
    return (delta_x, delta_y) in DIRECTIONS

def calculate_node_angle(node_1, node_2):
    return math.atan2(node_2.y - node_1.y, node_2.x - node_1.x)

def is_possible(node, nodes):
    return (node not in nodes) and 0 < node.x < WIDTH - 1 and 0 < node.y < HEIGHT - 1

def get_neighbouring_locations(node):
    squares = []
    for delta_x, delta_y in DIRECTIONS:
        new_x = node.x + delta_x
        new_y = node.y + delta_y

        if new_x >= 0 and new_x < WIDTH and new_y >= 0 and new_y < HEIGHT:
            squares.append((new_x,new_y))
    return squares
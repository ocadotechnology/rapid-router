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

DEFAULT_MAX_FUEL = 30
DEFAULT_START_NODE = Node(0, 3)
DEFAULT_NUM_TILES = 20
DEFAULT_BRANCHINESS = 0.3
DEFAULT_LOOPINESS = 0.1
DEFAULT_CURVINESS = 0.5

PERCENTAGE_OF_JUNCTIONS_WITH_TRAFFIC_LIGHTS = 30


def create(episode=None):
    maxFuel = DEFAULT_MAX_FUEL

    if not episode:
        num_tiles = DEFAULT_NUM_TILES
        branchiness = DEFAULT_BRANCHINESS
        loopiness = DEFAULT_LOOPINESS
        curviness = DEFAULT_CURVINESS
        blockly_enabled = True
        python_enabled = False
        blocks = Block.objects.all()
        name = "Default random level"
        traffic_lights_enabled = True
    else:
        num_tiles = episode.r_num_tiles
        branchiness = episode.r_branchiness
        loopiness = episode.r_loopiness
        curviness = episode.r_curviness
        blockly_enabled = episode.r_blocklyEnabled
        python_enabled = episode.r_pythonEnabled
        blocks = episode.r_blocks.all()
        name = "Random level for " + episode.name
        traffic_lights_enabled = episode.r_trafficLights

    level_data = generate_random_map_data(num_tiles,
                                          branchiness,
                                          loopiness,
                                          curviness,
                                          traffic_lights_enabled)

    level = Level(name=name,
                  path=level_data['path'],
                  destinations=level_data['destinations'],
                  traffic_lights=level_data['traffic_lights'],
                  max_fuel=maxFuel,
                  anonymous=True,
                  origin=level_data['origin'],
                  blocklyEnabled=blockly_enabled,
                  pythonEnabled=python_enabled)

    level.save()
    level.blocks = blocks
    level.save()

    return level


def generate_random_map_data(num_tiles, branchiness, loopiness, curviness, traffic_lights_enabled):
    path = generate_random_path(num_tiles, branchiness, loopiness, curviness)
    traffic_lights = generate_traffic_lights(path) if traffic_lights_enabled else []
    destinations = [[path[-1]['coordinate'].x, path[-1]['coordinate'].y]]
    origin = get_origin(path)

    return {'path': json.dumps(path), 'traffic_lights': json.dumps(traffic_lights),
            'origin': json.dumps(origin), 'destinations': json.dumps(destinations)}


def generate_random_path(num_road_tiles, branchiness_factor, loopiness_factor, curviness_factor):

    def pick_adjacent_node(nodes, connections, branchiness_factor, curviness_factor):
        for attempts in xrange(5):
            origin = pick_origin_node(nodes, connections, branchiness_factor)
            possibles = []

            x = origin.x
            y = origin.y
            for (delta_x, delta_y) in DIRECTIONS:
                node = Node(x + delta_x, y + delta_y)
                if is_possible(node, nodes):
                    possibles.append(node)

            if possibles:
                return origin, pick_destination_node(nodes, connections, origin, possibles,
                                                     curviness_factor)

        return None, None

    def pick_origin_node(nodes, connections, branchiness_factor):
        if random.random() < branchiness_factor and len(connections[0]) > 0:
            return random.choice(nodes[1:])
        else:
            return nodes[-1]

    def pick_destination_node(nodes, connections, origin, possibles, curviness_factor):
        existing_connections = [nodes[nodeIndex] for nodeIndex in connections[nodes.index(origin)]]
        existing_connection_directions = [(node.x - origin.x, node.y - origin.y)
                                          for node in existing_connections]
        linear = [node for node in possibles if (origin.x - node.x, origin.y - node.y)
                  in existing_connection_directions]
        curved = [node for node in possibles if (origin.x - node.x, origin.y - node.y)
                  not in existing_connection_directions]

        if linear and curved:
            if random.random() < curviness_factor:
                pick_from = curved
            else:
                pick_from = linear
        else:
            pick_from = possibles

        return random.choice(pick_from)

    def join_up_loops(nodes, connections, loopiness_factor):
        nodes_by_location = {(node.x, node.y): (index, node) for index, node in enumerate(nodes)}
        n = len(nodes)

        # Floyd-Warshall algorithm to find distances between all nodes
        distances = []
        for origin in range(n):
            row = []
            for destination in range(n):
                if origin == destination:
                    row.append(0)
                elif destination in connections[origin]:
                    row.append(1)
                else:
                    row.append(float('inf'))
            distances.append(row)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    alternate = distances[i][k] + distances[k][j]
                    if alternate < distances[i][j]:
                        distances[i][j] = alternate

        # Now find possible loops
        possible_loops = []
        for node_index, node in enumerate(nodes):
            if node != nodes[0]:
                for location in get_neighbouring_locations(node):
                    if location in nodes_by_location:
                        adjacent_node_index, adjacent_node = nodes_by_location[location]
                        if adjacent_node_index > node_index and adjacent_node != nodes[0]:
                            if adjacent_node_index not in connections[node_index]:
                                possible_loops.append((node_index, adjacent_node_index))

        if len(possible_loops) == 0:
            return connections
        # Now join up loops (does not dynamically update distances, but still get required effect)
        max_loop_distance = max([distances[s][d] for s, d in possible_loops])
        for origin, destination in possible_loops:
            adjusted_loopiness_factor = loopiness_factor * (0.5 + distances[origin][destination] / max_loop_distance)
            if random.random() < adjusted_loopiness_factor:
                connections = add_new_connections(connections, origin, destination)

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
                squares.append((new_x, new_y))
        return squares

    nodes = [Node(random.randrange(1, WIDTH - 1), random.randrange(1, HEIGHT - 1))]
    index_by_node = {nodes[0]: 0}
    connections = defaultdict(list)

    for _ in xrange(num_road_tiles - 1):
        (previous_node, new_node) = pick_adjacent_node(nodes, connections, branchiness_factor, curviness_factor)
        if new_node:
            nodes.append(new_node)
            index_by_node[new_node] = len(nodes) - 1
            connections = add_new_connections(connections, len(nodes) - 1, index_by_node[previous_node])

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


def get_origin(path):

    node = path[1]
    neighbour = path[0]
    direction = get_direction(node, neighbour)
    return {'coordinate': [neighbour['coordinate'].x, neighbour['coordinate'].y],
            'direction': direction}


def generate_traffic_lights(path):

    degree2Nodes = []
    degree3or4Nodes = []

    for node in path:
        degree = len(node['connectedNodes'])
        if degree == 3 or degree == 4:
            degree3or4Nodes.append(node)
        elif degree == 2:
            degree2Nodes.append(node)

    if len(degree3or4Nodes) > 0:
        candidateNodes = degree3or4Nodes
    else:
        candidateNodes = degree2Nodes

    numberOfJunctions = max(int(len(candidateNodes) * PERCENTAGE_OF_JUNCTIONS_WITH_TRAFFIC_LIGHTS / 100.0), 1)

    random.shuffle(candidateNodes)
    nodesSelected = candidateNodes[:numberOfJunctions]

    trafficLights = []
    for node in nodesSelected:
        nodeIndex = path.index(node)

        controlledNeighbours = []
        for neighbourIndex in node['connectedNodes']:
            neighbour = path[neighbourIndex]
            if neighbour not in nodesSelected:
                controlledNeighbours.append(neighbour)

        counter = 0
        for neighbour in controlledNeighbours:
            neighbourIndex = path.index(neighbour)

            direction = get_direction(node, neighbour)

            trafficLights.append({'sourceCoordinate': {'x': neighbour['coordinate'].x,
                                                       'y': neighbour['coordinate'].y},
                                  'direction': direction,
                                  'startTime': 0 if counter == 0 else 2 * (counter - 1),
                                  'startingState': 'GREEN' if counter == 0 else 'RED',
                                  'greenDuration': 2,
                                  'redDuration': 2 * (len(controlledNeighbours) - 1)})
            counter += 1

    return trafficLights


def get_direction(node, neighbour):
    if neighbour['coordinate'].y < node['coordinate'].y:
        direction = "N"
    elif neighbour['coordinate'].x < node['coordinate'].x:
        direction = "E"
    elif neighbour['coordinate'].y > node['coordinate'].y:
        direction = "S"
    elif neighbour['coordinate'].x > node['coordinate'].x:
        direction = "W"
    return direction

# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
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
from django.core.cache import cache
import json
import math
import random

import level_management

from collections import defaultdict, namedtuple
from models import Level, Block

from game.decor import get_decor_element
from game.theme import get_theme


Node = namedtuple("Node", ["x", "y"])

DIRECTIONS = {(1, 0), (0, 1), (-1, 0), (0, -1)}
WIDTH = 10
HEIGHT = 8
GRID_SIZE = 100


DEFAULT_MAX_FUEL = 30
DEFAULT_START_NODE = Node(0, 3)
DEFAULT_NUM_TILES = 20

DEFAULT_TRAFFIC_LIGHTS = True
DEFAULT_COWS = False
DEFAULT_DECOR = True

# Max parameter value: 1
DEFAULT_BRANCHINESS = 0.3
DEFAULT_LOOPINESS = 0.1
DEFAULT_CURVINESS = 0.5

PERCENTAGE_OF_JUNCTIONS_WITH_TRAFFIC_LIGHTS = 30


def decor_data():
    theme = get_theme(name="grass")

    return {
        "bush": {"ratio": 5, "decor": get_decor_element(theme=theme, name="bush")},
        "tree1": {"ratio": 4, "decor": get_decor_element(theme=theme, name="tree1")},
        "tree2": {"ratio": 3, "decor": get_decor_element(theme=theme, name="tree2")},
        "pond": {"ratio": 1, "decor": get_decor_element(theme=theme, name="pond")},
    }


def decor_sum():
    data = decor_data()
    return (
        data["bush"]["ratio"]
        + data["pond"]["ratio"]
        + data["tree1"]["ratio"]
        + data["tree2"]["ratio"]
    )


def create(episode=None):

    num_tiles = episode.r_num_tiles if episode else DEFAULT_NUM_TILES
    branchiness = episode.r_branchiness if episode else DEFAULT_BRANCHINESS
    loopiness = episode.r_loopiness if episode else DEFAULT_LOOPINESS
    curviness = episode.r_curviness if episode else DEFAULT_CURVINESS
    blocks = episode.r_blocks.all() if episode else Block.objects.all()
    traffic_lights = episode.r_trafficLights if episode else DEFAULT_TRAFFIC_LIGHTS
    cows = episode.r_cows if episode else DEFAULT_TRAFFIC_LIGHTS
    decor = DEFAULT_DECOR

    level_data = generate_random_map_data(
        num_tiles, branchiness, loopiness, curviness, traffic_lights, cows, decor
    )

    level_data["max_fuel"] = DEFAULT_MAX_FUEL
    level_data["theme"] = 1
    level_data["name"] = (
        ("Random level for " + episode.name) if episode else "Default random level"
    )
    level_data["character"] = 1
    level_data["blocklyEnabled"] = episode.r_blocklyEnabled if episode else True
    level_data["pythonEnabled"] = episode.r_pythonEnabled if episode else False
    level_data["blocks"] = [{"type": block.type} for block in blocks]

    level = Level(default=False, anonymous=True)
    level_management.save_level(level, level_data)

    return level


def generate_random_map_data(
    num_tiles,
    branchiness,
    loopiness,
    curviness,
    traffic_lights_enabled,
    decor_enabled,
    cows_enabled,
):
    path = generate_random_path(num_tiles, branchiness, loopiness, curviness)
    traffic_lights = generate_traffic_lights(path) if traffic_lights_enabled else []
    cows = generate_cows(path) if cows_enabled else []
    destinations = [[path[-1]["coordinate"].x, path[-1]["coordinate"].y]]
    origin = get_origin(path)
    decor = generate_decor(path, num_tiles) if decor_enabled else []

    return {
        "path": json.dumps(path),
        "traffic_lights": json.dumps(traffic_lights),
        "cows": json.dumps(cows),
        "origin": json.dumps(origin),
        "destinations": json.dumps(destinations),
        "decor": decor,
    }


def generate_random_path(
    num_road_tiles, branchiness_factor, loopiness_factor, curviness_factor
):
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
                return (
                    origin,
                    pick_destination_node(
                        nodes, connections, origin, possibles, curviness_factor
                    ),
                )

        return None, None

    def pick_origin_node(nodes, connections, branchiness_factor):
        if random.random() < branchiness_factor and len(connections[0]) > 0:
            return random.choice(nodes[1:])
        else:
            return nodes[-1]

    def pick_destination_node(nodes, connections, origin, possibles, curviness_factor):
        existing_connections = [
            nodes[nodeIndex] for nodeIndex in connections[nodes.index(origin)]
        ]
        existing_connection_directions = [
            (node.x - origin.x, node.y - origin.y) for node in existing_connections
        ]
        linear = [
            node
            for node in possibles
            if (origin.x - node.x, origin.y - node.y) in existing_connection_directions
        ]
        curved = [
            node
            for node in possibles
            if (origin.x - node.x, origin.y - node.y)
            not in existing_connection_directions
        ]

        if linear and curved:
            if random.random() < curviness_factor:
                pick_from = curved
            else:
                pick_from = linear
        else:
            pick_from = possibles

        return random.choice(pick_from)

    def join_up_loops(nodes, connections, loopiness_factor):
        nodes_by_location = {
            (node.x, node.y): (index, node) for index, node in enumerate(nodes)
        }
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
                    row.append(float("inf"))
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
                        if (
                            adjacent_node_index > node_index
                            and adjacent_node != nodes[0]
                        ):
                            if adjacent_node_index not in connections[node_index]:
                                possible_loops.append((node_index, adjacent_node_index))

        if len(possible_loops) == 0:
            return connections

        # Minimum deviation at very low and high loopiness factors, maximum at 0.5
        loopiness_deviation = 2 * loopiness_factor * (1 - loopiness_factor)

        # Now join up loops (does not dynamically update distances, but still get required effect)
        max_loop_distance = max([distances[s][d] for s, d in possible_loops])
        for origin, destination in possible_loops:
            distance_factor = distances[origin][destination] / max_loop_distance
            adjusted_loopiness_factor = loopiness_factor * (
                (1 - loopiness_deviation) + loopiness_deviation * distance_factor
            )
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
        return (
            (node not in nodes) and 0 < node.x < WIDTH - 1 and 0 < node.y < HEIGHT - 1
        )

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
        (previous_node, new_node) = pick_adjacent_node(
            nodes, connections, branchiness_factor, curviness_factor
        )
        if new_node:
            nodes.append(new_node)
            index_by_node[new_node] = len(nodes) - 1
            connections = add_new_connections(
                connections, len(nodes) - 1, index_by_node[previous_node]
            )

    connections = join_up_loops(nodes, connections, loopiness_factor)
    result = []
    for index, node in enumerate(nodes):
        result.append(
            {
                "coordinate": node,
                "connectedNodes": sorted(
                    connections[index],
                    key=lambda conn: calculate_node_angle(node, nodes[conn]),
                    reverse=True,
                ),
            }
        )

    return result


def get_origin(path):
    node = path[1]
    neighbour = path[0]
    direction = get_direction(node, neighbour)
    return {
        "coordinate": [neighbour["coordinate"].x, neighbour["coordinate"].y],
        "direction": direction,
    }


def generate_traffic_lights(path):
    degree2Nodes = []
    degree3or4Nodes = []

    for node in path:
        degree = len(node["connectedNodes"])
        if degree == 3 or degree == 4:
            degree3or4Nodes.append(node)
        elif degree == 2:
            degree2Nodes.append(node)

    if len(degree3or4Nodes) > 0:
        candidateNodes = degree3or4Nodes
    else:
        candidateNodes = degree2Nodes

    numberOfJunctions = max(
        int(len(candidateNodes) * PERCENTAGE_OF_JUNCTIONS_WITH_TRAFFIC_LIGHTS / 100.0),
        1,
    )

    random.shuffle(candidateNodes)
    nodesSelected = candidateNodes[:numberOfJunctions]

    trafficLights = []
    for node in nodesSelected:

        controlledNeighbours = []
        for neighbourIndex in node["connectedNodes"]:
            neighbour = path[neighbourIndex]
            if neighbour not in nodesSelected:
                controlledNeighbours.append(neighbour)

        counter = 0
        for neighbour in controlledNeighbours:
            neighbourIndex = path.index(neighbour)

            direction = get_direction(node, neighbour)

            trafficLights.append(
                {
                    "sourceCoordinate": {
                        "x": neighbour["coordinate"].x,
                        "y": neighbour["coordinate"].y,
                    },
                    "direction": direction,
                    "startTime": 0 if counter == 0 else 2 * (counter - 1),
                    "startingState": "GREEN" if counter == 0 else "RED",
                    "greenDuration": 2,
                    "redDuration": 2 * (len(controlledNeighbours) - 1),
                }
            )
            counter += 1

    return trafficLights


def generate_cows(path):
    # TODO Cows
    return []


def get_direction(node, neighbour):
    if neighbour["coordinate"].y < node["coordinate"].y:
        direction = "N"
    elif neighbour["coordinate"].x < node["coordinate"].x:
        direction = "E"
    elif neighbour["coordinate"].y > node["coordinate"].y:
        direction = "S"
    elif neighbour["coordinate"].x > node["coordinate"].x:
        direction = "W"
    return direction


def generate_decor(path, num_tiles):
    DECOR_DATA = decor_data()
    DECOR_SUM = decor_sum()

    def find_node_by_coordinate(x, y, dec, nodes):
        for node in nodes:
            coord = node["coordinate"]
            if (
                coord.x == x
                and coord.y == y
                or (dec == "pond" and coord.x == x + 1 and coord.y == y)
            ):
                return True
        return False

    def find_decor_by_coordinate(x, y, elem, decor):
        for dec in decor:
            coord = dec["coordinate"]

            # if there is a decor occupying this grid or neighbouring one in case of the pond
            if (
                coord["x"] / GRID_SIZE == x
                and coord["y"] / GRID_SIZE == y
                or (
                    elem == "pond"
                    and (
                        coord["x"] / GRID_SIZE == x + 1
                        and coord["y"] / GRID_SIZE == y
                        or x + 1 < WIDTH
                    )
                )
                or (
                    dec["decorName"] == "pond"
                    and coord["x"] / GRID_SIZE + 1 == x
                    and coord["y"] / GRID_SIZE == y
                )
            ):
                return True

        return False

    def near_road(x, y, nodes):
        for node in nodes:
            coord = node["coordinate"]
            if (
                math.fabs(coord.x - x) <= 1
                and math.fabs(coord.y - y) <= 1
                and not find_node_by_coordinate(x, y, "bush", nodes)
            ):
                return True
        return False

    def append_decor(decor, x, y, dec, dx=0, dy=0):
        decor_object = DECOR_DATA[dec]["decor"]
        x = x * GRID_SIZE + int((GRID_SIZE - decor_object.width) * 0.5 * (1 - dx))
        y = y * GRID_SIZE + int((GRID_SIZE - decor_object.height) * 0.5 * (1 - dy))

        decor.append(
            {
                "coordinate": {"x": x, "y": y},
                "decorName": dec,
                "height": decor_object.height,
            }
        )

    def place_near_road(elem, decor, path):
        for i in range(1, len(path) - 1):
            node = path[i]
            for (dx, dy) in DIRECTIONS:
                x = node["coordinate"].x + dx
                y = node["coordinate"].y + dy
                if not (
                    find_decor_by_coordinate(x, y, elem, decor)
                    or find_node_by_coordinate(x, y, dec, path)
                ):
                    return append_decor(decor, x, y, elem, dx, dy)

    def place_randomly(dec, decor):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 7)

            if not (
                find_decor_by_coordinate(x, y, dec, decor)
                or find_node_by_coordinate(x, y, dec, path)
            ):
                return append_decor(decor, x, y, dec)

    def place_bush(elem, decor, nodes):
        bush_exists = False
        for dec in decor:
            if dec["decorName"] == elem:
                bush_exists = True
                for (dx, dy) in DIRECTIONS:
                    x = dec["coordinate"]["x"] / GRID_SIZE + dx
                    y = dec["coordinate"]["y"] / GRID_SIZE + dy
                    if near_road(x, y, nodes) and not find_decor_by_coordinate(
                        x, y, elem, decor
                    ):
                        return append_decor(decor, x, y, elem, dx, dy)

        if not bush_exists:
            place_near_road(elem, decor, path)

    decor = []
    decor_count = 0
    for dec in DECOR_DATA:
        for i in range(0, DECOR_DATA[dec]["ratio"] * num_tiles / DECOR_SUM):
            if decor_count + num_tiles < WIDTH * HEIGHT:
                if dec == "bush":
                    place_bush(dec, decor, path)
                    decor_count += 1
                elif dec == "pond":
                    place_randomly(dec, decor)
                    decor_count += 2
                else:
                    place_randomly(dec, decor)
                    decor_count += 1

    for dec in decor:
        dec["x"] = dec["coordinate"]["x"]
        dec["y"] = dec["coordinate"]["y"]
        del dec["coordinate"]

    return decor

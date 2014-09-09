from django.test import TestCase
from database_objects import setup_decor, setup_themes
from game.random_road import *

import json
import random


def find_node(x, y, nodes):
        for node in nodes:
            if node['coordinate'][0] == x and node['coordinate'][1] == y:
                return True
        return False


class RandomRoadTestCase(TestCase):

    def create_test_data(self, num_tiles=None, branchiness=None, loopiness=None, curviness=None,
                         traffic_lights_enabled=False):
        if not num_tiles:
            num_tiles = random.randint(3, 30)
        if not branchiness:
            branchiness = random.randint(0, 10)
        if not loopiness:
            loopiness = random.randint(0, 10)
        if not curviness:
            curviness = random.randint(0, 10)

        return generate_random_map_data(num_tiles, branchiness, loopiness, curviness,
                                        traffic_lights_enabled)

    def check_if_valid(self, origin, destinations, path, decor):
        check = find_node(origin['coordinate'][0], origin['coordinate'][1], path)
        self.assertTrue(check)

        for node in destinations:
            self.assertTrue(find_node(node[0], node[1], path))

        # Check if any decor got generated
        self.assertTrue(decor)

    def setUp(self):
        setup_decor()
        setup_themes()

    def test_branchiness_min(self):
        """ Test that if the branchiness is 0 we don't get branches. """

        data = self.create_test_data(branchiness=0, loopiness=0, traffic_lights_enabled=False)

        path = json.loads(data['path'])
        destinations = json.loads(data['destinations'])
        traffic_lights = json.loads(data['traffic_lights'])
        origin = json.loads(data['origin'])
        decor = json.loads(data['decor'])

        self.check_if_valid(origin, destinations, path, decor)

        # Test if no branches
        for node in path:
            self.assertTrue(len(node['connectedNodes']) <= 2)

        # Assert no traffic lights got generated.
        self.assertFalse(traffic_lights)

    def test_curviness_max(self):
        """ Test that the path is curving significantly if the curviness is set to max value. """

        data = self.create_test_data(curviness=1, traffic_lights_enabled=False)

        path = json.loads(data['path'])
        destinations = json.loads(data['destinations'])
        traffic_lights = json.loads(data['traffic_lights'])
        origin = json.loads(data['origin'])
        decor = json.loads(data['decor'])

        self.check_if_valid(origin, destinations, path, decor)

        turn_count = 0
        for node in path:
            turn_count += int(
                not (get_direction(node['coordinate'], path[node['connectedNodes'][0]])
                     == get_direction(node['coordinate'], path[node['connectedNodes'][1]]))
            )

        self.assertTrue(turn_count)

        # Assert no traffic lights got generated.
        self.assertFalse(traffic_lights)

from django.test import TestCase
from database_objects import setup_decor, setup_themes 
from game.random_road import *

import json
import random


class RandomRoadTestCase(TestCase):

    def setUp(self):
        setup_decor()
        setup_themes()

    def test_branchiness_0(self):
        """ Test that the path is is 0 we don't get branches"""

        def find_node(x, y, nodes):
            for node in nodes:
                if node['coordinate'].x == x and nodeCoordinates['coordinate'].y == y:
                    return True
            return False

        num_tiles = random.randint(3, 20)
        branchiness = 0
        loopiness = 0
        curviness = random.randint(0, 10)
        traffic_lights_enabled = False

        data = generate_random_map_data(num_tiles, branchiness, loopiness, curviness, traffic_lights_enabled)

        path = json.loads(data['path'])
        destinations = json.loads(data['destinations'])
        traffic_lights = json.loads(data['traffic_lights'])
        origin = json.loads(data['origin'])
        decor = json.loads(data['decor'])

        # Test if no branches
        for node in path:
            self.assertTrue(len(node['connectedNodes']) <= 2)

        # Test if start and end belong to the path.
        self.assertTrue(find_node(origin['coordinate'][0], origin['coordinate'][1], path))

        for node in destinations:
            self.assertTrue(find_node(node[0], node[1], path))

        # Assert no traffic lights got generated.
        assertFalse(traffic_lights)

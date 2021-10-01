import json
import random
import itertools
from django.test import TestCase

from game.random_road import generate_random_map_data


def find_node(x, y, nodes):
    for node in nodes:
        if node["coordinate"][0] == x and node["coordinate"][1] == y:
            return True
    return False


def check_direction(node, neighbour):
    if neighbour["coordinate"][1] < node["coordinate"][1]:
        direction = "N"
    elif neighbour["coordinate"][0] < node["coordinate"][0]:
        direction = "E"
    elif neighbour["coordinate"][1] > node["coordinate"][1]:
        direction = "S"
    elif neighbour["coordinate"][0] > node["coordinate"][0]:
        direction = "W"
    return direction


class RandomRoadTestCase(TestCase):
    def create_test_data(
        self,
        num_tiles=None,
        branchiness=None,
        loopiness=None,
        curviness=None,
        traffic_lights_enabled=False,
        decor_enabled=True,
        cows_enabled=False,
    ):
        if num_tiles is None:
            num_tiles = random.randint(3, 40)
        if branchiness is None:
            branchiness = random.random()
        if loopiness is None:
            loopiness = random.random()
        if curviness is None:
            curviness = random.random()

        return generate_random_map_data(
            num_tiles,
            branchiness,
            loopiness,
            curviness,
            traffic_lights_enabled,
            decor_enabled,
            cows_enabled,
        )

    def check_if_valid(self, origin, destinations, path, decor):
        check = find_node(origin["coordinate"][0], origin["coordinate"][1], path)
        self.assertTrue(check)

        for node in destinations:
            self.assertTrue(find_node(node[0], node[1], path))

        if decor:
            # Check if any decor got generated
            self.assertTrue(decor)

    def test_tiles_less_or_equal_size(self):
        """Test that the number of tiles is less or equal to the size parameter"""

        number_of_tiles = 30
        data = self.create_test_data(num_tiles=number_of_tiles)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Test if number of tiles = size
        self.assertTrue(len(path) <= number_of_tiles)

    def test_branchiness_min(self):
        """Test that if the branchiness is 0 we don't get branches."""

        data = self.create_test_data(branchiness=0, loopiness=0)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Test if no branches
        for node in path:
            self.assertTrue(len(node["connectedNodes"]) <= 2)

    def test_branchiness_max(self):
        """Test that if the branchiness > 0 we get branches."""

        data = self.create_test_data(branchiness=2, loopiness=0)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Test if some branches
        branch_count = 0
        for node in path:
            if len(node["connectedNodes"]) > 2:
                branch_count += 1

        self.assertTrue(branch_count)

    def test_curviness_max(self):
        """Test that the path is curving significantly if the curviness is set to max value."""

        data = self.create_test_data(curviness=1.0)
        path = json.loads(data["path"])

        destinations = json.loads(data["destinations"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        num_curves = 0
        for node in path:
            already_checked_for_curves = (
                []
            )  # So that A->B->C and C->B->A don't count as two separate curves
            if len(node["connectedNodes"]) > 1:
                for (one_way, other_way) in itertools.combinations(
                    node["connectedNodes"], 2
                ):
                    if (
                        one_way,
                        other_way,
                    ) not in already_checked_for_curves:
                        already_checked_for_curves.append(
                            (
                                one_way,
                                other_way,
                            )
                        )
                        already_checked_for_curves.append(
                            (
                                other_way,
                                one_way,
                            )
                        )

                        previous_to_this = check_direction(path[one_way], node)
                        this_to_next = check_direction(node, path[other_way])

                        num_curves += int(not (previous_to_this == this_to_next))

        if len(path) == 3:
            self.assertEqual(num_curves, 1)
        else:
            self.assertGreaterEqual(num_curves, 2)

    def test_traffic_light_no(self):
        """Test that traffic lights don't get generated"""

        data = self.create_test_data(traffic_lights_enabled=False)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        traffic_lights = json.loads(data["traffic_lights"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Assert no traffic lights got generated.
        self.assertFalse(traffic_lights)

    def test_traffic_light_yes(self):
        """Test that traffic lights get generated"""

        data = self.create_test_data(traffic_lights_enabled=True)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        traffic_lights = json.loads(data["traffic_lights"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Assert no traffic lights got generated.
        self.assertTrue(traffic_lights)

    def test_decor_no(self):
        """Test that scenery doesn't get generated"""

        data = self.create_test_data(decor_enabled=False)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Assert no scenery got generated.
        self.assertFalse(decor)

    def test_decor_yes(self):
        """Test that scenery does get generated"""

        data = self.create_test_data(decor_enabled=True)

        path = json.loads(data["path"])
        destinations = json.loads(data["destinations"])
        origin = json.loads(data["origin"])
        decor = data["decor"]

        self.check_if_valid(origin, destinations, path, decor)

        # Assert scenery got generated.
        self.assertTrue(decor)

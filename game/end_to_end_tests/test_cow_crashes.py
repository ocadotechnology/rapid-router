from game.character import get_character
from game.end_to_end_tests.base_game_test import BaseGameTest
from game.models import Level, Block, LevelBlock
from game.theme import get_theme


class TestCowCrashes(BaseGameTest):
    cow_level = None

    def test_crash_into_cow_going_forward(self):
        self.run_cow_crashing_test("crash_into_cow_going_forward")

    def test_crash_into_cow_turning_left(self):
        self.run_cow_crashing_test("crash_into_cow_turning_left")

    def test_crash_into_cow_turning_right(self):
        self.run_cow_crashing_test("crash_into_cow_turning_right")

    def test_crash_into_cow_on_t_junction(self):
        self.run_cow_crashing_test("crash_into_cow_on_t_junction")

    def test_crash_into_cow_on_t_junction2(self):
        self.run_cow_crashing_test("crash_into_cow_on_t_junction2")

    def test_crash_into_cow_on_t_junction3(self):
        self.run_cow_crashing_test("crash_into_cow_on_t_junction3")

    def test_crash_into_cow_on_crossroads_junction(self):
        self.run_cow_crashing_test("crash_into_cow_on_crossroads_junction")

    def run_cow_crashing_test(self, workspace_file):
        user_profile = self.login_once()
        TestCowCrashes.cow_level.owner = user_profile
        TestCowCrashes.cow_level.save()
        workspace_id = self.use_workspace(workspace_file, user_profile)
        self.go_to_custom_level(TestCowCrashes.cow_level).load_solution(
            workspace_id
        ).run_cow_crashing_program()

    @classmethod
    def setUpClass(cls):
        BaseGameTest.setUpClass()
        grass = get_theme(name="grass")

        van = get_character("Van")

        TestCowCrashes.cow_level = Level(
            name="Cow crashing",
            anonymous=False,
            blockly_enabled=True,
            character=van,
            cows='[{"minCows":"7","maxCows":"7","potentialCoordinates":[{"x":4,"y":4},{"x":2,"y":4},{"x":3,"y":7},{"x":4,"y":6},{"x":2,"y":6},{"x":3,"y":1},{"x":4,"y":2}],"type":"WHITE"}]',
            default=False,
            destinations="[[4,5]]",
            fuel_gauge=False,
            max_fuel=50,
            model_solution="[1]",
            origin='{"coordinate":[2,5],"direction":"E"}',
            path='[{"coordinate":[2,5],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,4,2,5]},{"coordinate":[4,5],"connectedNodes":[1]},{"coordinate":[3,7],"connectedNodes":[4]},{"coordinate":[3,6],"connectedNodes":[8,3,6,1]},{"coordinate":[3,4],"connectedNodes":[10,1,11,16]},{"coordinate":[4,6],"connectedNodes":[4,7]},{"coordinate":[4,7],"connectedNodes":[6]},{"coordinate":[2,6],"connectedNodes":[9,4]},{"coordinate":[2,7],"connectedNodes":[8]},{"coordinate":[2,4],"connectedNodes":[13,5,12]},{"coordinate":[4,4],"connectedNodes":[5,14,15]},{"coordinate":[2,3],"connectedNodes":[10]},{"coordinate":[1,4],"connectedNodes":[10]},{"coordinate":[5,4],"connectedNodes":[11]},{"coordinate":[4,3],"connectedNodes":[11,19]},{"coordinate":[3,3],"connectedNodes":[5,17]},{"coordinate":[3,2],"connectedNodes":[18,16,19,20]},{"coordinate":[2,2],"connectedNodes":[17]},{"coordinate":[4,2],"connectedNodes":[17,15,23,22]},{"coordinate":[3,1],"connectedNodes":[21,17,22]},{"coordinate":[2,1],"connectedNodes":[20]},{"coordinate":[4,1],"connectedNodes":[20,19]},{"coordinate":[5,2],"connectedNodes":[19]}]',
            python_enabled=False,
            theme=grass,
            threads=1,
            traffic_lights="[]",
        )

        TestCowCrashes.cow_level.save()

        blocks = Block.objects.filter(
            type__in=["move_forwards", "turn_left", "turn_right"]
        )

        for block in blocks:
            new_block = LevelBlock(
                type=block, number=None, level=TestCowCrashes.cow_level
            )
            new_block.save()

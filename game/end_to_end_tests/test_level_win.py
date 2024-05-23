from game.end_to_end_tests.base_game_test import BaseGameTest
from game.models import Level


class TestLevelWin(BaseGameTest):
    custom_level = None

    def test_deliver_everywhere(self):
        self.deliver_everywhere_test(level=16)

    def test_try_again_if_not_full_score(self):
        page = self.try_again_if_not_full_score_test(
            level=19, workspace_file="complete_level_not_with_full_score"
        )
        self.complete_and_check_level(19, page)

    def test_custom_level_scoring(self):
        user_profile = self.login_once()
        TestLevelWin.custom_level.owner = user_profile
        TestLevelWin.custom_level.save()
        workspace_id = self.use_workspace("custom_level_scoring_solution_file", user_profile)
        self.go_to_custom_level(TestLevelWin.custom_level).load_solution(workspace_id).run_custom_level_program()

    @classmethod
    def setUpClass(cls):
        BaseGameTest.setUpClass()

        TestLevelWin.custom_level = Level(
            name="Custom level",
            anonymous=False,
            blocklyEnabled=True,
            character=van,
            cows='[]',
            default=False,
            destinations="[[3,4]]",
            direct_drive=True,
            fuel_gauge=False,
            max_fuel=50,
            model_solution="[1]",
            origin='{"coordinate":[3,5],"direction":"S"}',
            path='[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],' '"connectedNodes":[0]}]',
            pythonEnabled=False,
            theme=grass,
            threads=1,
            traffic_lights="[]",
        )


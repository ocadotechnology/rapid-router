from game.end_to_end_tests.base_game_test import BaseGameTest


class TestRegressions(BaseGameTest):
    def test_crash_turning_left_clear_and_pass_level(self):
        page = self.running_out_of_instructions_test(
            level=45, workspace_file="double_forwards"
        ).try_again()

        page.step()

        page.assert_is_green_light(0)

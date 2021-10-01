from game.end_to_end_tests.base_game_test import BaseGameTest


class TestTurningAround(BaseGameTest):
    def test_turn_around_on_straight_road(self):
        self.running_out_of_instructions_test(
            level=40, workspace_file="turn_around_on_straight_road"
        )

    def test_turn_around_on_left_turn(self):
        self.running_out_of_instructions_test(
            level=40, workspace_file="turn_around_on_left_turn"
        )

    def test_turn_around_on_right_turn(self):
        self.running_out_of_instructions_test(
            level=40, workspace_file="turn_around_on_right_turn"
        )

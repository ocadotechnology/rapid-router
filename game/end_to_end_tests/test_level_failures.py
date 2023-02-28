from game.end_to_end_tests.base_game_test import BaseGameTest


class TestCrashes(BaseGameTest):
    def test_crash_turning_left_on_straight_road(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_left_on_straight_road"
        )

    def test_crash_turning_left_on_right_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_left_on_right_turn"
        )

    def test_crash_turning_right_on_straight_road(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_right_on_straight_road"
        )

    def test_crash_turning_right_on_left_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_right_on_left_turn"
        )

    def test_crash_going_forward_on_right_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_going_forward_on_right_turn"
        )

    def test_crash_going_forward_on_left_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_going_forward_on_left_turn"
        )

    def test_crash_going_forward_on_t_junction(self):
        self.run_crashing_test(
            level=13, workspace_file="crash_going_forward_on_t_junction"
        )

    def test_crash_going_left_on_t_junction(self):
        self.run_crashing_test(
            level=40, workspace_file="crash_going_left_on_t_junction"
        )

    def test_crash_going_right_on_t_junction(self):
        self.run_crashing_test(
            level=40, workspace_file="crash_going_right_on_t_junction"
        )

    def test_running_out_of_instructions(self):
        self.running_out_of_instructions_test(
            level=6, workspace_file="running_out_of_instructions"
        )

    def test_running_out_of_fuel(self):
        self.running_out_of_fuel_test(level=68, workspace_file="running_out_of_fuel")

    def test_running_a_red_light(self):
        self.running_a_red_light_test(level=44, workspace_file="running_a_red_light")

    def test_not_delivered_everywhere(self):
        self.not_delivered_everywhere_test(
            level=16, workspace_file="not_delivered_everywhere"
        )

    def test_procedure_undefined(self):
        self.undefined_procedure_test(level=63, workspace_file="undefined_procedure")

    def test_crash_turning_left_clear_and_pass_level(self):
        page = (
            self.run_crashing_test(
                level=6, workspace_file="crash_turning_left_on_straight_road"
            )
            .try_again()
            .clear()
        )

        self.complete_and_check_level(6, page, check_algorithm_score=False)

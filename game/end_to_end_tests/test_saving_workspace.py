import random
import string

from game.end_to_end_tests.base_game_test import BaseGameTest


class TestSavingWorkspace(BaseGameTest):
    already_logged_on = False
    user_profile = None

    def test_save_and_load_workspace(self):
        self.login_once()
        level = 10
        random_save_entry_name = "".join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(10)
        )
        return (
            self.go_to_level(level)
            .save_solution(random_save_entry_name)
            .load_solution_by_name(random_save_entry_name)
        )

from game.end_to_end_tests.base_game_test import BaseGameTest


class TestLevelWin(BaseGameTest):
    def test_deliver_everywhere(self):
        self.deliver_everywhere_test(level=16)

    def test_try_again_if_not_full_score(self):
        page = self.try_again_if_not_full_score_test(
            level=19, workspace_file="complete_level_not_with_full_score"
        )
        self.complete_and_check_level(19, page)

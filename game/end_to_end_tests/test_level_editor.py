from game.end_to_end_tests.base_game_test import BaseGameTest
from game.views.level_editor import available_blocks


class TestLevelEditor(BaseGameTest):
    def test_level_editor_displays(self):
        page = self.go_to_level_editor()

        assert page.element_exists_by_id("paper")

    def test_code_tab_blocks_load(self):
        page = self.go_to_level_editor()
        page.go_to_code_tab()

        block_types = [block.type for block in available_blocks()]

        for block_type in block_types:
            assert page.element_exists_by_id(f"{block_type}_checkbox")
            assert page.element_exists_by_id(f"{block_type}_image")

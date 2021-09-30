from game.end_to_end_tests.base_game_test import BaseGameTest


class TestPythonLevels(BaseGameTest):
    def test_can_see_python_commands(self):
        self.run_python_commands_test(level=92)

    def test_clear_console(self):
        self.run_clear_console_test(level=92)

    def test_console_parse_error(self):
        self.run_console_parse_error_test(level=92)

    def test_console_attribute_error(self):
        self.run_console_attribute_error_test(level=92)

    def test_console_print(self):
        self.run_console_print_test(level=92)

    def test_invalid_import(self):
        self.run_invalid_import_test(level=109)

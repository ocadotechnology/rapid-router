from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from game.character import get_character
from game.end_to_end_tests.base_game_test import BaseGameTest
from game.models import Level
from game.theme import get_theme

DELAY_TIME = 10


class TestPythonLevels(BaseGameTest):
    def test_can_see_python_commands(self):
        self.go_to_level(4, from_python_den=True).check_python_commands()

    def test_clear_console(self):
        self.go_to_level(4, from_python_den=True).write_to_then_clear_console()

    def test_console_parse_error(self):
        self.go_to_level(4, from_python_den=True).run_parse_error_program()

    def test_console_attribute_error(self):
        self.go_to_level(4, from_python_den=True).run_attribute_error_program()

    def test_console_print(self):
        self.go_to_level(4, from_python_den=True).run_print_program()

    def test_invalid_import(self):
        self.go_to_level(5, from_python_den=True).run_invalid_import_program()

    def test_run_code(self):
        self.go_to_level(4, from_python_den=True)
        run_code = self.selenium.find_element(By.ID, "run-code-button")
        run_code.click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_all_elements_located((By.ID, "myModal-lead"))
        )

    def test_animal_sound_horn(self):
        grass = get_theme(name="grass")

        van = get_character("Van")

        animal_level = Level(
            name="Animal commands",
            anonymous=False,
            blockly_enabled=False,
            character=van,
            cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":4}],"type":"WHITE"}]',
            default=False,
            destinations="[[4,4]]",
            fuel_gauge=False,
            max_fuel=50,
            model_solution="",
            origin='{"coordinate":[2,4],"direction":"E"}',
            path='[{"coordinate":[2,4],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1]}]',
            python_enabled=True,
            theme=grass,
            threads=1,
            traffic_lights="[]",
            disable_algorithm_score=True,
        )

        user_profile = self.login_once()
        animal_level.owner = user_profile
        animal_level.save()

        self.run_animal_sound_horn_test(animal_level).assert_success()

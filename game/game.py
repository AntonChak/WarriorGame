from typing import Optional
from character import Character
from menu import Menu
from menu.exceptions import ValidationError
from menu.interface import InputResult
from scenario import Scenario
from scenario.exceptions import ScenarioFinished
from scenario.scenario_manager import ScenarioManager


class Game:

    def __init__(self, menu: Menu):
        self.menu = menu
        self.new_game = True
        self._exit_scenario = False
        self._character: Optional[Character] = None

    @property
    def character(self):
        return self._character

    @property
    def exit_scenario(self):
        return self._exit_scenario

    def start_new_game(self):
        """
        Entrypoint to start new game.
        """
        scenario = ScenarioManager.new_game()
        while not self.exit_scenario:
            try:
                # Execute steps from json, e.g. {"step_0": {...}, ...}
                self.process_scenario(scenario=scenario)
            except ScenarioFinished:
                self._exit_scenario = True

    def process_scenario(self, scenario: Scenario):
        """
        Execute step from scenario.
        """
        if scenario.input_required:
            # Display + Input from user.
            try:
                result = self.menu.make_input(scenario)
            except ValidationError:
                return

            # Set inputted value to the instance.
            # TODO: Add validation on `hasattr` or raise Exception.
            if scenario.attribute:
                instance = self
                for attribute in scenario.attribute.split(".")[:-1]:
                    instance = getattr(instance, attribute)

                attribute_name = scenario.attribute.rsplit(".", 1)[-1]
                setattr(instance, attribute_name, result.value)

        else:
            # Display to user.
            params = {}
            for param in scenario.params:
                value = self
                for parameter in param.split('.'):
                    value = getattr(value, parameter)

                params[param] = value

            result = self.menu.display_dialog(scenario, **params)

        # Functions to execute on backend.
        for post_process in scenario.post_process:
            func_ = getattr(self, post_process)
            func_(result, scenario)

        scenario.step_finished()
        return result

    def create_character(self, result: InputResult, scenario: Scenario):
        self._character = Character(name=result.value)

import os
from menu.interface import DialogResult, InputResult
from menu.const import Step
from menu.validators import Validator
from game.exceptions import DataTypeException, DataValueException
from menu.exceptions import ValidationError
from scenario import Scenario


class Menu:

    def __init__(self):
        self._steps = []
        self._current_step = Step.START
        self._previous_step = Step.START

    @property
    def current_step(self):
        return self._current_step

    @property
    def previous_step(self):
        return self._previous_step

    @property
    def steps(self):
        return self._steps

    def change_step(self, new_step: Step):
        self._steps.append(self.previous_step)
        self._previous_step = self.current_step
        self._current_step = new_step

    def display_dialog(self, scenario: Scenario, **params) -> DialogResult:
        """
        Displays dialog message to user.
        """
        self.display_message(scenario.message, **params)

        return DialogResult()

    def make_input(self, scenario: Scenario) -> InputResult:
        """
        General function that:
        - display input message
        - waits until used input data
        - validate inputted data
        """
        if scenario.message:
            self.display_message(scenario.message)

        # TODO: bug.
        # Add any letters in input, delete it and write new string.
        # Exists first letter from first input in the result.
        result = input()

        for validator in scenario.validators:
            validator_ = getattr(Validator, validator)
            try:
                validator_(result)
            except (DataTypeException, DataValueException) as e:
                self.display_message(e.message)
                raise ValidationError()

        return InputResult(value=result)

    @staticmethod
    def clear():
        """
        Clear console.
        :return:
        """
        return os.system("clear")

    @staticmethod
    def display_message(message: str, **params):
        print(f"\n{message.format(**params)}")

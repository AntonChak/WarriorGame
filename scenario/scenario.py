from typing import Dict
from scenario.exceptions import ScenarioFinished


class Scenario:
    """
    Represents single game `action`, `scene`.

    Scenario build based on json file, stored in `static/messages/`.
    """

    def __init__(self, data: Dict):
        self.original_data = data
        self._step_counter = 0

    @property
    def input_required(self):
        """
        Represents if input is required on current step.
        """
        return self.original_data[self._get_key()].get("input_required", False)

    @property
    def message(self):
        """
        Returns message that should be displayed for user in CLI.
        """
        return self.original_data[self._get_key()].get("message", "Input please:")

    @property
    def validators(self):
        """
        List of validators that should be called whenever user input the value.
        """
        return self.original_data[self._get_key()].get("validators", [])

    @property
    def attribute(self):
        """
        What attribute user had inputted.
        """
        return self.original_data[self._get_key()].get("attribute", "")

    @property
    def post_process(self):
        """
        List of function names that should be called after step execution.
        """
        return self.original_data[self._get_key()].get("post_process", [])

    @property
    def params(self):
        """
        List of parameter names that should be passed in message.
        """
        return self.original_data[self._get_key()].get("params", [])

    def reset(self):
        self._step_counter = 0

    def step_finished(self):
        self._step_counter += 1

    def _get_key(self) -> str:
        """
        Builds key to proceed sequence of actions in scenario.
        """
        key = f"step_{self._step_counter}"
        if not self.original_data.get(key):
            raise ScenarioFinished()

        return key

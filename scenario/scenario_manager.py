import os
import json
from typing import Dict
from scenario import Scenario
from settings import ROOT_FOLDER


class ScenarioManager:
    MESSAGES_PATH = "static/scenarios"

    @classmethod
    def new_game(cls):
        return Scenario(cls._parse_file("new_game.json"))

    @classmethod
    def _parse_file(cls, filename: str) -> Dict:
        abs_file = os.path.join(ROOT_FOLDER, cls.MESSAGES_PATH, filename)
        with open(abs_file, "r+") as f:
            data = f.read()

        data = json.loads(data)

        return data

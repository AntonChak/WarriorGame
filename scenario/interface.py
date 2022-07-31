from typing import List
from dataclasses import dataclass


@dataclass
class ScenarioStep:
    input_required: bool
    message: str
    validators: List[str]
    attribute: str
    post_process: List[str]
    params: str

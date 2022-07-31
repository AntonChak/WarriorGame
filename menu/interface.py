from typing import List, Optional, Union
from dataclasses import dataclass


@dataclass
class DialogResult:
    input_required: Optional[bool] = False
    message: Optional[str] = ""
    validators: Optional[List[str]] = list
    attribute: Optional[str] = ""
    params: Optional[str] = list


@dataclass
class InputResult:
    value: Union[str, int, float]

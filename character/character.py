from typing import Optional
from character.const import Gender, CharacterClassType


class Character:

    def __init__(
            self,
            name: str,
            gender: Optional[Gender] = Gender.NOT_SELECTED,
            class_type: Optional[CharacterClassType] = CharacterClassType.NOT_SELECTED
    ):
        self.name = name
        self._gender = gender
        self._class_type = class_type

    def __str__(self):
        return f"{self.name} is a {self.gender.label} class {self.class_type.label}"

    @property
    def class_type(self):
        return self._class_type

    @class_type.setter
    def class_type(self, value):
        self._class_type = CharacterClassType(value)

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = Gender(value)

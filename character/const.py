from enum import Enum


class CustomEnum(Enum):
    @property
    def label(self):
        return f"{' '.join(self.name.lower().capitalize().split('_'))}"


class CharacterClassType(CustomEnum):
    NOT_SELECTED = "not_selected"
    WARRIOR = "1"
    ARCHER = "2"
    MAGE = "3"


class Gender(CustomEnum):
    NOT_SELECTED = "not_selected"
    MALE = "1"
    FEMALE = "2"

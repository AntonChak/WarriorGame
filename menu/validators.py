from game.exceptions import DataTypeException, DataValueException


class Validator:
    CLASS_TYPE_LIMIT = (1, 3)
    GENDER_LIMIT = (1, 2)

    @staticmethod
    def string_required(value):
        if not value:
            raise DataTypeException("This value is required.")

        return str(value)

    @staticmethod
    def int_required(value):
        if not value:
            raise DataTypeException("This value is required.")

        try:
            return int(value)
        except ValueError:
            raise DataTypeException("You can choose only integer value.")

    @classmethod
    def class_type_limit(cls, value):
        if cls.CLASS_TYPE_LIMIT[0] <= int(value) <= cls.CLASS_TYPE_LIMIT[1]:
            return value

        raise DataValueException("Your choose should be between 1 and 3.")

    @classmethod
    def gender_limit(cls, value):
        if cls.GENDER_LIMIT[0] <= int(value) <= cls.GENDER_LIMIT[1]:
            return value

        raise DataValueException("Your choose should be between 1 and 2.")

class DataTypeException(Exception):

    def __init__(self, message: str):
        self.message = message


class DataValueException(Exception):

    def __init__(self, message: str):
        self.message = message

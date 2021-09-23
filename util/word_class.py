class Word:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def get_key(self):
        return self.__key

    def set_key(self, key):
        if isinstance(key, str):
            self.__key = key

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if isinstance(value, str):
            self.__value = value

    def __str__(self):
        return self.__key + ":" + self.__value


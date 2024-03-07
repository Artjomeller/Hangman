class Score:

    def __init__(self, name, word, missing, seconds, time):
        self.__name = name
        self.__word = word
        self.__missing = missing
        self.__seconds = seconds
        self.__time = time

    @property
    def name(self):
        return self.__name

    @property
    def word(self):
        return self.__word

    @property
    def missing(self):
        return self.__missing

    @property
    def seconds(self):
        return self.__seconds

    @property
    def time(self):
        return self.__time

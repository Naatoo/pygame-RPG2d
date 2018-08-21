from random import choice


class GenerateFields:

    def __init__(self):
        self.size = 20
        self.__types = {}

        self.cities()
        self.mountains()
        self.plains()

    def cities(self):
        for _ in range(3):
            self.__types[choice(range(1, 401))] = 4

    def mountains(self):
        for _ in range(3):
            index = choice(range(1, 370))
            [self.__types.update({x: 3}) for x in range(index, index + 20)]

    def plains(self):
        for index in range(1, 401):
            if index not in self.__types.keys():
                self.__types[index] = 1

    @property
    def data(self):
        return self.__types

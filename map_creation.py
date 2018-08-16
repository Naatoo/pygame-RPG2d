from random import choice


class GenerateBiomes:

    def __init__(self):
        self.size = 20
        self.__indexes = ["g" for _ in range(pow(self.size, 2))]
        self.sample_list = [x for x in range(pow(self.size, 2))]

        self.cities()

    def cities(self):
        if self.size == 20:
            for _ in range(3):
                self.__indexes[choice(self.sample_list)] = "C"

    def __call__(self):
        return self.__indexes

    @property
    def indexes(self):
        return self.__indexes

    def __iter__(self):
        return iter(biome for biome in self.__indexes)


class GenerateWeather:

    def __init__(self):
        self.size = 20

    @property
    def data(self):
        return ["SUN" for _ in range(self.size ** 2)]

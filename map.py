from map_creation import GenerateBiomes, GenerateWeather


class Map:
    def __init__(self, session, Field):
        self.size = 20
        self.__fields = session.query(Field)

    def __getitem__(self, item):
        return self.__fields[item - 1]

    def __setitem__(self, key, value, asd):
        pass

    def __format__(self, format_spec='i'):

        if format_spec == "t":
            list_to_format = ['{} ' if field.id % self.size != 0 else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            return joined_list.format(*(field.biome for field in self.__fields))
        elif format_spec == "i":
            list_to_format = ['{}' + " " * round(1 / (len(str(field.id)) / 3)) if field.id % self.size != 0
                              else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            return joined_list.format(*(field.id for field in self.__fields))

    def __repr__(self):
        return format(self, "t")

    @property
    def fields(self):
        return list(self.__fields)

    def insert_data(self, session, Field):
        session.add_all([Field(id=index, biome=biome, weather=weather)
                         for index, biome, weather in
                         zip(range(1, 20 * 20 + 1), GenerateBiomes(), GenerateWeather().data)])

class Country:
    def __init__(self, name):
        self.name = name
        self.region = []

    def add(self, reg):
        self.region.append(reg)

    @property
    def pop(self):
        """The total population of this country"""
        tot = 0
        for reg in self.region:
            tot += reg.pop
        return tot

    @property
    def most_populuous_city(self):
        """The most populous city"""
        cities = []
        for reg in self.region:
            for el in reg.city:
                cities.append(el)
        data = []
        for city in cities:
            data.append(city.pop)

        for city in cities:
            if city.pop == max(data):
                res = city

        return res


class Region:
    def __init__(self, name):
        self.name = name
        self.city = []
        self.pop = 0

    def add(self, cities):
        self.city.append(cities)
        self.pop += cities.pop


class City:
    """A city"""

    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop

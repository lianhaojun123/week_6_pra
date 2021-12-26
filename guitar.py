class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.cost = cost
        self.year = year
        self.name = name

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

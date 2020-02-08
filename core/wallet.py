class People:
    _people = dict()

    def __init__(self, name):
        self.name = name
        People._people[name] = self

    @classmethod
    def find(cls, name):
        return cls._people.get(name, None)    
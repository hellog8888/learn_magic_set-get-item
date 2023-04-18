class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__weight = 0
        self.bag = []

    def __check_weight(self, new_thing, old_thing=None):
        w = new_thing.weight + self.__weight if old_thing is None else new_thing.weight + self.__weight - old_thing.weight
        if w > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
    def add_thing(self, thing):
        self.__check_weight(thing)
        self.bag.append(thing)
        self.__weight += thing.weight

    def __check_index(self, index):
        if not (0 <= index < len(self.bag)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        t = self.bag[key]
        self.__check_weight(value, t)
        self.bag[key] = value
        self.__weight += (value.weight - t.weight)

    def __delitem__(self, key):
        self.__check_index(key)
        temp = self.bag.pop(key)
        self.__weight -= temp.weight
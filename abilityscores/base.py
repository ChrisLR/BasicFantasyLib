import abc


class AbilityScore(object):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["value"]

    _modifier_table = {
        3: -3,
        4: -2,
        5: -2,
        6: -1,
        7: -1,
        8: -1,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 1,
        14: 1,
        15: 1,
        16: 2,
        17: 2,
        18: 3,
    }

    def __init__(self, value):
        self.value = value

    def modifier(self):
        return self._modifier_table[self.value]


class Strength(AbilityScore):
    pass


class Dexterity(AbilityScore):
    pass


class Constitution(AbilityScore):
    pass


class Intelligence(AbilityScore):
    pass


class Wisdom(AbilityScore):
    pass


class Charisma(AbilityScore):
    pass

class Level(object):
    __slots__ = ["value", "attack_bonus", "experience_required", "hit_dice", "saving_throws_set", "spell_slots_set"]

    def __init__(self, value, attack_bonus, experience_required, hit_dice, saving_throws_set, spell_slots_set):
        self.value = value
        self.attack_bonus = attack_bonus
        self.experience_required = experience_required
        self.hit_dice = hit_dice
        self.saving_throws_set = saving_throws_set
        self.spell_slots_set = spell_slots_set


class LevelTable(object):
    __slots__ = ["levels"]

    def __init__(self, levels=None):
        self.levels = {level.value: level for level in levels} if levels else {}

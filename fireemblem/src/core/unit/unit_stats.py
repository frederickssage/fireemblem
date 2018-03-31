"""Unit stats objects"""
from core.rule import FireEmblemRulesetError


class BaseStatsArray(object):

    def __init__(self, ruleset):
        self.ruleset = ruleset
        self.array_stat_dict = {}
        self.stats_list = ruleset.primary_stats_list
        for stat in ruleset.primary_stats_list:
            self.array_stat_dict[stat] = None

    @staticmethod
    def apply_stat_dict(attribute_stat_dict, input_stat_dict):
        if type(input_stat_dict) != dict:
            raise TypeError('Stats arrays must be in the form of a dictionary')
        # assert stat dicts contain positive numbers or 0
        if not compare_stat_dicts(attribute_stat_dict, input_stat_dict):
            raise FireEmblemRulesetError
        for key, value in input_stat_dict:
            attribute_stat_dict[key] = value

    def __str__(self):
        return self.array_stat_dict.__str__()


class DynamicStatsArray(BaseStatsArray):

    def __init__(self, ruleset):
        BaseStatsArray.__init__(self, ruleset)
        self.stat_cap_dict = {}
        self.stat_growth_dict = {}
        for stat in self.stats_list:
            self.stat_cap_dict[stat] = None
            self.stat_growth_dict[stat] = None

    def set_up(self, base_stats, stat_caps, stat_growths):
        self.apply_stat_dict(self.array_stat_dict, base_stats)
        self.apply_stat_dict(self.stat_cap_dict, stat_caps)
        self.apply_stat_dict(self.stat_growth_dict, stat_growths)
        self.enforce_stat_caps()

    def enforce_stat_caps(self):
        for key, value in self.stat_cap_dict:
            if self.array_stat_dict[key] > value:
                self.array_stat_dict[key] = value

    def __str__(self):
        return {
            'Stat Array': self.array_stat_dict,
            'Caps Array': self.stat_cap_dict,
            'Growths Array': self.stat_growth_dict
        }.__str__()

    def advance_by_level(self, level):
        #  assert level is positive number
        #  assert level is valid in ruleset
        for stat in self.stats_list:
            self.array_stat_dict[stat] += level * self.stat_growth_dict[stat]
        self.enforce_stat_caps()


def compare_stat_dicts(stat_dict_1, stat_dict_2):
    if False:  # Compare stat dicts, raise error if not same stats
        return False
    return True
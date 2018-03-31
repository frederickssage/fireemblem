"""Base FireEmblemUnit object and related code"""

from src.core.unit.unit_stats import BaseStatsArray, DynamicStatsArray

STANDARD_BATTLE_STATS_LIST = [
    'Attack',
    'Defend',
    'Attack Speed',
    'Accuracy',
    'Evasion',
    'Critical',
    'Critical Evasion'
]


class FireEmblemUnit(object):

    def __init__(self, identification_code):
        self.identification_code = identification_code
        self.is_dead = False
        self.stats_block = None
        self.battle_stats_block = None
        self.inventory = None


class FireEmblemJobUnit(FireEmblemUnit):
    pass


class FireEmblemCharacterUnit(FireEmblemJobUnit):
    pass


class FireEmblemPlayerCharacterUnit(FireEmblemCharacterUnit):
    pass


class AbstractBattleStatsArray(object):

    def __init__(self, battle_stats_list):
        self.battle_stats_list = battle_stats_list
        self.battle_stats = {}

    def validate_stat_list(self, ruleset):
        pass

    def compute_battle_stats(self, *args):
        """Leave to child classes"""
        raise NotImplementedError

    def set_keys(self):
        for key in self.battle_stats_list:
            self.battle_stats[key] = None


class StandardBattleStatsArray(AbstractBattleStatsArray):

    def __init__(self):
        AbstractBattleStatsArray.__init__(self, STANDARD_BATTLE_STATS_LIST)



    def compute_battle_stats(self, stat_array, equipped_weapon_stats, terrain_adjustments):
        pass

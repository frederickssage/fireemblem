"""Classes and functions related to FireEmblemBattles"""


class BaseFireEmblemBattle(object):

    def __init__(self, first_actor, second_actor, environment):
        self.initiator = first_actor
        self.responder = second_actor
        self.environment = environment

    def resolve(self):
        pass


class SpeedFireEmblemBattle(BaseFireEmblemBattle):

    def __init__(self, first_actor, second_actor, environment):
        BaseFireEmblemBattle.__init__(self, first_actor, second_actor, environment)

    def resolve(self):
        pass


class OneSidedFireEmblemBattle(BaseFireEmblemBattle):

    def __init__(self, first_actor, second_actor, environment):
        BaseFireEmblemBattle.__init__(self, first_actor, second_actor, environment)

    def resolve(self):
        pass
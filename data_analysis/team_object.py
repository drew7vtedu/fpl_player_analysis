class team(object):

    def __init__(self, id, goals_for, goals_against, xg, xga):
        self.id = id
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.xg = xg
        self.xga = xga

    def set_goals_for(self, gf):
        self.goals_for = gf

    def set_goals_against(self, ga):
        self.goals_against = ga

    def set_xg(self, xg):
        self.xg = xg

    def set_xga(self, xga):
        self.xga = xga

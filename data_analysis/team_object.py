class team(object):

    def __init__(self, id, goals_for, goals_against, xg, npxg, xga):
        self.id = id
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.xg = xg
        self.npxg = npxg
        self.xga = xga
        self.schedule_id = schedule_id

    def set_goals_for(self, gf):
        self.goals_for = gf

    def set_goals_against(self, ga):
        self.goals_against = ga

    def set_xg(self, xg):
        self.xg = xg

    def set_npxg(self, npxg):
        self.npxg = npxg

    def set_xga(self, xga):
        self.xga = xga

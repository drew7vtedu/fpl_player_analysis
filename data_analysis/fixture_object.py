
class fixture_obj(object):

    def __init__(self, home, home_goals, hxg, away, away_goals, axg, gameweek, postponed):
        self.home = home
        self.home_goals = home_goals
        self.hxg = hxg
        self.away = away
        self.away_goals = away_goals
        self.axg =axg
        self.gameweek = gameweek
        self.postponed = postponed

    def get_home(self):
        return self.home

    def get_home_goals(self):
        return self.home_goals

    def get_hxg(self):
        return self.hxg

    def get_away(self):
        return self.away

    def get_away_goals(self):
        return self.away_goals

    def get_axg(self):
        return self.axg

    def get_gameweek(self):
        return self.gameweek

    def get_postponed(self):
        return self.postponed

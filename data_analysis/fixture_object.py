
class fixture_obj(object):

    def __init__(self, home, hxg, away, axg, gameweek, postponed):
        self.home = home
        self.hxg = hxg
        self.away = away
        self.axg =axg
        self.gameweek = gameweek
        self.postponed = postponed

    def get_home(self):
        return self.home

    def get_hxg(self):
        return self.hxg

    def get_away(self):
        return self.away

    def get_axg(self):
        return self.axg

    def get_gameweek(self):
        return self.gameweek

    def get_postponed(self):
        return self.postponed

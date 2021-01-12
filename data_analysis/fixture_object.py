
class fixture_obj(object):

    def __init__(self, home, away, gameweek):
        self.home = home
        self.away = away
        self.gameweek = gameweek

    def get_home(self):
        return self.home

    def get_away(self):
        return self.away

    def get_gameweek(self):
        return self.gameweek

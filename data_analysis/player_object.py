class player_obj(object):

    def __init__(self, id, first_name, last_name, pls, cp, price, ly_mins, mins, team):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.points_last_season = pls
        self.current_points = cp
        self.price = price
        self.ly_minutes = ly_mins
        self.minutes = mins
        self.xg = 0
        self.xa = 0
        self.team_id = team

    def matches(self, first_name, last_name):
        return first_name == self.first_name and last_name == self.last_name

    '''
    last season data
    '''
    def set_pls(self, points_last_season):
        self.points_last_season = points_last_season

    def set_ly_minutes(self, mins):
        self.ly_minutes = mins

    '''
    current season data
    '''
    def set_points(self, points):
        self.current_points = points

    def set_minutes(self, mins):
        self.minutes = mins

    def get_price(self):
        return self.price

    def set_price(self, nPrice):
        self.price = nPrice

    def set_team(self, team):
        self.team_id = team

    def set_xg(self, xg):
        self.xg = xg

    def set_xa(self, xa):
        self.xa = xa


    def to_dict(self):
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "points_last_season": self.points_last_season,
                "current_points": self.current_points,
                "price": self.price,
                "ly_minutes": self.ly_minutes,
                "minutes": self.minutes,
                "xg": self.xg,
                "xa": self.xa,
                "team": self.team_id
            }

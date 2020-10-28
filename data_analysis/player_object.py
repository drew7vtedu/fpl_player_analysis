class player_obj(object):

    def __init__(self, first_name, last_name, pls, cp, price, ly_mins, mins, team):
        self.first_name = first_name
        self.last_name = last_name
        self.points_last_season = pls
        self.current_points = cp
        self.price = price
        self.ly_minutes = ly_mins
        self.ly_points_per_90 = 0
        self.ly_points_per_match = 0
        self.ly_points_per_match2 = 0
        self.ly_value_added_per_mil = 0
        self.minutes = mins
        self.points_per_90 = 0
        self.points_per_match = 0
        self.points_per_match_minus_starts= 0
        self.value_added_per_mil = 0
        self.team = team

    def matches(self, first_name, last_name):
        return first_name == self.first_name and last_name == self.last_name

    '''
    these metrics are based on data from the previous season because
    the current season is often too small a sample size to be reliable
    '''
    def set_pls(self, points_last_season):
        self.points_last_season = points_last_season

    def set_ly_minutes(self, mins):
        self.ly_minutes = mins

    def set_ly_points_per_90(self, pp90):
        self.ly_points_per_90 = pp90

    def set_ly_points_per_match(self, ppm):
        self.ly_points_per_match = ppm

    def set_ly_points_per_match2(self, ppm2):
        self.ly_points_per_match2 = ppm2

    def set_ly_value_added_per_mil(self, value_added):
        self.ly_value_added_per_mil = value_added

    '''
    these metrics are based on the current season
    '''
    def set_points(self, points):
        self.points_last_season = points_last_season

    def set_minutes(self, mins):
        self.minutes = mins

    def set_points_per_90(self, pp90):
        self.points_per_90 = pp90

    def set_points_per_match(self, ppm):
        self.points_per_match = ppm

    def set_points_per_match2(self, ppm2):
        self.points_per_match2 = ppm2

    def set_value_added_per_mil(self, value_added):
        self.value_added_per_mil = value_added

    def get_price(self):
        return self.price

    def set_team(self, team_string):
        self.team = team_string

    def to_dict(self):
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "points_last_season": self.points_last_season,
                "current_points": self.current_points,
                "price": self.price,
                "ly_minutes": self.ly_minutes,
                "ly_points_per_90": self.ly_points_per_90,
                "ly_points_per_match": self.ly_points_per_match,
                "ly_points_per_match2": self.ly_points_per_match2,
                "ly_value_added_per_mil": self.ly_value_added_per_mil,
                "minutes": self.minutes,
                "points_per_90": self.points_per_90,
                "points_per_match": self.points_per_match,
                "points_per_match2": self.points_per_match2,
                "value_added_per_mil": self.value_added_per_mil,
                "team": self.team
            }

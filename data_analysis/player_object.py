class player_obj(object):

    def __init__(self, id, first_name, last_name, games, starts, goals, assists, pens, xg, npxg, xa, tackles, tackles_won, pressures, pressure_regains, dribbles_completed, dribbles, team):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        # self.points_last_season = pls
        # self.current_points = cp
        # self.price = price
        # self.ly_minutes = ly_mins
        # self.minutes = mins
        self.games = games
        self.starts = starts
        self.goals = goals
        self.assists = assists
        self.penalty_goals = pens
        self.xg = xg
        self.npxg = npxg
        self.xa = xa
        self.tackles = tackles
        self.tackles_won = tackles_won
        self.pressures = pressures
        self.pressure_regains = pressure_regains
        self.dribbles_completed = dribbles_completed
        self.dribbles_attempted = dribbles
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

    def get_id(self):
        return self.id

    def set_points(self, points):
        self.current_points = points

    def get_points(self):
        return self.points

    def set_minutes(self, mins):
        self.minutes = mins

    def get_minutes(self):
        return self.minutes

    def get_price(self):
        return self.price

    def set_price(self, nPrice):
        self.price = nPrice

    '''
    sets the players team_id to the new integer corresponding
    to the correct team
    '''
    def set_team(self, team):
        self.team_id = team

    '''
    returns an integer representing the players team
    '''
    def get_team():
        return self.team_id

    def set_xg(self, xg):
        self.xg = xg

    def get_xg(self):
        return self.xg

    def set_xa(self, xa):
        self.xa = xa

    def get_xa(self):
        return self.xa


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

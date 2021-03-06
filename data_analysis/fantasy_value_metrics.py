# standardises returns, doesn't account for playing reduced minutes
def points_scored_per_90(points, minutes):
    if minutes == 0:
        return 0
    return (points / (minutes / 90))

# considers reduced mintutes but doesn't consider price
def points_scored_per_match(points, matches):
    if matches == 0:
        return 0
    return points / matches

# adds price into the equation unlike previous methods, data is skewed by appearance points
def points_scored_per_match_per_mil(points, matches, price):
    if price == 0:
        return 0
    return points_scored_per_match(points, matches) / price

# best available metric, eliminate base 2 points for appearance to get real difference per match between players
def value_added_per_mil(points, matches, price):
    if price == 0:
        return 0
    return (points_scored_per_match((points - (2 * matches)), matches) / price)

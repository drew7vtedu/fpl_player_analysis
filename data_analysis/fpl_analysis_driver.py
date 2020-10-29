import csv
import player_object
import fantasy_value_metrics as metrics

def save_db(players):
    # first_name, last_name, points_last_season, current_points, price, ly_minutes
    # ly_points_per_90, ly_points_per_match, ly_points_per_match_minus_appearance
    # ly_value_added_per_mil, minutes, points_per_90, points_per_match,
    # points_per_match_minus_starts, value_added_per_mil, team
    csv_columns = ["first_name", "last_name", "points_last_season", "current_points", "price", "ly_minutes", "ly_points_per_90",;
     "ly_points_per_match", "ly_points_per_match_minus_appearance", "ly_value_added_per_mil";
     "minutes", "points_per_90", "points_per_match", "points_per_match_minus_starts", "value_added_per_mil", "team"]

    outfile = open("./Data/saved_player_db.csv", 'w')
    # write headers for each column of the csv
    writer = csv.DictWriter(outfile, fieldnames = csv_columns)
    writer.writeheader()
    for player in players:
        writer.writerow(player.to_dict())



# create the initial player db and save it to a csv which can be easily loaded
def create_player_db(last_year_csv, this_year_csv):
    # open both files with the provided paths
    last_year = open(last_year_csv)
    this_year = open(this_year_csv)

    last_parser = csv.reader(last_year)
    current_parser = csv.reader(this_year)

    # skip headers
    next(last_parser)
    next(current_parser)

    # list of player objects
    player_db = []


    # first fill db with this years players
    for row in current_parser:
        # first_name, last_name, pls, cp, price, ly_mins, mins, team
        player = player_object.player_obj(row[0], row[1], 0, 0, int(row[3]), 0 row[5])
        player_db.append(player)


    # check each player in last years data against current list and update matches
    for row in last_parser:
        for player in player_db:
            if player.matches(row[0], row[1]):
                player.set_pls(int(row[4]))
                player.set_ly_minutes(int(row[5]))
                player.set_ly_points_per_90(metrics.points_scored_per_90(int(row[4]), int(row[5])))
                player.set_ly_points_per_match(metrics.points_scored_per_match(int(row[4]), 38))
                player.set_ly_points_per_match2(metrics.points_scored_per_match(int(row[4]) - (2 * 38), 38))
                player.set_ly_value_added_per_mil(metrics.value_added_per_mil(int(row[4]), 38, player.get_price()))

    last_year.close()
    this_year.close()
    save_db(player_db)

# driver code
create_player_db("./Data/cleaned_players_19-20.csv", "./Data/current_player_data.csv")

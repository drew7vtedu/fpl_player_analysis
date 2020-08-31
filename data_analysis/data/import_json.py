import pandas as pd
import json
import csv
import requests
from pandas.io.json import json_normalize


# Define a function to get info from the FPL API and save to the specified file_path
# It might be a good idea to navigate to the link in a browser to get an idea of what the data looks like
def get_json(file_path):
    r = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    jsonResponse = r.json()
    with open(file_path, 'w') as outfile:
        json.dump(jsonResponse, outfile)

# Run the function and choose where to save the json file
get_json('player_data.json')

# open the json file containing your data
json_data = open('player_data.json', encoding='utf-8')

# get a string (text) representation of the entire contents of the file
data = json_data.read()

# convert text to a python dictionary of key-value pairs
data_dict = json.JSONDecoder().decode(data)

# done with json input file
json_data.close()

players = data_dict["elements"]

# we will fill this list with data and convert it to csv later
csv_player_list = []
# column headers for when we convert to csv
csv_columns = ["first_name", "last_name", "current_points", "price", "minutes"]

for player in players:
    # create dict to fill with each player's data
    temp_player_dict = {}
    # fill temp dict with desired data
    temp_player_dict["first_name"] = player["first_name"]
    temp_player_dict["last_name"] = player["second_name"]
    temp_player_dict["current_points"] = int(player["total_points"])
    temp_player_dict["price"] = int(player["now_cost"])
    temp_player_dict["minutes"] = int(player["minutes"])
    # add data to list to become csv
    csv_player_list.append(temp_player_dict)

# name of the csv file to write to
csv_out = "current_player_data.csv"
try:
    with open(csv_out, 'w') as csvfile:
        # write headers for each column of the csv
        writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
        writer.writeheader()
        for player in csv_player_list:
            writer.writerow(player)
except IOError:
    print("IOError while opening csv file")
# close out file
csvfile.close()

# data I can get from each player:
# 'chance_of_playing_next_round', 'chance_of_playing_this_round', 'code', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'dreamteam_count', 'element_type', 'ep_next', 'ep_this', 'event_points', 'first_name', 'form', 'id', 'in_dreamteam', 'news', 'news_added', 'now_cost', 'photo', 'points_per_game', 'second_name', 'selected_by_percent', 'special', 'squad_number', 'status', 'team', 'team_code', 'total_points', 'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event', 'value_form', 'value_season', 'web_name', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index', 'influence_rank', 'influence_rank_type', 'creativity_rank', 'creativity_rank_type', 'threat_rank', 'threat_rank_type', 'ict_index_rank', 'ict_index_rank_type'

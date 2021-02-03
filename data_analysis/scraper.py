import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv
from data_analysis import team_object as to
from data_analysis import fixture_object as fo
from data_analysis import player_object as po


# this is an array containing all team names in the league this year, will need to be updated each season. Team id is its position in the array + 1
teams = ["Arsenal", "Aston Villa", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leicester City", "Leeds United", "Liverpool", "Manchester City", "Manchester Utd", "Newcastle Utd", "Sheffield Utd", "Southampton", "Tottenham", "West Brom", "West Ham", "Wolves"]


'''
turn a dictionary containing team data into a team object. We assume the id is in string form
because that's how we get it from fbref
'''
def team_from_dict(team_dict):
    id = teams.index(team_dict["squad"]) + 1
    gf = team_dict["goals_for"]
    ga = team_dict["goals_against"]
    xg = team_dict["xg_for"]
    xga = team_dict["xg_against"]
    return to.team(id, gf, ga, xg, xga)


'''
turn a dictionary containing fixture data into a fixture object
'''
def fixture_from_dict(fd):
    home = teams.index(fd["squad_a"]) + 1
    home_goals = fd["home_goals"]
    hxg = fd["xg_a"]
    away = teams.index(fd["squad_b"]) + 1
    away_goals = fd["away_goals"]
    axg = fd["xg_b"]
    gameweek = fd["gameweek"]
    postponed = fd["postponed"]
    return fo.fixture_obj(home, home_goals, hxg, away, away_goals, axg, gameweek, postponed)

'''
turn a dictionary containing player data into a player object
'''
def player_from_dict(pd):
    if "id" not in pd:
        return None
    id = pd["id"]
    name = pd["name"]
    split_name = name.split(' ', 1)
    if len(split_name) < 2:
        last_name = name
        first_name = ''
    else:
        first_name = split_name[0]
        last_name = split_name[1]
    games = pd["games"]
    starts = pd["games_starts"]
    goals = pd["goals"]
    if goals == '':
        goals = None
    assists = pd["assists"]
    if assists == '':
        assists = None
    penalties = pd["pens_made"]
    if penalties == '':
        penalties = None
    xg = pd["xg"]
    if xg == '':
        xg = None
    npxg = pd["npxg"]
    if npxg == '':
        npxg = None
    xa = pd["xa"]
    if xa == '':
        xa = None
    tackles_attempted = pd["tackles"]
    if tackles_attempted == '':
        tackles_attempted = None
    tackles_won = pd["tackles_won"]
    if tackles_won == '':
        tackles_won = None
    pressures = pd["pressures"]
    if pressures == '':
        pressures = None
    pressure_regains = pd["pressure_regains"]
    if pressure_regains == '':
        pressure_regains = None
    dribbles_completed = pd["dribbles_completed"]
    if dribbles_completed == '':
        dribbles_completed = None
    dribbles_attempted = pd["dribbles"]
    if dribbles_attempted == '':
        dribbles_attempted = None
    team_id = teams.index(pd["team"]) + 1
    return po.player_obj(id, first_name, last_name, games, starts, goals, assists, penalties, xg, npxg, xa, tackles_attempted, tackles_won, pressures, pressure_regains, dribbles_completed, dribbles_attempted, team_id)



def get_teams():
    # fbref url to premier league stats
    res = requests.get("https://fbref.com/en/comps/9/Premier-League-Stats")
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("",res.text),'lxml')

    all_tables = soup.findAll("tbody")
    teams_table = all_tables[0]
    squad_standard_table = all_tables[1]

    #Parse league_table
    pre_df_team = dict()
    teams_list = []
    features_wanted_team = {"goals_for", "goals_against", "xg_for", "xg_against"}
    rows_team = teams_table.find_all('tr')
    for row in rows_team:
        team_dict = dict()
        if(row.find('th',{"scope":"row"}) != None):
            name = row.find('td',{"data-stat":"squad"}).text.strip().encode().decode("utf-8")
            if 'squad' in pre_df_team:
                pre_df_team['squad'].append(name)
            else:
                pre_df_team['squad'] = [name]

            # was getting key errors before I seperated these, TODO: comment this better
            if 'squad' in team_dict:
                team_dict['squad'].append(name)
            else:
                team_dict['squad'] = name

            for f in features_wanted_team:
                cell = row.find("td",{"data-stat": f})
                a = cell.text.strip().encode()
                text=a.decode("utf-8")
                if f in pre_df_team:
                    pre_df_team[f].append(text)
                else:
                    pre_df_team[f] = [text]


                if f in team_dict:
                    team_dict[f].append(text)
                else:
                    team_dict[f] = text
        teams_list.append(team_dict)

    df_team = pd.DataFrame.from_dict(pre_df_team)
    df_team.to_csv("data/test_scrape_data.csv")
    return teams_list


'''
scrape fixtures from fbref
'''
def get_fixtures():
    # fbref url to premier league fixtures
    res = requests.get("https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures")
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("",res.text),'lxml')

    # this page contains a single table with all 38 gameweeks
    table = soup.findAll("tbody")

    # a in data-stats refers to home, b to away
    features_wanted_fixture = {"squad_a", "xg_a", "xg_b", "squad_b", "notes"}
    fixture_list = []
    rows_fixture = table[0].find_all('tr')
    for row in rows_fixture:

        fixture_dict = dict()

        if(row.find('th',{"scope":"row"}) != None):
            #gameweek requires special treatment
            week = row.find('th',{"data-stat":"gameweek"}).text.strip().encode().decode("utf-8")
            # skip blank rows
            if week != "":
                fixture_dict["gameweek"] = week

                # score needs to be separated into home and away goals
                score_cell = row.find("td",{"data-stat": "score"})
                score_a = score_cell.text.strip().encode()
                score = score_a.decode("utf-8")
                # it was a nightmare figuring out that the score is seperated by an em dash not an en dash
                split_score = score.split('–')
                # handle null values for score
                if len(split_score) > 1:
                    fixture_dict["home_goals"] = split_score[0]
                    fixture_dict["away_goals"] = split_score[1]
                else:
                    fixture_dict["home_goals"] = None
                    fixture_dict["away_goals"] = None

                for f in features_wanted_fixture:
                    cell = row.find("td",{"data-stat": f})
                    a = cell.text.strip().encode()
                    text=a.decode("utf-8")
                    if text != '' and f != "notes":
                        fixture_dict[f] = text
                    elif f == "notes" and text != '':
                        fixture_dict["postponed"] = True
                    elif f == "notes":
                        fixture_dict["postponed"] = False
                    else:
                        fixture_dict[f] = None
        if fixture_dict != {}:
            fixture_list.append(fixture_dict)

    return fixture_list


'''
takes a path to a csv file containing urls for each team's player data
scrapes each url and returns an array of player objects
these objects will be missing some data which will be provided by
the premier league api (fantasy price for example)
'''
def get_players(url_csv):
    file = open(url_csv)
    parser = csv.reader(file)
    player_list = []
    # skip header
    next(parser)
    for row in parser:
        team_list = []
        res = requests.get(row[1])


        ## The next two lines get around the issue with comments breaking the parsing.
        comm = re.compile("<!--|-->")
        soup = BeautifulSoup(comm.sub("",res.text),'lxml')

        all_tables = soup.findAll("tbody")

        rows_standard_table = all_tables[0].find_all('tr')
        rows_defensive_actions = all_tables[8].find_all('tr')
        rows_possession = all_tables[9].find_all('tr')

        features_wanted_standard = {"games", "games_starts", "goals", "assists", "pens_made", "xg", "npxg", "xa"}
        for srow in rows_standard_table:
            player_dict = dict()
            player_dict["team"] = row[0]
            # name requires special attention
            name_cell = srow.find("th", {"data-stat": "player"})
            if name_cell != None:
                name_a = name_cell.text.strip().encode()
                name = name_a.decode("utf-8")
                player_dict["name"] = name
                for f in features_wanted_standard:
                    cell = srow.find("td",{"data-stat": f})
                    a = cell.text.strip().encode()
                    text=a.decode("utf-8")
                    player_dict[f] = text

                team_list.append(player_dict)
        features_wanted_defense = {"tackles", "tackles_won", "pressures", "pressure_regains"}
        # players are in the same order in each table so we use that to assign these stats to
        # the correct player
        i = 0
        for drow in rows_defensive_actions:
            # temporary id until I scrape from prem website
            team_list[i]["id"] = i + (30 * teams.index(row[0]))
            for f in features_wanted_defense:
                cell = drow.find("td",{"data-stat": f})
                if cell != None:
                    a = cell.text.strip().encode()
                    text=a.decode("utf-8")
                    team_list[i][f] = text
            i += 1

        i = 0
        features_wanted_possession = {"dribbles_completed", "dribbles"}
        for prow in rows_possession:
            for f in features_wanted_possession:
                cell = prow.find("td",{"data-stat": f})
                if cell != None:
                    a = cell.text.strip().encode()
                    text=a.decode("utf-8")
                    team_list[i][f] = text
            i += 1
        player_list += team_list


    file.close()
    return player_list

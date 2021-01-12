import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv
from ddata_analysis import team_object as to


# this is an array containing all team names in the league this year, will need to be updated each season. Team id is its position in the array + 1
teams = ["Arsenal", "Aston Villa", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leicester City", "Leeds United", "Liverpool", "Manchester City", "Manchester Utd", "Newcastle Utd", "Sheffield Utd", "Southampton", "Tottenham", "West Brom", "West Ham", "Wolves"]


'''
turn a dictionary containing team data into a team object. We assume the id is in string form
because that's how we get it from fbref
'''
def team_from_dict(team_dict):
    id = teams.index(team_dict["Squad"]) + 1
    gf = team_dict["goals_for"]
    ga = team_dict["goals_against"]
    xg = team_dict["xg_for"]
    xga = team_dict["xg_against"]
    return to.team(id, gf, ga, xg, xga)

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
    features_wanted_team = {"Squad", "goals_for", "goals_against", "xg_for", "xg_against"}
    rows_team = teams_table.find_all('tr')
    for row in rows_team:
        team_dict = dict()
        if(row.find('th',{"scope":"row"}) != None):

            for f in features_wanted_team:
                cell = row.find("td",{"data-stat": f})
                a = cell.text.strip().encode()
                text=a.decode("utf-8")
                if f in pre_df_team:
                    pre_df_team[f].append(text)
                    team_dict[f].append(text)
                else:
                    pre_df_team[f] = [text]
                    team_dict[f] = [text]
        teams_list.append(team_dict)

    df_team = pd.DataFrame.from_dict(pre_df_team)
    df_team.to_csv("data/test_scrape_data.csv")
    return teams_list

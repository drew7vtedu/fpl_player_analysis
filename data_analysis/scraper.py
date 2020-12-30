import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv

## hard coded url for now, pls fix
res = requests.get("https://fbref.com/en/comps/9/Premier-League-Stats")
## The next two lines get around the issue with comments breaking the parsing.
comm = re.compile("<!--|-->")
soup = BeautifulSoup(comm.sub("",res.text),'lxml')

all_tables = soup.findAll("tbody")
teams_table = all_tables[0]
squad_standard_table = all_tables[1]

#Parse league_table
pre_df_team = dict()
features_wanted_team = {"goals_for", "goals_against", "xg_for", "xg_against"}
rows_team = teams_table.find_all('tr')
for row in rows_team:
    if(row.find('th',{"scope":"row"}) != None):

        for f in features_wanted_team:
            cell = row.find("td",{"data-stat": f})
            a = cell.text.strip().encode()
            text=a.decode("utf-8")
            if f in pre_df_team:
                pre_df_team[f].append(text)
            else:
                pre_df_team[f] = [text]
df_team = pd.DataFrame.from_dict(pre_df_team)
df_team.to_csv("data/test_scrape_data.csv")

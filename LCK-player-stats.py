import pandas as pd
import requests
from datetime import datetime

# note api key 
## !! HIDE API WHEN SHARING !! ##
#api_key = ?

# get summoner csv to retrieve info
# csv_path1 = path_to_player_account_csv
account_df = pd.read_csv(csv_path1, delimiter=',')

# add stat csv to fill data in. Columns : date,player,team,role,region,LP,wins,losses,games,winrate. Can leave all columns empty
# csv_path2 = path_to_player_stat_csv
stats_df = pd.read_csv(csv_path2, delimiter=',')
player_names = stats_df['player'].tolist()

# create function to retrieve player stats from API
def get_player_stats(player_name):
    # get Riot API
    league_api_base = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"
    league_api = f"{league_api_base}{summonerid}?api_key={api_key}"
        
    # make API call for the stats
    response = requests.get(league_api)
    
    # check if the API call is successfull (code 200)
    if response.status_code == 200:
        player_stats_list = response.json()
        
        # check if the list is not empty
        if player_stats_list:
            # extract the first dictionary from the list
            player_stats = player_stats_list[0]
            
            # extract required stats from the dictionary
            league_points = player_stats.get('leaguePoints', None)
            wins = player_stats.get('wins', None)
            losses = player_stats.get('losses', None)
            tier = player_stats.get('tier', None)
            rank = player_stats.get('rank', None)
            
            return league_points, wins, losses, tier, rank
        else:
            print(f"No stats found for {player_name}")
            return None
       
    else:
        print(f"Failed to fetch summonerID for {player_name} from the API. Status code: {response.status_code}")
        return None

# create function for LP number based on tier
def get_LP(tier, rank, league_points):
    if tier == 'DIAMOND' and rank == 'IV':
        LP = league_points - 400
    elif tier == 'DIAMOND' and rank == 'III':
        LP = league_points - 300
    elif tier == 'DIAMOND' and rank == 'II':
        LP = league_points - 200
    elif tier == 'DIAMOND' and rank == 'I':
        LP = league_points - 100
    else:
        LP = league_points
    
    return LP
    
# current date
current_date = datetime.now().strftime('%Y-%m-%d')

# iterate definition for each player
for index, row in account_df.iterrows():
    summonerid = row['summonerID']
    player_name = row['player']
    team_name = row['team']
    role_name = row['role']
    region_name = row['region']
        
    player_stats = get_player_stats(summonerid)
    
    if player_stats is not None:
        league_points, wins, losses, tier, rank = player_stats
        
        # get actual LP number based on tier (Master 0LP is the standard)
        LP = get_LP(tier, rank, league_points)
        
        # calculate number of games and winrate
        games = wins + losses
        winrate = "{:.2f}%".format((wins / games) * 100) if games > 0 else "0.00%"
                
        new_row = {'date': current_date, 'player': player_name, 'team': team_name, 'role': role_name, 'region': region_name, 'LP': LP, 'wins': wins, 'losses': losses, 'games': games, 'winrate': winrate }
        stats_df = pd.concat([stats_df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        print(f"No stats found for {player_name}")

# check dataframe before adding to CSV (optional) 
print(stats_df)

# add values back to the csv file
stats_df.to_csv(csv_path2, index=False)

# add new CSV to put daily stats. Columns : date,player,team,role,region,LP,wins,losses,winrate,games. Leave empty
# csv_path3 = path_to_daily_stats_CSV
daily_stats_df = pd.read_csv(csv_path3, delimiter=',')

# put daily data into the dataframe we just created
stats_df['date'] = pd.to_datetime(stats_df['date'])
daily_data = stats_df.loc[stats_df['date'] == current_date]
daily_stats_df = pd.concat([daily_stats_df, daily_data], ignore_index=True)

# check dataframe before adding to CSV (optional) 
print(daily_stats_df)

# add values to csv file
daily_stats_df.to_csv(csv_path3, index=False)

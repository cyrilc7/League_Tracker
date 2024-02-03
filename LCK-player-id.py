import pandas as pd
import requests
from dotenv import load_dotenv

# get API_KEY
load_dotenv()
api_key = os.getenv("api_key")

# open  player csv file with player, team, role, region, gamename, tagline, puuid (empty), summonerid(empty)
csv_path = r"data\LCK-players-24.csv"
df = pd.read_csv(csv_path, delimiter=',')

# get Riot API to query the puuid of the players
account_api_base = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"

# iterate search for each row in the dataframe
for index, row in df.iterrows():
    gamename = row['gamename']
    tagline = row ['tagline']
                   
    # construct the Riot API URL
    account_api = f"{account_api_base}{gamename}/{tagline}?api_key={api_key}"
        
    # make API call for the puuid
    response = requests.get(account_api)
    
    # check if the API call is successfull (code 200)
    if response.status_code == 200:
        puuid = response.json().get('puuid', None)
        
        # update the dataframe with puuid
        df.at[index, 'puuid'] = puuid
        
    else:
         print(f"Failed to fetch puuid for {gamename} {tagline} from the API. Status code: {response.status_code}")
         
# get Riot API to query the summonerid of the players
summoner_api_base = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"

# iterate search for each row in the dataframe
for index, row in df.iterrows():
    puuid = row['puuid']
                   
    # construct the Riot API URL
    summoner_api = f"{summoner_api_base}{puuid}?api_key={api_key}"
        
    # make API call for the summoner ID
    response = requests.get(summoner_api)
    
    # check if the API call is successfull (code 200)
    if response.status_code == 200:
        summonerid = response.json().get('id', None)
        
        # update the dataframe with puuid
        df.at[index, 'summonerID'] = summonerid
        
    else:
         print(f"Failed to fetch summonerID for {puuid} from the API. Status code: {response.status_code}")
         
print(df)
# save dataframe back to the csv file
df.to_csv(csv_path, index=False)

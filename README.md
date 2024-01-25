This project is a SoloQ Tracker for pro players in the LCK.
It shows the evolution of their performance in soloQ with different stats.

The stats are acquired by querying RiotAPI.
You will need an API Key. 
!! API Keys are individual and should not be shared !!
To get your API Key :

    * Visit https://developer.riotgames.com/
    * Log in
    * You can either use daily "Development API Key" that you need to refresh every day
        or
    * You can click on "Register Product" to ask for a permanent API Key

Before starting the project, I created a CSV with the following columns:

    * player, team, region, role, gamename, tagline, puuid, summonerID
    * only puuid and summonerID columns are left empty
    * You can get gamenames and taglines by visiting https://www.deeplol.gg/

All CSV are stored in "data" folder

    * player's account CSV to store names, puuid and summonerID
    * player's stats CSV to store all the stats everyday for each player
    * player's daily stats to store data of all player of the day

For the Rank and Tier, the standard point (0 point) is Master 0LP. Diamond rank will be below 0
The lowest possible elo is Diamond IV 0LP

You can visualize the project by visiting https://lookerstudio.google.com/reporting/a6f70368-1a33-4118-be27-f078c9777f42
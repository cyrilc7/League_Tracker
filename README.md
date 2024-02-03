# LCK SoloQ TRACKER

![Dashboard Image](./Dashboard.png)

## Introduction

Welcome to the LCK Solo Queue Tracker! This project aims to provide insights into the solo queue performances of professional League of Legends players participating in the LCK (League of Legends Champions Korea).

### *What is Solo Queue?*

Solo queue is the standard matchmaking mode in League of Legends where individual players compete against others to climb the ranked ladder. It's a platform for players to showcase their individual skills and test their strategies in a competitive environment.

### *What is LCK?*

The LCK (League of Legends Champions Korea) is the premier professional league in South Korea, featuring top-tier teams and players. LCK is known for its high level of competition and has produced some of the world's most skilled and renowned players.

## Features

- **Performance Evolution:** Explore historical data to identify trends, track improvements, and gain insights into player performances over time
- **Daily Statistics:** View daily statistics of the players' performance
- **Filters:** Compare and track the performance of any players with tailored filters (player, team, role etc.)

## Inspiration

Being a huge T1 (team operating in the LCK, 4 times world champions) and data fan myself, I always loved to check players SoloQ performance to get insights on the players' current form, see how next week's opponents are performing, but also check if there is a relationship between pro circuit performance and SoloQ performance.
I decided to make this tracker to automate this process and share it to anyone interested in League of Legends SoloQ or pro circuit. It is easily readable and understandable for anyone regardless of their knowledge in the game.


## Project Information

### *Process*

I completed the process through the following steps:

* Fetched all the players' gamename through [deeplol.gg](https://www.deeplol.gg/)
* Queried with RiotAPI their account ID and summonerID in order to get their daily stats
* Queried with RiotAPI the daily statistics and automatically integrate them in a CSV file for visualization
* Processed Data Visualization with [Tableau](https://public.tableau.com/views/LCKSoloQTracker/Tableaudebord2?:language=fr-FR&publish=yes&:display_count=n&:origin=viz_share_link) 

### *Rank and Tier System*

For the Rank and Tier, the standard point (0 point) is Master 0LP. Diamond rank will be below 0.
The lowest possible elo is Diamond IV 0LP.

## Sources

* Gamenames : [deeplol.gg](https://www.deeplol.gg/)
* Players' data : [Riot Developer](https://developer.riotgames.com)

## Credits and References

This process would not have been possible without RiotAPI and Deeplol.


## End Result
You can visualize the project by visiting my [Tableau Dashboard](https://public.tableau.com/views/LCKSoloQTracker/Tableaudebord2?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

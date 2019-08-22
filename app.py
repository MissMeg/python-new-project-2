# Code written by Megan Amendola

# Import player data
from constants import TEAMS, PLAYERS


# Clean the player data
def clean_player_data(PLAYERS):
    # List of player data to use for organizing teams
    cleaned_players = []
    # Loop through players to clean data
    for player in PLAYERS:
        # Create holder for the data
        add_player_data = {}
        # Add player name
        add_player_data["name"] = player["name"]
        # Clean the guardian field -> split up into a list
        if "and" in player["guardians"]:
            add_player_data["guardians"] = player["guardians"].split(' and ')
        else:
            add_player_data["guardians"] = [player["guardians"]]
        # Clean experience -> Bool
        if player["experience"] == 'YES':
            add_player_data["experience"] = True
        else:
            add_player_data["experience"] = False
        # Clean height -> Int
        add_player_data["height"] = int(player['height'].split(' ')[0])
        cleaned_players.append(add_player_data)
    return cleaned_players


# Setup teams from file
def prep_teams(teams):
    team_prep = []
    for team in teams:
        team_prep.append({"team": team, "players": [], "number_of_players": 0})
    return team_prep


# Balance the players across the teams
# Equal experience levels on teams
#   Example: [{"team":"Panthers", "players": [{},{},{}]}]
def balance_teams(players, teams):
    pass


# Display the stats:
#   Team name
#   Total players on team
#   Player names separated by commas
#   Number of inexperienced players
#   Number of experienced players
#   Average height of the team
#   Guardians of all the players -> comma separated string

if __name__ == "__main__":
    # Console readability matters
    balance_teams(clean_player_data(PLAYERS), prep_teams(TEAMS))

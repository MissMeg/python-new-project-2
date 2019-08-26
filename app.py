# Code written by Megan Amendola

# Import player data
from constants import TEAMS, PLAYERS
# import only system from os
from os import system, name
import math


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Clean the player data
def clean_player_data(PLAYERS):
    # List of player data to use for organizing teams
    exp_players = []
    inexp_players = []
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
        if add_player_data['experience'] is True:
            exp_players.append(add_player_data)
        else:
            inexp_players.append(add_player_data)
    return exp_players, inexp_players


# Setup data from file
def prep_teams(teams):
    team_prep = []
    for team in teams:
        team_prep.append({"team": team, "players": []})
    return team_prep


# Balance the players across the teams
# Equal experience levels on teams
def balance_teams(players, teams):
    count = 0
    # groups = exp and inexp lists
    for group in players:
        # each player within each list
        for player in group:
            # add player to team
            teams[count]['players'].append(player)
            # add to count so the next player
            # is added to the next team
            count += 1
            # reset count
            if count == len(teams):
                count = 0
    return teams


# Display the stats:
def display_stats(team):
    # Team name
    print('\n{} Stats'.format(team['team']))
    print('\n-------------------')
    # Total players on team
    print('\nNumber of Players: {}'.format(len(team['players'])))
    # Number of experienced players
    count_exp = 0
    for player in team['players']:
        if player['experience'] is True:
            count_exp += 1
    print('\nNumber of Experienced players: {}'.format(count_exp))
    # Number of inexperienced players
    print('\nNumber of Inexperienced players: {}'
          .format(len(team['players']) - count_exp))
    # Average height of the team
    height = []
    for player in team['players']:
        height.append(player['height'])
    average_height = math.floor(sum(height) / len(height))
    print("\nAverage Height: {} inches".format(average_height))
    # Player names separated by commas
    player_names = []
    for player in team['players']:
        player_names.append(player['name'])
    print('\nPlayers:')
    print('\n{}'.format(', '.join(player_names)))
    # Guardians of all the players -> comma separated string
    guardian_names = []
    for player in team['players']:
        for guardian in player['guardians']:
            guardian_names.append(guardian)
    print('\nGuardians:')
    print('\n{}'.format(', '.join(guardian_names)))


if __name__ == "__main__":
    # Console readability matters
    # set variable for the program
    displaying_data = True

    while displaying_data:
        clear()
        # get data to display
        data = balance_teams(clean_player_data(PLAYERS), prep_teams(TEAMS))
        # print start menu
        print('\nTeam Stats Tool')
        print('\n---- MENU ----')
        print('\nChoose one of the following options:')
        count = 1
        for team in data:
            print('\n{}) Display {} stats'.format(count, team['team']))
            count += 1
        print('\n{}) Quit\n'.format(len(data) + 1))
        # make sure their choice is a number
        try:
            response = int(input('Your choice: '))
        except ValueError:
            clear()
            input('\nYou must input a number. Press "Enter" to try again.')
        else:
            if response == (len(data) + 1):
                displaying_data = False
            elif response <= len(data):
                display_stats(data[response - 1])
                input('\nPress "Enter" to return to the main menu.')
            else:
                clear()
                input(
                    '\nThat number is not valid. Press "Enter" to try again.'
                )

# Code written by Megan Amendola

from constants import TEAMS, PLAYERS
from os import system, name
import math
from typing import List, Dict


def clear_screen():
    """Clears the terminal window for a better user experience"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def clean_player_data(PLAYERS: List[dict]) -> List[dict]:
    """
    Cleans the player data.
    - player['name'] = str
    - player['guardians'] = List[str]
    - player['experience'] = bool
    - player['height'] = int
    """
    # Split player data by exp to create even teams
    exp_players = []  # type: List[dict]
    inexp_players = []  # type: List[dict]
    for player in PLAYERS:
        add_player_data = {}  # type: dict
        add_player_data["name"] = player["name"]
        if "and" in player["guardians"]:
            add_player_data["guardians"] = player["guardians"].split(' and ')
        else:
            add_player_data["guardians"] = [player["guardians"]]
        if player["experience"] == 'YES':
            add_player_data["experience"] = True
        else:
            add_player_data["experience"] = False
        add_player_data["height"] = int(player['height'].split(' ')[0])
        if add_player_data['experience'] is True:
            exp_players.append(add_player_data)
        else:
            inexp_players.append(add_player_data)
    return exp_players, inexp_players


def prep_teams(teams: List[str]) -> List[dict]:
    """Sets up each team as a dict and returns a list of dicts"""
    team_prep = []  # type: List[dict]
    for team in teams:
        team_prep.append({"team": team, "players": []})
    return team_prep


def balance_teams(players: List[dict], teams: List[dict]) -> List[dict]:
    """Organizes players into equal teams and returns list of dicts"""
    count = 0
    for group in players:
        for player in group:
            teams[count]['players'].append(player)
            # add to count so the next player
            # is added to the next team
            count += 1
            if count == len(teams):
                count = 0
    return teams


def display_stats(team: List[dict]):
    """Prints out the team's stats"""
    # Team name
    print('\n{} Stats'.format(team['team']))
    print('\n-------------------')
    # Total players on team
    print('\nNumber of Players: {}'.format(len(team['players'])))
    # Number of experienced players
    count_exp = 0  # type: int
    for player in team['players']:
        if player['experience'] is True:
            count_exp += 1
    print('\nNumber of Experienced players: {}'.format(count_exp))
    # Number of inexperienced players
    print('\nNumber of Inexperienced players: {}'
          .format(len(team['players']) - count_exp))
    # Average height of the team
    height = []  # type: List[int]
    for player in team['players']:
        height.append(player['height'])
    average_height = math.floor(sum(height) / len(height))
    print("\nAverage Height: {} inches".format(average_height))
    # Player names separated by commas
    player_names = []  # type: List[str]
    for player in team['players']:
        player_names.append(player['name'])
    print('\nPlayers:')
    print('\n{}'.format(', '.join(player_names)))
    # Guardians of all the players -> comma separated string
    guardian_names = []  # type: List[str]
    for player in team['players']:
        for guardian in player['guardians']:
            guardian_names.append(guardian)
    print('\nGuardians:')
    print('\n{}'.format(', '.join(guardian_names)))


if __name__ == "__main__":
    displaying_data = True

    while displaying_data:
        clear_screen()
        team_data = balance_teams(clean_player_data(PLAYERS),
                                  prep_teams(TEAMS))  # type: List[dict]
        # start menu
        print('\nTeam Stats Tool')
        print('\n---- MENU ----')
        print('\nChoose one of the following options:')
        count = 1  # type: int
        for team in team_data:
            print('\n{}) Display {} stats'.format(count, team['team']))
            count += 1
        print('\n{}) Quit\n'.format(len(team_data) + 1))
        # check choice
        try:
            response = int(input('Your choice: '))
        except ValueError:
            clear_screen()
            input('\nYou must input a number. Press "Enter" to try again.')
        else:
            if response == (len(team_data) + 1):
                displaying_data = False
            elif response <= len(team_data):
                display_stats(team_data[response - 1])
                input('\nPress "Enter" to return to the main menu.')
            else:
                clear_screen()
                input(
                    '\nThat number is not valid. Press "Enter" to try again.'
                )

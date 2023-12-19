# df_players est une dataframe, l idex est composé des noms des joueurs, et en colonne il y a  "Password", "Score",
import pandas as pd


def create_an_account(df_players):
    username = str(input("What is your username?"))
    while username in df_players.keys:
        username = str(input("This username is already taken! Try an other one"))
    password = str(input("What is your password?"))
    check_password = str(input("Please enter your password again"))
    while password != check_password:
        print("Your passwords are different")
        check_password = str(input("Please enter your password again"))
    df_players.loc[username] = [password, 100]
    return df_players


def create_an_event(df_events):
    sport = str(input("What is the sport of the game your want to add?"))
    team_1 = str(input("Who is the first team playing?"))
    team_2 = str(input("Who is the opponent?"))
    cote_team_1 = str(input("What are the odds of", team_1, "of winning?"))
    cote_team_2 = str(input("What are the odds of", team_2, "of winning?"))
    cote_draw = str(input("What are the odds of a draw?"))
    event_name = sport + "/" + team_1 + "versus" + team_2
    df_events[len(df_events)] = [event_name]

# df_players est une dataframe, l idex est composé des noms des joueurs, et en colonne il y a  "Password", "Money",
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

# %% Import library
import pandas as pd
import requests
import json
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

# %%


def search():

    # Input info

    n = input('Type 1 for FC search \nType 2 for player search.')
    server, name = input('Please enter server name.'), input(
        'Please enter FC/player name.')

    # FC search

    if n == '1':
        try:
            result = requests.get(
                f'https://xivapi.com/freecompany/search?name={name}&server={server}').json()
            fc_id = int(result["Results"][0]["ID"])
            fc_info = requests.get(
                f'https://xivapi.com/freecompany/{fc_id}?data=FCM').json()
            table = pd.DataFrame(zip(*[(i['Name'], i['ID'], i['Rank'])
                                       for i in fc_info['FreeCompanyMembers']])).T
            table.columns = ['Name', 'ID', 'Rank']
            return table
        except:
            return 'Error'

    # Player search

    elif n == '2':
        try:
            result = requests.get(
                f'https://xivapi.com/character/search?name={name}&server={server}').json()
            player_id = int(result['Results'][0]['ID'])
            player_info = requests.get(
                f'https://xivapi.com/character/{player_id}').json()
            jobs = [i['Name'] for i in player_info['Character']['ClassJobs']]
            levels = [j['Level']
                      for j in player_info['Character']['ClassJobs']]
            table = pd.DataFrame(jobs, levels)
            table.columns = ['Jobs']
            return table
        except:
            return 'Error'

    # Error

    else:
        print('Enter a correct number.')


search()
# %%

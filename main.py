# %%

# Documentation :

# %%
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# %%


def search():

    n, server, name = input('Type 1 for FC search \n Type 2 for player search.'), input(
        'Please enter server name.'), input('Please enter player/FC name.')

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
            return table
        except:
            return 'Error'
    else:
        print('Error')
        pass


search()
# %%

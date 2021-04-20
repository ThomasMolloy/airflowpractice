import configparser
import requests
import json
from datetime import datetime
import os


def get_mma_data():

    '''
    Obtain API key and make api call and then dump data into json file
    '''
    cfg = configparser.ConfigParser()
    cfg.read('mmadata.cfg')

    api_key = cfg.get('KEYS', 'api_key')

    fighter_data_url = 'https://fly.sportsdata.io/v3/mma/scores/json/Fighters'
    params = dict(key=api_key)

    response = requests.get(fighter_data_url, params)

    if response.status_code == 200:
        json_data = response.json()
        file_name = 'FighterData_' + str(datetime.now().date()) + '.json'
        dir_name = os.path.join(os.path.dirname(__file__), 'data', file_name)

        with open(dir_name, 'w') as output:
            json.dump(json_data, output)
    
    else:
        print('API Call Error!') 

if __name__ == "__main__":
    get_mma_data()
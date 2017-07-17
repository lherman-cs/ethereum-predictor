from json import loads
from os.path import join, dirname

import requests


def collect_data(filename='history.csv'):
    dataset_dir = join(dirname(__file__), 'dataset')
    url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=DSZ5QPH6TDQ4JP7TVAMFP3DH6RSCA78R6U'

    dataset_path = join(dataset_dir, filename)
    r = requests.get(url)
    data = loads(r.content.decode())

    if data['message'] == 'OK':
        result = data['result']
        ethusd_timestamp = result['ethusd_timestamp']
        ethusd = result['ethusd']

        with open(dataset_path, 'a') as f:
            f.write('{};{}\n'.format(ethusd_timestamp, ethusd))

    else:
        raise Exception('Please check your internet connection')

collect_data()

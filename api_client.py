'''This module is API Client which has API CRUD operations'''
import pprint
import requests

def get_req(url):
    '''

    :param url:
    :return:
    '''
    try:
        res = requests.get(url=url)
        if res.status_code == 200:
            return res.json()
        else:
            return res
    except Exception as e:
        raise f'Failed due to {e}'

if __name__ == '__main__':
    # url = 'https://sampls.openweathermap.org/data/2.5/forecas/hourly?q=London,us&appid=b6907d289e10d714a6e88b'
    url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
    pprint.pprint(get_req(url))
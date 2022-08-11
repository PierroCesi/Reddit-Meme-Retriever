import requests
import json 
from utils import get_reddit_authentification

def init_reddit():

        authUser = get_reddit_authentification()

        auth = requests.auth.HTTPBasicAuth(authUser['CLIENT_ID'], authUser['SECRET_KEY'])

        data = {'grant_type': 'password',
                'username': authUser['USERNAME'],
                'password': authUser['PASSWORD']}

        headers = {'User-Agent': 'MyBot/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

        TOKEN = res.json()['access_token']

        return {**headers, **{'Authorization': f"bearer {TOKEN}"}}

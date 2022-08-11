from reddit import init_reddit
from utils import * 
import requests
import urllib.request
import random

init()

for subreddit in get_subreddit_list():
    res = requests.get(subreddit, headers=init_reddit())
    print("Retrieving meme from " + subreddit)
    i = 0
    for meme in res.json()['data']['children']:
        name = FOLDER_NAME+"/"+str(random.randint(0, 99999))+".jpg"
        link = meme['data']['url']
        if(link[8] == "i"): # Only pictures/gif | not videos
            urllib.request.urlretrieve(link, name)

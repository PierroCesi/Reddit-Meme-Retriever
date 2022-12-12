from reddit import init_reddit
from utils import * 
import requests
import urllib.request
import random
from utils import get_telegram_info, MY_CHANNEL
from telethon import TelegramClient

init()

memes = []
for subreddit in get_subreddit_list():
    res = requests.get(subreddit, headers=init_reddit())
    print("Retrieving meme from " + subreddit)
    for meme in res.json()['data']['children']:
        name = FOLDER_NAME+"/"+str(random.randint(0, 99999))+".jpg"
        link = meme['data']['url']
        if(link[8] == "i"): # Only pictures/gif | no videos
            try:
                urllib.request.urlretrieve(link, name)
                memes.append(name)
            except:
                print("Error on meme: ", link)

telegram_infos = get_telegram_info()
client = TelegramClient(telegram_infos["username"], telegram_infos["api_id"], telegram_infos["api_hash"])

async def post_memes():
    for meme in memes:
        try:
            await client.send_file(MY_CHANNEL, meme)
        except:
            None

with client:
    print("Posting memes")
    client.loop.run_until_complete(post_memes())



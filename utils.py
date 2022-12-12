import os 
import json

FOLDER_NAME = "memes"
SUBREDDIT_PATH = "ressources/subreddit.json"
TELEGRAM_PATH = "ressources/telegram.json"
USER_PATH = "ressources/user_data.json"

def init():
    if not os.path.exists("./"+FOLDER_NAME):
        os.makedirs("./"+FOLDER_NAME)

def get_subreddit_list():
    with open(SUBREDDIT_PATH, 'r') as f:
        return json.load(f)['subreddit']

def get_reddit_authentification():
    with open(SUBREDDIT_PATH, 'r') as f:
        return json.load(f)['authentification']

def get_telegram_info():
    with open(TELEGRAM_PATH, 'r') as f:
        return json.load(f)['telegram']

def get_telegram_channel_list():
    with open(TELEGRAM_PATH, 'r') as f:
        return json.load(f)['telegram_channel']

def get_telegram_users():
    with open(USER_PATH, 'r') as f:
        return json.load(f)
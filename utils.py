import os 
import json

FOLDER_NAME = "memes"
SUBREDDIT_PATH = "subreddit.json"

def init():
    if not os.path.exists("./"+FOLDER_NAME):
        os.makedirs("./"+FOLDER_NAME)

def get_subreddit_list():
    with open(SUBREDDIT_PATH, 'r') as f:
        return json.load(f)['subreddit']

def get_reddit_authentification():
    with open(SUBREDDIT_PATH, 'r') as f:
        return json.load(f)['authentification']

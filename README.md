# Meme Reddit Retriever

Retrieve most famous memes from reddit channel, using the reddit API.

## Installation

### Install librairie
```pip3 install requests```

### Set API authentification 
Set up your reddit API Auth URL in subreddit.json file : 
```
"authentification":{
    "CLIENT_ID": "your_client_id_here", 
    "SECRET_KEY": "your_secret_key_here",
    "USERNAME": "your_username",
    "PASSWORD": "your_password"
}

```

## Run the program 

```python3 main.py```

## Add a subreddit
Add subreddit URL to the subreddit.json file : 
```
"subreddit":[
    "https://oauth.reddit.com/r/shitposting/hot", 
    "https://oauth.reddit.com/r/memes/hot", 
    "https://oauth.reddit.com/<SUBREDDIT>/hot"
]

```
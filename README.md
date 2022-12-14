# Meme Reddit Retriever

Retrieve most famous memes from reddit channel, using the reddit API.

## Installation

### Install librairie
```pip3 install requests```

### Set Reddit API authentification 
Set up your reddit API Auth URL in ressources/subreddit.json file : 
```
"authentification":{
    "CLIENT_ID": "your_client_id_here", 
    "SECRET_KEY": "your_secret_key_here",
    "USERNAME": "your_username",
    "PASSWORD": "your_password"
}

```

### Set Telegram API authentification 
Set up your telegram API Auth URL in ressources/telegram.json file : 
```
"telegram":{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone": "+33750505050",
    "username": "your_telegram_usernam",
    "my_channel": "https://t.me/yourchannel"
}

```

### Add subreddit channels
Add subreddit URL to the ressources/subreddit.json file : 
```
"subreddit":[
    "https://oauth.reddit.com/r/shitposting/hot", 
    "https://oauth.reddit.com/r/memes/hot", 
    "https://oauth.reddit.com/<SUBREDDIT>/hot"
]

```

## Run the program 
You will maybe need to be root to launch the script.

```sudo python3 main.py```

## /!\ First run

If it is the first time you are launching the script, for security controls by telegram, you will need to input your phone number and the telegram code you received.

```
Please enter your phone (or bot token): +33750505050
Please enter the code you received: 12345
Signed in successfully as Username123
```
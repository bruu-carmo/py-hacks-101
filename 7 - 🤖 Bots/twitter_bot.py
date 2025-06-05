# Bot para postar tweet usando Tweepy

import tweepy

auth = tweepy.OAuth1UserHandler("API_KEY", "API_SECRET", "ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

api.update_status("Olá, Twitter! #Bot")

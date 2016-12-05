from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from tokens import *

auth = Oauth1Authenticator(
    consumer_key = YOUR_CONSUMER_KEY,
    consumer_secret = YOUR_CONSUMER_SECRET,
    token = YOUR_TOKEN,
    token_secret = YOUR_TOKEN_SECRET
)

params = {
    "location": "San Francisco",
    "term": "",
    "price": "2",
    "open_now": True,
    "limit": 9,
    "lang": "en"
}

client = Client(auth)

def restaurant_recs(client):
    #go to yelp api and fetch business
    response = client.search(**params)
    business_objs_list = response.businesses
    return business_objs_list

@listen_to("i'm hungry for", re.IGNORECASE)
def help(message):
    message.reply('K and')
    new_param = message._body["text"]
    params["term"] = new_param
    print params

@listen_to("i'm thirsty for", re.IGNORECASE)
def help(message):
    message.reply('K and')
    new_param = message._body["text"]
    params["term"] = new_param
    print params

@listen_to("search for me", re.IGNORECASE)
def hungry(message):
    restaurants = restaurant_recs(client)
    for place in restaurants:
        if place.location.cross_streets == None:
            response = "Try " + place.name + ", but Google the address first."
        else:
            response = "Try " + place.name + ", located at " + place.location.cross_streets + "."
        message.reply(response)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
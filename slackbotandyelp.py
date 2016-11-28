from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from tokens import *

DEFAULT_REPLY = "Sorry but I didn't understand you"

# Yelp API Oauth
auth = Oauth1Authenticator(
    consumer_key = YOUR_CONSUMER_KEY,
    consumer_secret = YOUR_CONSUMER_SECRET,
    token = YOUR_TOKEN,
    token_secret = YOUR_TOKEN_SECRET
)

params = {
    "location": "San Francisco",
    "term": "vegan",
    "price": "2",
    "open_now": True,
    "limit": 9,
    "lang": "en"
}

# location_param = raw_input(str("Where to search?"))
# params["location"] = location_param
# price_param = int(raw_input("How many Yelp dollar signs?"))
# params["price"] = price_param
# term_param = raw_input(str("Any other requirements?"))
# params["term"] = term_param

client = Client(auth)

def restaurant_recs(client):
    #go to yelp api and fetch business
    response = client.search(**params)
    business_objs_list = response.businesses
    # print the name of all the businesses that came back from yelp
    for place in business_objs_list:
        if place.location.cross_streets == None:
            print "Try", place.name + ", but Google the address first."
        else:
            print "Try", place.name + ", located at", place.location.cross_streets + "."
    return business_objs_list

# restaurants = restaurant_recs(client)

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply("I'm not sure I'm ready for such a commitment...")

# @listen_to('Can someone help me?')
# def help(message):
#     # Message is replied to the sender (prefixed with @user)
#     message.reply('Yes, I can!')
#     # Message is sent on the channel
#     # message.send('I can help everybody!')

@respond_to("I'm hungry", re.IGNORECASE)
def hungry(message):
#REPLY NEEDS A STRING
    restaurants = restaurant_recs(client)
    for place in restaurants:
        response = place.name + ": " + place.location.cross_streets
        message.reply(response)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
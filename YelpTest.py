from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from tokens import *

auth = Oauth1Authenticator(
    consumer_key = YOUR_CONSUMER_KEY,
    consumer_secret = YOUR_CONSUMER_SECRET,
    token = YOUR_TOKEN,
    token_secret = YOUR_TOKEN_SECRET
)

# build the parameter dictionary with user input
params = {
    "location": "",
    "term": "", 
    "price": "",
    "open_now": True,
    "limit": 9,
    "lang": "en"
}

location_param = raw_input(str("Where to search?"))
params["location"] = location_param
price_param = int(raw_input("How many Yelp dollar signs?"))
params["price"] = price_param
term_param = raw_input(str("Any other requirements?"))
params["term"] = term_param

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

restaurant_recs(client)

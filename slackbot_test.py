from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

DEFAULT_REPLY = "Sorry but I didn't understand you"

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    # message.send('I can help everybody!')

@respond_to("I'm hungry", re.IGNORECASE)
def hungry(message):
    message.reply("Ok!")
    

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
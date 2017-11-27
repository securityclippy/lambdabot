#!/usr/bin/env python3
'''
Lambda function handler for entry into lambdabot
'''

import os
from lambdabot import LambdaBot

def handler(event, context):
    '''
    :param event:
    :param context:
    :return:
    '''
    # Note: This is hear to provide a simple way to verify
    # your function when you set up your slack bot.  Dont't remove
    #this unless you're intending to solve this a different way
    if "challenge" in event:
        return event["challenge"]
    else:
        print("incoming msg: {}".format(event))
        #instantiate bot and do things!
        bot = LambdaBot(botname=os.environ['BOT_NAME'])
        if not bot.process_event(event):
            print("event processing failed, exiting")
            return
        #make sure bot is really supposed to reply
        if bot.is_dm() or bot.has_bot_mention():
            if not bot.is_bot_msg():
                if 'test' in bot.event.event.text:
                    bot.maze_reply()
                    return
            ## Insert actual code do do interesting things here
            ## event is exposed by lb.event.event. (or lb.event) for meta data
            #dummy response just echos back the user input in reverse.  Good for testing
            #r = lb.maze_reply()
                bot.dummy_response()
        return

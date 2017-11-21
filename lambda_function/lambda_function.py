#!/usr/bin/env python3

from lambdabot import LambdaBot

def handler(event, context):
    '''
    :param event:
    :param context:
    :return:
    '''
    # Note: This is hear to provide a simple way to verify your function when you set up your slack bot.  Dont't remove
    #this unless you're intending to solve this a different way
    if "challenge" in event:
        return event["challenge"]
    else:
        #instantiate bot and do things!
        lb = LambdaBot()
        lb.process_event(event)
        ## Insert actual code do do interesting things here
        ## event is exposed by lb.event.event. (or lb.event) for meta data
        #dummy response just echos back the user input in reverse.  Good for testing
        lb.dummy_response()
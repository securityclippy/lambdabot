#!/usr/bin/env python3

### simple slack chatbot built to run in aws lambda functions

import logging
from urllib.parse import urlencode
import requests
import json
import boto3

class Event(object):
    def __init__(self, slack_event=None):
        if slack_event:
            self.type = slack_event['type']
            self.user = slack_event['user']
            self.text = slack_event['text']
            self.ts = slack_event['ts']
            self.channel = slack_event['channel']
            self.event_ts = slack_event['event_ts']
        else:
            self.type = None
            self.user = None
            self.text = None
            self.ts = None
            self.channel = None
            self.event_ts = None

class SlackBotMessage(object):
    def __init__(self, event=None):
        if event:
            self.event = Event(event['event'])
            self.token = event['token']
            self.team_id = event['team_id']
            self.api_app_id = event['api_app_id']
            self.type = event['type']
            self.event_id = event['event_id']
            self.event_time = event['event_time']
            self.authed_users = event['authed_users']
            self.has_challenge = False
            if "challege" in event:
                self.has_challenge = True
        else:
            self.event = Event()
            self.token = ""
            self.team_id = ""
            self.api_app_id = ""
            self.type = ""
            self.event_id = ""
            self.event_time = ""
            self.authed_users = ""
            self.has_challenge = False


class LambdaBot(object):
    def __init__(self, region_name='us-east-1',
                 ssm_parameter_name='lambda_bot_token',
                 verification_token_param_name='lambda_bot_verification_token'):
        '''
        :param event:
        :param region_name:
        :param ssm_parameter_name:
        '''
        #if this is an auth event, return challenge and exit
        self.postMessageUrl = "https://slack.com/api/chat.postMessage"
        ssm = boto3.client('ssm', region_name=region_name)
        self.bot_token = ssm.get_parameters(Names=[ssm_parameter_name], WithDecryption=True)['Parameters'][0]['Value']
        self.verification_token = ssm.get_parameters(Names=[verification_token_param_name], WithDecryption=True)['Parameters'][0]['Value']
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
        self.event = SlackBotMessage()

    def verify_msg(self):
        if self.event.token == self.verification_token:
            print("token mismatch")
            return False
        return True


    def process_event(self, event):
        #if "challenge" in event:
            #return event['challenge']
        self.raw_event = event
        self.event = SlackBotMessage(event)
        #if self._authenticate_to_slack():
            #return self._authenticate_to_slack()
        if not self.verify_msg():
            exit(0)

    def _authenticate_to_slack(self):
        if "challenge" in self.raw_event:
            return self.raw_event['challenge']

    def dummy_response(self):
        response = {
            "text": self.event.event.text[::-1],
            "channel": self.event.event.channel,
            "token": self.bot_token
        }
        self.respond_with(response)
        return

    def respond_with(self, response):
        data = urlencode(response)
        r = requests.post(self.postMessageUrl, data=data, headers=self.headers)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)
        return

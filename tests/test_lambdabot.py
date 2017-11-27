from pytest import fixture
from lambda_function.lambdabot import LambdaBot
import json

import os

os.environ['AWS_ACCESS_KEY_ID'] = "LOEIJRDLKD0349DF"
os.environ['AWS_SECRET_ACCESS_KEY'] = "LKDFIO344KDFKL349DJKLfd"


@fixture
def bot():
    return LambdaBot('testbot', is_lambda=False, verification_token='test_token')

@fixture
def user_event():
    with open("tests/test_user_event.json", "r") as f:
        event = json.load(f)
    return event

@fixture
def bot_event():
    with open("tests/test_bot_mesage.json", "r") as f:
        event = json.load(f)
    return event

def test_botname_required():
    lb = LambdaBot('testbot')
    assert lb.botname == 'testbot'

def test_handle_resp_false():
    lb = LambdaBot('testbot')
    resp = '{"ok": false}'
    assert lb._handle_resp(resp) == False

def test_handle_resp_true():
    lb = LambdaBot('testbot')
    resp = '{"ok": true}'
    assert lb._handle_resp(resp) == True

def test_is_bot_msg_true():
    lb = LambdaBot('testbot', is_lambda=False, verification_token='test_token')
    with open("tests/test_bot_message.json", "r") as f:
        data = json.load(f)
        data['token'] = 'test_token'
    lb.process_event(data)
    assert lb.is_bot_msg() == True

def test_is_bot_msg_false():
    lb = LambdaBot('testbot', is_lambda=False, verification_token='test_token')
    with open("tests/test_user_event.json", "r") as f:
        data = json.load(f)
        data['token'] = 'test_token'
    lb.process_event(data)
    assert lb.is_bot_msg() == False

def test_verify_msg_false():
    lb = bot()
    lb.verification_token = 'bad_token'
    event = user_event()
    lb.process_event(event)
    assert lb.verify_msg() == False

def test_verify_msg_true():
    lb = bot()
    lb.verification_token = 'good_token'
    event = user_event()
    event['token'] = 'good_token'
    lb.process_event(event)
    assert lb.verify_msg() == True


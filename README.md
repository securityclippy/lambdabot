## Lambdabot

[![Build Status](https://travis-ci.org/securityclippy/lambdabot.svg?branch=master)](https://travis-ci.org/securityclippy/lambdabot)
[![Coverage Status](https://coveralls.io/repos/github/securityclippy/lambdabot/badge.svg?branch=master)](https://coveralls.io/github/securityclippy/lambdabot?branch=master)

##### About:  
Lambdabot is designed to be a simple example of a serverless slack chatbot which can
be easily extended to work within a variaty of contexts.  By itself, all Lambdabot will do is
response to a DM in slack by reversing the text sent to it.  The idea is that instead of using
the static reverser interaction, the user will substitute other logic in and use the bot for
more complex functions

##### Requirements: 
Lambdabot is built in python3 and is deploy with terraform. Make sure terraform is installed and in your
$PATH

### Deployment:

1. create a slack app.  [create slack app](docs/slack_bot_setup.md)

```bash
git clone https://github.com/securityclippy/lambdabot.git
cd lambdabot
cp lambdabot_config.json.example lambdabot.conf
```
```commandline
edit lambdabot.conf with your specific info and save
```

```commandline
python3 manage.py --apply
```


TODO:
- [ ] Add custom auth on api_gateway to validate bot token
- [ ] Tighten permissions on ssm parameter store (currently buggy and only works
to change permissions by destroying role.  Attach role perms seem to also fail)
- [ ] Slash commands for bot 
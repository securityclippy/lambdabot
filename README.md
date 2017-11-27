[![Build Status](https://travis-ci.org/securityclippy/lambdabot.svg?branch=master)](https://travis-ci.org/securityclippy/lambdabot)
[![Coverage Status](https://coveralls.io/repos/github/securityclippy/lambdabot/badge.svg?branch=master)](https://coveralls.io/github/securityclippy/lambdabot?branch=master)

## Lambdabot

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
1. copy ```lambadbot_config.json.exampl``` -> ```lambdabot_config.json```
2. open ```lambdabot_config.json``` and enter your specific variables. (make sure to save your file)
3. run ```python3 manage.py --apply```


TODO: Guide to setting up slack bot from the slack side  of things
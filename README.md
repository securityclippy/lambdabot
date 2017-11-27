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
1. copy ```lambadbot_config.json.example``` -> ```lambdabot.conf```
2. open ```lambdabot.conf``` and enter your specific variables. (make sure to save your file)
3. run ```python3 manage.py --apply```


TODO:
- [ ] Tighten permissions on ssm parameter store (currently buggy and only works
to change permissions by destroying role.  Attach role perms seem to also fail)
- [ ] Slash commands for bot 
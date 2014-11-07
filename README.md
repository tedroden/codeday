# Fancy Hands Code Day


## Install the Python SDK

The Fancy Hands python SDK lives on github at [github.com/fancyhands/fancyhands-python](https://github.com/fancyhands/fancyhands-python).

You can install it with `pip`, but let's just [download it by hand](https://github.com/fancyhands/fancyhands-python/archive/master.zip): `http://bit.ly/fh-zip`

Unzip and install it:

    unzip fancyhands-python-master.zip
    cd fancyhands-python-master
    sudo python setup.py install

Poke around with the Fancy Hands code if you like...

## Get an API Key

- Go to [fancyhands.com/developer](http://www.fancyhands.com/developer)
- Click [Create an App](http://www.fancyhands.com/developer/apps/new)
  - You can put in any information you like, none of if affects building your app.
- Save it and keep this tab open!

## Create a hello world application

In this script, we'll create a super simple application. This is just a sanity check to ensure we can talk to the Fancy Hands server. This application will:
 1. Connect to Fancy Hands
 2. Send some parameters
 3. Print out the response from the server

Create a file credentials.py:

```python
FANCYHANDS_KEY = "YOUR_FANCY_HANDS_KEY"
FANCYHANDS_SECRET = "YOUR_FANCY_HANDS_SECRET"
```

OK, not create a file called hello.py:

```python
from fancyhands import FancyhandsClient
from credentials import *
client = FancyhandsClient(FANCYHANDS_KEY, FANCYHANDS_SECRET)
print client.echo_get({ 'HELLO WORLD': 'GOODBYE' })
```

Now run it:

`python hello.py`

You should a long version of this: `{u'oauth_nonce': u'59892137', ...  u'HELLO WORLD': u'GOODBYE'}`

## Tell us what to do?

```python
from fancyhands import FancyhandsClient
from datetime import timedelta, datetime
from credentials import *

TASK_TITLE = "What's the top story on the frontpage of reddit?"
TASK_BODY = "Go to reddit.com, what's the title for the top headline on the frontpage?"
TASK_BID = 2.0
TASK_EXPIRE = datetime.utcnow() + timedelta(hours=1)

client = FancyhandsClient(FANCYHANDS_KEY, FANCYHANDS_SECRET)
print client.standard_create(TASK_TITLE, TASK_BODY, TASK_BID, TASK_EXPIRE, test=True)
```

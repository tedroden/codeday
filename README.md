# Fancy Hands Code Day

[The Slides!](https://docs.google.com/presentation/d/1E_MXFHD-6kr24aED7E9AejPG2UaclxfEgdEhyIG7oY4/edit#slide=id.p)

## Install the Python SDK

The Fancy Hands python SDK lives on github at [github.com/fancyhands/fancyhands-python](https://github.com/fancyhands/fancyhands-python).

You can install it with `pip`, but let's just [download it by hand](https://github.com/fancyhands/fancyhands-python/archive/master.zip): [http://bit.ly/fh-zip](http://bit.ly/fh-zip)

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
FANCYHANDS_KEY = "YOUR_FANCYHANDS_KEY"
FANCYHANDS_SECRET = "YOUR_FANCYHANDS_SECRET"
```

OK, now create a file called hello.py:

```python
from fancyhands import FancyhandsClient
from credentials import *
client = FancyhandsClient(FANCYHANDS_KEY, FANCYHANDS_SECRET)
print client.echo_get({ 'HELLO WORLD': 'GOODBYE' })
```

Now run it:

`python hello.py`

You should a long version of this: `{u'oauth_nonce': u'59892137', ...  u'HELLO WORLD': u'GOODBYE'}`

Not seeing this? Let me know!

## Tell us what to do

Now that we know we can connect to the server, let's send a task to Fancy Hands.

In this task, we'll use our `fancyhands.standard.Standard` endpoint to create a standard Fancy Hands Task.

```python
from fancyhands import FancyhandsClient
from datetime import timedelta, datetime
from credentials import *

TASK_TITLE = "What's the top story on the frontpage of Hacker News?"
TASK_BODY = "Go to news.ycombinator.com, what's the title for the top headline on the frontpage?"
TASK_BID = 2.0
TASK_EXPIRE = datetime.utcnow() + timedelta(hours=1)

client = FancyhandsClient(FANCYHANDS_KEY, FANCYHANDS_SECRET)
request = client.standard_create(TASK_TITLE, TASK_BODY, TASK_BID, TASK_EXPIRE, test=True)
key = request.get('key')

print "Created Request: %s" % key
```

If you want to check the status and see the result:

```python
loaded = client.standard_get(key)
```

## Call me, maybe?

In this one, we'll have a real live human call us. We'll use the `fancyhands.call.Outgoing` endpoint which is specific for phone calls. It's also pretty fast and very cheap!

The hardest part here is that we have to define a script. I'll give you something to copy and paste, but you can always use our [script builder](https://www.fancyhands.com/api/explorer/script/builder) to build one for you.

```python
from fancyhands import FancyhandsClient
from datetime import timedelta, datetime
from credentials import *
import json
PHONE = "212-555-1212" # put your phone number here

# copy this conversation: http://bit.ly/fh-convo
CONVERSATION = {
  "id": "sample_outgoing",
  "name": "Sample Outgoing",
  "version": 1.1,
  "scripts": [
    {
      "id": "finish",
      "steps": [
        {
          "name": "hello",
          "prompt": "Hello, my name is $assistant_name. Between the following colors, which is your favorite: red, white, or blue?",
          "note": "This is a sample task, but please do it. Thanks!",
          "type": "select",
          "options": [
            {"name": "red", },
            { "name": "white", },
            { "name": "blue", }
          ]
        },
        {
          "type": "logic_control",
          "name": "goodbye",
          "note": "",
          "prompt": "Thanks! Enjoy the rest of Code Day.",
          "options": []
        }
      ]
    }
  ]
}

client = FancyhandsClient(FANCYHANDS_KEY, FANCYHANDS_SECRET)
request = client.outgoing_create(PHONE, json.dumps(CONVERSATION))
key = request.get('key')

print "Created Call Request: %s" % key
```


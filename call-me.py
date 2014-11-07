""" 
Have Fancy Hands call you.
"""

from fancyhands import FancyhandsClient
from datetime import timedelta, datetime
from credentials import *
import json
PHONE = "212-555-1212"

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
print "Loading the request..."

loaded = client.outgoing_get(key)
print loaded

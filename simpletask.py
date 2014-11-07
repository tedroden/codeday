""" Tell Fancy Hands to do something """

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
print "Loading the request..."

loaded = client.standard_get(key)
print loaded

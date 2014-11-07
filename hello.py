""" 
A Simple hello world application for the API 

This is the example we use for the hello world section.
"""
from fancyhands import FancyhandsClient
from credentials import *
client = FancyhandsClient(FANCYHANDS_KEY, FANCYHANDS_SECRET)
print client.echo_post({ 'HELLO WORLD': 'GOODBYE' })


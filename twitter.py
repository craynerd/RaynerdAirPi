#!/usr/bin/env python
import sys
from twython import Twython
from twython import TwythonError
import os

CONSUMER_KEY = 'XXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXX'

# client_args
from twython import Twython

#proxy settings set in script if needed! remove comment
#client_args = {
#    'proxies': {
#        'http': 'http://proxy.ip.here:8080orYourPort',
#        'https': 'https://proxy.ip.here:8080orYourPort',
#        'verify': 'False'                                 #include this to ignore ssl errors! http only.
#    }
#}

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) #for proxy.....ACCESS_SECRET, client_args=client_args)

def send_tweet1(temp_value, temp_symbol, light_value, light_symbol, pressure_value, pressure_symbol, volume_value, volume_symbol):
        try:
	        photo = open('twitterpicture.jpg','rb')
		api.update_status_with_media(media=photo, status="Temp: {0}{1}. Light Level: {2:.2f} {3}. Pressure: {4:.2f} {5}. Volume: {6:.2f} {7}.".format(temp_value, temp_symbol, light_value, light_symbol, pressure_value, pressure_symbol, volume_value, volume_symbol))
                print "Successfully posted tweet."
        except TwythonError:
                print "Failed to post tweet - duplicate"

def send_tweet2(temp_value, temp_symbol, light_value, light_symbol, pressure_value, pressure_symbol, volume_value, volume_symbol):
        try:
		api.update_status(status="Temp: {0}{1}. Light Level: {2:.2f} {3}. Pressure: {4:.2f} {5}. Volume: {6:.2f} {7}.".format(temp_value, temp_symbol, light_value, light_symbol, pressure_value, pressure_symbol, volume_value, volume_symbol))
                print "Successfully posted tweet."
        except TwythonError:
                print "Failed to post tweet - duplicate"

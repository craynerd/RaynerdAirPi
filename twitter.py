#!/usr/bin/env python
import sys
from twython import Twython
from twython import TwythonError
import os

CONSUMER_KEY = 'XXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXX'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

def send_tweet(temp_value, temp_symbol, light_value, light_symbol, pressure_value, pressure_symbol, volume_value, volume_symbol):
        try: 
                photo = open('twitterpicture.jpg','rb')
		api.update_status_with_media(media=photo, status="Temp: {0}{1}. Light Level: {2:.2f} {3}. Pressure: {4:.2f} {5}. Volume: {6:.2f} {7}.".format(temp_value, temp_symbol, light_value, light_symbol, pressure_value, pressure_symbol, volume_value, volume_symbol))
                print "Successfully posted tweet."
        except TwythonError:
                print "Failed to post tweet - duplicate"

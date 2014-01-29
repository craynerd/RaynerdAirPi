RaynerdAirPi
============

This is code edited from AirPi.es for the raspberry Pi AirPi weather/air monitoring board.

Edits to the original code:
1. Rounds all numbers to 2dp
2. Integrates a twitter post of the data being collected

Upload or Replace the three files, airpi.py twitter.py and settings.cfg in the AirPi folder. 

How to integrate Twitter:
Sign up for twitter developers and create a "new app" - the informatuon requested can be ignored! Make up a website and callback URL if you wish!. On the settings tab, change Application Type to Read and Write. On the Details tab click "Create access OAuth token". Open twitter.py and enter the KEYS. Note that ACCESS_KEY is referred to as Access Token on the twitter app page. 
Install Twython: 
sudo apt-get install python-setuptools
sudo apt-get install pip
sudo pip install twython


Twitter does limit the amount of posts to ~1000 each day. It is likely you will want to upload to Xively more frequently than this:
sudo nano settings.cfg 
Edit the twitter:Xively upload ration to reduce the amount of auto tweets.

Enjoy!

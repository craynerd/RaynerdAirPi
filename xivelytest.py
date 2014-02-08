# C.Raynerd 8.2.14    #This script tests Xively upload feed
# Change APIKEY and also FEEDID to match your xively account. 
# Running this script should generate a Test Channel and update a test variable every 10 seconds
# IF this does not work - attempt to connect via http ("http://api.xively.com/v2/feeds/FEEDID")

import requests
import time
import json

x = 10     # test variable

while 1:         # loop forever
	a = {"datastreams": [{"id": "test","current_value": x}]}        

	z = requests.put("https://api.xively.com/v2/feeds/FEEDID_HERE",
                         headers={"X-ApiKey":"APIKEY_HERE"},
                         data=json.dumps(a))
	print "Success - uploaded to Xively: test =", x
	x = x+10
	time.sleep (10)       # waits 10 seconds before each upload

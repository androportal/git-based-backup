#!/usr/bin/python -tt
# test script for android

'''

$ export AP_PORT=4321  # Use set AP_PORT=9999 on Windows
$ export AP_HOST=192.168.0.100  # Use set AP_HOST=192.168.0.100 on Windows
$ python basic.py

'''

# import android.py
# used to communicate with sl4a 
import android
import time

# create obj
say = android.Android()

# basic loop
while True:
    # notification
    say.makeToast("what say ?")
    print "pop-up"
    time.sleep(5)






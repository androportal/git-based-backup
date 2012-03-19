#!/usr/bin/python -tt
# test script for android


import time
import android
say = android.Android()

while True:	
	say.makeToast("what say ?")
	print "pop-up"
	time.sleep(5)

	


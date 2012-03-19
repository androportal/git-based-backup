#!/usr/bin/python -tt
# test script

import os,sys
import time
import android
say = android.Android()

def backupSync(srcDir,destDir):
    # check for src dir
    if not os.path.exists(srcDir):
        #sys.exit("Source directory does not exist!")
        say.makeToast("Src dir not exist!")
    else:
        # check if the destination path already exist, if not, create it.
        if not os.path.exists(destDir):
            os.mkdir(destDir) # make directory
            print "Destination dir created: ", destDir
        else:
            rsync_command = 'cp -r ' + srcDir + ' ' + destDir
            os.system(rsync_command)
            print "Content successfully backed up"
            say.makeToast("Content successfully backed up")
            
backupSync('/sdcard/src/','/sdcard/dest')

	


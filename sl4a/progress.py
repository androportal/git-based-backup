#!/usr/bin/python -tt
#name = droid.dialogGetInput("Enter the path")

import os
import time
import android
from subprocess import Popen, PIPE

droid = android.Android()


def testing_horizontal_progress():

    # count number of files in src dir
    os.chdir('/sdcard/src')
    file_count = Popen('ls | wc -l',shell=True, stdout=PIPE).stdout.readline()
    src_file_count = file_count.strip()
    #    max_file_count = int(src_file_count)
    print int(src_file_count)

    title = 'Copying...'
    message = 'File copy in progress, please wait '
    droid.dialogCreateHorizontalProgress(title, message, int(src_file_count))
    droid.dialogShow()

    
    temp_file_names = Popen('ls -1',shell=True, stdout=PIPE).stdout.readlines()
    listOfFiles = list(temp_file_names)

    srcDir = '/sdcard/src'
    destDir = '/sdcard/dest'

    file_count = 0
    for file1 in listOfFiles:
        time.sleep(1)
#        print srcDir + '/' + file1.strip
        copy_command = 'cp -r ' + srcDir + '/' + file1.strip('\n') + ' ' + destDir
#        print copy_command
        os.system(copy_command)
        file_count += 1
        droid.dialogSetCurrentProgress(file_count)
    droid.dialogDismiss()
#        print file_count

'''
    #droid.dialogSetMaxProgress(4096)
    droid.dialogShow()
    for x in range(0,100):
        time.sleep(0.1)
        droid.dialogSetCurrentProgress(x)
    droid.dialogDismiss()
 #  return True

'''
testing_horizontal_progress()
#droid.makeToast("hello")

def show_copy_status():
    os.chdir('/sdcard/src')
    file_count = Popen('ls | wc -l',shell=True, stdout=PIPE).stdout.readline()
    src_file_count = file_count.strip()
    #    max_file_count = int(src_file_count)
    print int(src_file_count)

#   src_file_names = Popen('ls -1 > /sdcard/file_list',shell=True, stdout=PIPE).stdout.readlines()
    temp_file_names = Popen('ls -1',shell=True, stdout=PIPE).stdout.readlines()
    listOfFiles = list(temp_file_names)

    srcDir = '/sdcard/src'
    destDir = '/sdcard/dest'

    file_count = 0
    for file in listOfFiles:
        pass
#        print srcDir + '/' + file
#        copy_command = 'cp -r ' + srcDir + '/' + file + ' ' + destDir
#        os.system(copy_command)
        file_count += 1
        print file_count


        

'''

    srcDir = '/sdcard/dest'
    destDir = '/sdcard/src'

    copy_command = 'cp -r ' + srcDir + ' ' + destDir
    os.system(copy_command)

    
    
    
    os.chdir('/sdcard/src')
    count = 0
    for count in src_file_count:
        time.sleep(0.1)
        dest_file_count = Popen('ls | wc -l',shell=True, stdout=PIPE).stdout.readline()
        count  = dest_file_count
        print count
'''      
        
        


    

#show_copy_status()
    
    
    


#!/usr/bin/python -tt
#name = droid.dialogGetInput("Enter the path")

import os
import time
import android
from subprocess import Popen, PIPE

droid = android.Android()

def FirstYesNoDialog():
    droid.dialogCreateAlert('Backup/Restore Tool',' Do you want to proceed')
    droid.dialogSetPositiveButtonText('Yes')
    droid.dialogSetNegativeButtonText('Not now')
    droid.dialogShow()
    yesNo = droid.dialogGetResponse().result
    if yesNo['which'] == 'positive':
        backupRestoreDialog()
    else:
        droid.makeToast("Good Bye !")

def backupRestoreDialog():
        droid.dialogCreateAlert('Select Option')
        droid.dialogSetPositiveButtonText('OK')
        droid.dialogSetNegativeButtonText('Cancel')
        choice = ['backup','restore']
        droid.dialogSetSingleChoiceItems(choice)
        droid.dialogShow()
        OkCancel = droid.dialogGetResponse().result

        srcDir='/sdcard/src'
        destDir='/sdcard/dest'

        if OkCancel['which'] == 'positive':
            choice = droid.dialogGetSelectedItems().result
            if choice == [0]:
                backup(srcDir,destDir)
            elif choice == [1]:
                #droid.makeToast("Restore_Program_Called")
                restore(destDir,srcDir)
            droid.makeToast("Good Bye!")


def progress_bar(srcDir,destDir,src_file_count):

    title = 'Copying...'
    message = 'File copy in progress, please wait '
    droid.dialogCreateHorizontalProgress(title, message, int(src_file_count))
    droid.dialogShow()

    # take file-names as a list
    temp_file_names = Popen('ls -1',shell=True, stdout=PIPE).stdout.readlines()
    listOfFiles = list(temp_file_names)

    file_count = 0
    for file_nm in listOfFiles:
        time.sleep(1)
        copy_command = 'cp -r ' + srcDir + '/' + file_nm.strip('\n') + ' ' + destDir
        os.system(copy_command)
        file_count += 1
        droid.dialogSetCurrentProgress(file_count)
    droid.dialogDismiss()


def backup(srcDir,destDir):

    # check for src dir
    if not os.path.exists(srcDir):
        droid.makeToast("Src dir not exist!")
    else:
        # count number of files in src dir
        os.chdir(srcDir)
        file_count = Popen('ls | wc -l',shell=True, stdout=PIPE).stdout.readline()
        src_file_count = file_count.strip()

        # check if the destination path already exist, if not, create it.
        if not os.path.exists(destDir):
            os.mkdir(destDir) # make directory
            print "Destination dir created: ", destDir
        else:
            progress_bar(srcDir,destDir,src_file_count)
            # rsync_command = 'cp -r ' + srcDir + ' ' + destDir
            # os.system(rsync_command)
            # print "Content successfully backed up"
            # droid.makeToast("Content successfully backed up")


def restore(srcDir,destDir):

    backupDir=srcDir                    # from where to backup apks
    restoreDir=destDir                  # where to restore apks
    
    # check for backup dir
    if not os.path.exists(backupDir):
        droid.makeToast("Backup dir does not exist!")
        sys.exit("Backup dir does not exist!")
    else:
        # count number of files in src dir
        os.chdir(backupDir)
        file_count = Popen('ls | wc -l',shell=True, stdout=PIPE).stdout.readline()
        src_file_count = file_count.strip()
        
        # check if the destination path already exist, if not, create it.
        if not os.path.exists(restoreDir):
            sys.exit("Restore Dir does not exist!")
            # os.mkdir(destDir) # make directory
            # print "Destination dir created: ", destDir
        else:
            progress_bar(srcDir,destDir,src_file_count)
            # rsync_command = 'cp -r ' + srcDir + ' ' + destDir
            # os.system(rsync_command)
            # print "Content successfully backed up"
            # droid.makeToast("Content successfully backed up")



if __name__ == '__main__':
    FirstYesNoDialog()



"""
    # check for src dir
    if not os.path.exists(srcDir):
        droid.makeToast("Src dir not exist!")
    else:
        # check if the destination path already exist, if not, create it.
        if not os.path.exists(destDir):
            os.mkdir(destDir) # make directory
            print "Destination dir created: ", destDir
        else:
            rsync_command = 'cp -r ' + srcDir + ' ' + destDir
            os.system(rsync_command)
            print "Content successfully backed up"
            droid.makeToast("Content successfully backed up")

# call function
backupSync('/sdcard/src/','/sdcard/dest')
"""

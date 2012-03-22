#!/usr/bin/python -tt
# sl4a based backup/restore app

import os
import time
import android
from subprocess import Popen, PIPE

# make an instant
droid = android.Android()

#==============================  1  ========================================
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

#==============================  2  =========================================

def backupRestoreDialog():
        droid.dialogCreateAlert('Select Option')
        droid.dialogSetPositiveButtonText('OK')
        droid.dialogSetNegativeButtonText('Cancel')
        choice = ['backup','restore']
        droid.dialogSetSingleChoiceItems(choice)
        droid.dialogShow()
        OkCancel = droid.dialogGetResponse().result

        # source and destination path
        # for multiple paths, create a list
        srcDirs=['/data/app','/data/data']
        destDirs=['/sdcard/data/app','/sdcard/data/data']

        if OkCancel['which'] == 'positive':
            choice = droid.dialogGetSelectedItems().result
            if choice == [0]:
                # pass a range to for loop as a tuple
                for backupPath in range(0,len(srcDirs)):
                    backup(srcDirs[backupPath],destDirs[backupPath])
            elif choice == [1]:
                for restorePath in range(0,len(srcDirs)):
                    restore(destDirs[restorePath],srcDirs[restorePath])
            droid.makeToast("Good Bye!")

#=============================  3  =========================================

def progress_bar(srcDir,destDir,src_file_count):

    title = 'Copying...'
    message = 'File copy in progress, please wait '
    droid.dialogCreateHorizontalProgress(title, message, int(src_file_count))
    droid.dialogShow()

    # take file-names as a list from source
    temp_file_names = Popen('ls -1',shell=True, stdout=PIPE).stdout.readlines()
    listOfFiles = list(temp_file_names)

    
    file_count = 0              # initial file count
    # go through the listOfFiles and copy each file at once
    for file_nm in listOfFiles:
        time.sleep(0.1)
        copy_command = 'cp -r ' + srcDir + '/' + file_nm.strip('\n') + ' ' + destDir
        print copy_command
#        os.system(copy_command)
        file_count += 1
        droid.dialogSetCurrentProgress(file_count)
    droid.dialogDismiss()

#==============================  4  =========================================

def backup(srcDir,destDir):
    print srcDir,destDir,
    # check for src dir
    if not os.path.exists(srcDir):
        droid.makeToast("Src dir not exist!")
    else:
        # count number of files in src dir
        os.chdir(srcDir)
        file_count = Popen('ls | wc -l',shell=True, stdout=PIPE).stdout.readline()
        src_file_count = file_count.strip()

        # check if the destination dir path exist, if not, create it.
        if not os.path.exists(destDir):
            os.makedirs(destDir) # make directory
            print "Destination dir created: ", destDir
            progress_bar(srcDir,destDir,src_file_count)
        else:
            progress_bar(srcDir,destDir,src_file_count)

#=============================   5  =========================================

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

        # check if the destination dir path
        if not os.path.exists(restoreDir):
            sys.exit("Restore Dir does not exist!")
        else:
            # call progress bar
            progress_bar(srcDir,destDir,src_file_count)

#============================================================================
#============================================================================

if __name__ == '__main__':
    FirstYesNoDialog()


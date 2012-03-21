#name = droid.dialogGetInput("Enter the path")

import os
import time
import android
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
        if OkCancel['which'] == 'positive':
            choice = droid.dialogGetSelectedItems().result
            if choice == [0]:
                backup()
            elif choice == [1]:
                restore()
            droid.makeToast("Good Bye!")





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

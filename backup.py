#!/usr/bin/env python
"""
backup.py : Checks periodically the status of directory and creates
a git repository. One can checkout to particular state any time.

__author__      = Sachin & Srikant
__copyright__   = GNU GPLv3

"""

import os,time,sys
from subprocess import Popen, PIPE

global dirPath
global timeInterval 
timeInterval = 5                # define the time interval(in seconds)


# Accepts only one Command line argument as directory-name              
def pathforBackup():
    if len(sys.argv) == 2:                    
        global dirPath
        dirPath = sys.argv[1]
    else:    
        sys.exit("Provide a directory path for backup")

# check for existance of .git directory, else create it 
def checkforGit():
    global dirPath
    if not os.path.exists(dirPath + '/.git/'):
        os.system('git init ' + dirPath)
    else:
        print '.git exist at destination'
    os.chdir(dirPath)                       # change directory to dirPath

# function to handle newly untracked files
def gitUntracked():
    # list all untracked files
    untracked = Popen('git ls-files --exclude-standard --others',shell=True, stdout=PIPE).stdout.readlines()
    # go through every file and add
    for untrackedfile in untracked:
        gitAdd(untrackedfile)

# function to handle modification made to file(s)
def gitModified():
    commit_msg='modified'
    modified = Popen('git ls-files --modified',shell=True, stdout=PIPE).stdout.readlines()
    for modifiedfile in modified:
        gitAdd(modifiedfile)

# function to handle deleted file(s)
def gitDelete():
    commit_msg='deleted'
    deleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
    for deletedfile in deleted:
        gitdelete='git rm ' + deletedfile
        os.system(gitdelete)

# function to add changes    
def gitAdd(receivedFiles):
    gitadd = 'git add ' + receivedFiles
    os.system(gitadd)
    
# commit changes
def gitCommit():
    myWeek = time.strftime("%a")
    myDate = time.strftime("%Y, %m, %d")
    
    myTime = time.strftime("%H-%M-%S")
    timeStamp='Commit on: ' + myDate 
    gitcommit='git commit -m ' + "'" + timeStamp + ' ' + "'" 
    os.system(gitcommit)

if __name__=='__main__':
    # call below functions only once
    pathforBackup()
    checkforGit()   
    while True:
        # call functions
        gitUntracked()
        gitModified()
        gitDelete()
        gitCommit()
	time.sleep(timeInterval)
	
	
	

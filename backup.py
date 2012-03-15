#!/usr/bin/env python
"""
backup.py : Checks periodically the status of directory and creates
a git repository. One can checkout to particular state any time.

__author__      = Sachin & Srikant
__copyright__   = GNU GPLv3

"""

import os,time,sys
from subprocess import Popen, PIPE
global filePath 


def pathforBackup():
    if len(sys.argv) == 2:                    # accepts one CLA, i.e filename              
        global filePath
        filePath = sys.argv[1]
    else:    
        sys.exit("Provide a file path for backup")

def checkforGit():
    global filePath
    if not os.path.exists(filePath + '/.git/'):
        os.system('git init ' + filePath)
    else:
        print '.git exist at destination'
    cdtofilePath = 'cd ' + filePath   
    os.system(cdtofilePath)
    print cdtofilePath

def gitUntracked():
    commit_msg='added'
    untracked = Popen('git ls-files --exclude-standard --others',shell=True, stdout=PIPE).stdout.readlines()
    for untrackedfile in untracked:
        gitAdd(untrackedfile,commit_msg)

def gitModified():
    commit_msg='modified'
    modified = Popen('git ls-files --modified',shell=True, stdout=PIPE).stdout.readlines()
    for modifiedfile in modified:
        gitAdd(modifiedfile,commit_msg)

def gitDelete():
    commit_msg='deleted'
    deleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
    for deletedfile in deleted:
        gitdelete='git rm ' + deletedfile
        os.system(gitdelete)
        gitCommit(commit_msg)

def gitAdd(receivedFiles,commitMsg):
    print commitMsg
    gitadd = 'git add ' + receivedFiles
    os.system(gitadd)
    gitCommit(commitMsg)

def gitCommit(msg):
    #print "In function gitCommit " + msg
    myWeek = time.strftime("%a")
    myDate = time.strftime("%d-%B-%Y")
    myTime = time.strftime("%H-%M-%S")
    timeStamp='Commit on: ' + myWeek + ' ' + myDate + ' ' + myTime
    gitcommit='git commit -m ' + "'" + timeStamp + ' ' + '\nAction: ' + msg + "'" 
    os.system(gitcommit)

if __name__=='__main__':
    pathforBackup()
    checkforGit()   
    while True:
        gitUntracked()
        gitModified()
        gitDelete()
	time.sleep(5)
	
	
	
########################################################################################
""" Not in use 
def gitstart():
    # if not os.path.exists('.git'):
    if not os.path.isdir('.git'):
        print "No .git/ dir"
        os.system('git init')       
    else:
        #print ".git/ dir exist"
        gitUntracked()
        gitModified()
        gitDelete()
        # gitCached()
        
def gitCached():
    cached = Popen('git ls-files --cached',shell=True, stdout=PIPE).stdout.readlines()
    for cachedfile in cached:
        print cachedfile       
        
"""        
        

import os,time
from subprocess import Popen, PIPE
eachfile = ''

if not os.path.exists('.git'):
    os.system('git init')

while True:
    bashout = Popen('git status',shell=True, stdout=PIPE).stdout.readlines()
    
    """captures git status from stdout, 'if' statement checks line2 from 
    stdout with standard commit message """

    if not bashout[1].strip() == 'nothing to commit (working directory clean)':
        userDeleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
        for i in userDeleted:                                #for more than one deleted files                   
            eachfile = i.strip()
            rm = 'git rm ' + eachfile                        #adding all deleted files to staging area
            os.system(rm)             
        os.system('git add .')                               #adding all new files 
        commit = 'git commit -am ' + "'" + eachfile + "'"    #adding modified files
        os.system(commit)
        time.sleep(5)                                        #delay in seconds
    
    else:    
        os.system('git add .')
        os.system("git commit -am 'added all files'")



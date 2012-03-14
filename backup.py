import os,time
from subprocess import Popen, PIPE
eachfile = ''
if not os.path.exists('.git'):
    os.system('git init')

while True:
    bashout = Popen('git status',shell=True, stdout=PIPE).stdout.readlines()
    
    """captures git status and next 'if' statement checks status of git commit """

    if not bashout[1].strip() == 'nothing to commit (working directory clean)':
        userDeleted = Popen('git ls-files --deleted',shell=True, stdout=PIPE).stdout.readlines()
        for i in userDeleted:
            eachfile = i.strip()
            rm = 'git rm ' + eachfile
 #           print eachfile
            os.system(rm)                      # git rm files
        os.system('git add .')   
        commit = 'git commit -am ' + "'" + eachfile + "'"
#        print commit
        os.system(commit)
        time.sleep(5)
    
    else:    
        os.system('git add .')
        os.system("git commit -am 'added all files'")



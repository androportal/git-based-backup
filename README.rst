Introduction
============
This script will check periodically the status of a git repository and add/rm 
files based on any change made by user in that directory. It is an
attempt to use git as incremental backup tool. User can select a restore point
based on periodic commits.


Packages required
-----------------

 #. git 

 #. python, PyQt, pyuic4



Usage
-----
Just run the script by 
:: 
 
    python backup.py destination-Directory-Path  (to start backup process)

:: 
 
    python restore.py                            (a calender to select restore date) 


License
-------
GNU GPLV3


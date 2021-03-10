import os
import shutil
#source=input("enter the folder you wish to move")
source= ("/Users/divyanshsmac/desktop/DIVYANSH")
dest=("/Users/divyanshsmac/desktop/DIVYANSH2")
source= source+'/'
dest=dest+'/'
allfiles=os.listdir(source)
for file in allfiles:
    shutil.copy((source+file),dest)
import os
import random
import glob
cwd = os.getcwd()
cwd = cwd.replace("\\", "\\\\")

done = 'n'
q = '"'
while (done == 'n'):
    print ("to pate from your clip board, click the top left icon > edit > paste\n")
    direc = input("paste your (base) directory: ")
    fold = input("What folder: ")
    done = 'y'
    break

dirlist = os.listdir(direc)
dirlist = dirlist + "/" + fold
with open('filenames.txt', 'w') as f:
    for item in dirlist:
        if (item == 'clicky2.html' or item == "eromanga.jpg" or item == 'GetFiles.py' or item == 'filenames.txt'):
            print ("Skipping")
        else:
            f.write (q + fold + "/" + "%s" % item + q + ", ")
            print("Writing file")
            

import sys

yesAnswers = {'y', 'yes'}

answer = input("Is this common parent folder of each director where files will be processed? y/n...")

if answer.lower() not in yesAnswers:
	print('Exiting...')
	sys.exit()
print('Preparing to move Files...')

import shutil
import os

currDir = os.getcwd()
print('Current Dir: ', currDir)

def mover():
    sourceFolder = input('\nEnter the SOURCE folder on top of current directory:\n  '+currDir+"/")
    finalSource = currDir+"/"+sourceFolder+"/"

    while not os.path.exists(finalSource):
        print(finalSource + '  <----- Does NOT exist! *** \n ')
        sourceFolder = input('  Re-Enter the SOURCE folder that is ON TOP of the current directory:\n  '+currDir + "/")
        finalSource = currDir+"/"+sourceFolder+"/"

    print('\nFinal Source: ', finalSource)

    destFolder = input('\nEnter the DESTINATION folder on top of current directory: \n  '+currDir+"/")
    finalDest = currDir+"/"+destFolder+"/"
    print(finalDest)

    if not os.path.exists(finalDest):
        answer = input('Folder '+destFolder+' does NOT exist; create it? y/n... ')
        if answer.lower() not in yesAnswers:
            print('Exiting...')
            sys.exit()
        else:
            os.makedirs(finalDest)
            print('Folder '+destFolder+' created...\n')
    else:
        print('Directory exists. Moving files...')

    print('\nFinal Destination: ', finalDest, '\n')

    fileCount = 0
    files = os.listdir(finalSource)
    for f in files:
        if "x" in f:
            shutil.move(finalSource + f, finalDest)
            print(f, ' moved')
            fileCount += 1
        #else:
            #print(f, ' not moved')

    print('Moved '+str(fileCount)+' files.')

mover()

continueMoving = input('Move another folder in current directory? y/n... ')
while(continueMoving in yesAnswers):
    mover()


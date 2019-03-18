import os
import csv
from datetime import datetime
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='the file path of name changes. optional - if not provided, the script will ask for input')
parser.add_argument('-f', '--fileNameCSV', help='the CSV file of name changes. optional - if not provided, the script will ask for input')
parser.add_argument('-m', '--makeChanges', help='Enter "true" to if the script should actually rename the files (otherwise, it will only create a log of the expected file name changes). optional - if not provided, the script will to "false"')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter the directory of the files to be renamed: ')
if args.fileNameCSV:
    fileNameCSV = args.fileNameCSV
else:
    fileNameCSV = input('Enter the CSV file of name changes (including \'.csv\'): ')
if args.makeChanges:
    makeChanges = args.makeChanges
else:
    makeChanges = input('Enter "true" to if the script should actually rename the directories (otherwise, it will only create a log of the expected directory name changes): ')

startTime = time.time()
print(startTime)
f = csv.writer(open('renameLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','w'))
f.writerow(['oldLocation'] + ['newLocation'])
for root, dirs, files in os.walk(directory, topdown=False):
    for dir in dirs :
        print(dir)
        with open(fileNameCSV) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                oldFolder = row['oldFolder']
                newFolder = row['newFolder']
                if dir == oldFolder:
                    oldPath = os.path.join(root,dir)
                    newPath = os.path.join(root,newFolder)
                    f.writerow([oldPath] + [newPath])
                    if makeChanges == 'true':
                        os.rename(oldPath,newPath)
                    else:
                        print('log of expected directory name changes created only, no files renamed')

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print('Total script run time: ', '%d:%02d:%02d' % (h, m, s))

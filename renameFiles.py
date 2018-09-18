import os
import csv
from datetime import datetime
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='the directory of the files to be renamed. optional - if not provided, the script will ask for input')
parser.add_argument('-f', '--fileNameCSV', help='the CSV file of name changes. optional - if not provided, the script will ask for input')
parser.add_argument('-m', '--makeChanges', help='Enter "true" to if the script should actually rename the files (otherwise, it will only create a log of the expected file name changes). optional - if not provided, the script will to "false"')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = raw_input('Enter the directory of the files to be renamed: ')
if args.fileNameCSV:
    fileNameCSV = args.fileNameCSV
else:
    fileNameCSV = raw_input('Enter the CSV file of name changes (including \'.csv\'): ')
if args.makeChanges:
    makeChanges = args.makeChanges
else:
    makeChanges = raw_input('Enter "true" to if the script should actually rename the files (otherwise, it will only create a log of the expected file name changes): ')

startTime = time.time()
f=csv.writer(open('renameLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['oldFilename']+['newFilename'])
for root, dirs, files in os.walk(directory, topdown=True):
    for file in files:
        with open(fileNameCSV) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                oldFilename = row['file']
                newFilename = row['newFile']
                if file == oldFilename:
                    print oldFilename
                    oldPath = os.path.join(root,file)
                    newPath = os.path.join(root,newFilename)
                    f.writerow([oldPath]+[newPath])
                    if makeChanges == 'true':
                        os.rename(oldPath,newPath)
                    else:
                        print 'log of expected file name changes created only, no files renamed'

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)

import os
import csv
from datetime import datetime
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-1', '--primaryFilePath', help='the primary file path (C:/Test/). optional - if not provided, the script will ask for input')
parser.add_argument('-2', '--secondaryFilePath', help='the secondary file path (C:/Test/). optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.primaryFilePath:
    key = args.primaryFilePath
else:
    primaryFilePath = raw_input('Enter primary file path (C:/Test/): ')
if args.secondaryFilePath:
    key2 = args.secondaryFilePath
else:
    secondaryFilePath = raw_input('Enter secondary file path (C:/Test/): ')

startTime = time.time()
f=csv.writer(open('filesMissingFromSecondaryDirectory'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['directory']+['file'])
f2=csv.writer(open('filesMissingFromPrimaryDirectory'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f2.writerow(['directory']+['file'])
primaryFilePathDict = {}
for root, dirs, files in os.walk(primaryFilePath, topdown=True):
    for file in files:
        primaryFilePathDict[file] = root
secondaryFilePathDict = {}
for root, dirs, files in os.walk(secondaryFilePath, topdown=True):
    for file in files:
        secondaryFilePathDict[file] = root

for k, v in primaryFilePathDict.items():
    if k in secondaryFilePathDict:
        pass
    else:
        f.writerow([v]+[k])

for k, v in secondaryFilePathDict.items():
    if k in primaryFilePathDict:
        pass
    else:
        f2.writerow([v]+[k])

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)

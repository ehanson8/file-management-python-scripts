import os
import csv
from datetime import datetime

filePath = raw_input('Enter file path: ')

f=csv.writer(open(filePath+'renameLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['oldLocation']+['newLocation'])
for root, dirs, files in os.walk(filePath, topdown=True):
    for dir in dirs:
        with open('FolderNames.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                oldFolder = row['oldFolder']
                newFolder = row['newFolder']
                if dir == oldFolder:
                    oldPath = os.path.join(root,dir)
                    newPath = os.path.join(root,newFolder)
                    f.writerow([oldPath]+[newPath])
                    os.rename(oldPath,newPath)

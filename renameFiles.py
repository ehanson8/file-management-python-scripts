import os
import csv
from datetime import datetime
import time

filePath = raw_input('Enter file path (C:/Test/): ')
nameChangeFile = raw_input('Enter name of CSV with name changes: ')

startTime = time.time()
f=csv.writer(open('renameLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['oldFilename']+['newFilename'])
for root, dirs, files in os.walk(filePath, topdown=True):
    for file in files:
        with open(nameChangeFile) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                oldFilename = row['file']
                newFilename = row['newFile']
                if file == oldFilename:
                    print oldFilename
                    oldPath = os.path.join(root,file)
                    newPath = os.path.join(root,newFilename)
                    f.writerow([oldPath]+[newPath])
                    #Uncomment the following line to acutally rename files rather than just writing a log file of the changes to be made
                    #os.rename(oldPath,newPath)

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)

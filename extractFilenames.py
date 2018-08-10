import csv
import os
import time

filePath = raw_input('Enter file path (C:/Test/): ')
fileExtension = raw_input('Enter file extension: ')
prefix = raw_input('Enter prefix to be added: ')

startTime = time.time()
f = csv.writer(open('fileListing.csv', 'wb'))
f.writerow(['file'] + ['newFile'])
f2 = csv.writer(open('fullfileListing.csv', 'wb'))
f2.writerow(['file'] + ['newFile'])
directories = os.walk(filePath, topdown=True)
for root, dirs, files in directories:
    for file in files:
        f2.writerow([file])
        if file[-3:] == fileExtension:
            itemID = file[0:5]
            newFile = prefix + itemID + fileExtension
            f.writerow([file] + [newFile])

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)

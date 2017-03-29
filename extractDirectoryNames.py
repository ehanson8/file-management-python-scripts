import csv
import os

filePath = '[Enter File Path]'
f = csv.writer(open('directoryListing.csv', 'wb'))
f.writerow(['folder'])
directories = os.walk(filePath, topdown=True)
for root, dirs, files in directories:
    f.writerow([root])

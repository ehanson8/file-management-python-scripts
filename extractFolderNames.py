import csv
import os

filePath = input('Enter file path (C:/Test/): ')

f = csv.writer(open('directoryListing.csv', 'w'))
f.writerow(['folder'])
directories = os.walk(filePath, topdown=True)
for root, dirs, files in directories:
    f.writerow([root])

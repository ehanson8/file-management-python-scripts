from __future__ import division
import os
import shutil
import csv
from datetime import datetime
import itertools

filePath = raw_input('Enter file path (C:/Test/): ')

f=csv.writer(open('sampledLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['oldLocation']+['newLocation'])

for root, dirs, files in os.walk(filePath, topdown=True):
    print root
    print files
    sampledFiles = itertools.islice(files, 1, None, 10)
    for sampledFile in sampledFiles:
        print sampledFile
        oldLocation = os.path.join(root, sampledFile)
        project = root[root.rfind('/')+1:]
        root1 = root[:root.rfind('/')]
        root2 = root1[:root1.rfind('/')]
        newLocation = os.path.join(root2, 'sampled', project)
        if not os.path.exists(newLocation):
            os.makedirs(newLocation)
        newLocation = os.path.join(newLocation, sampledFile)
        print oldLocation
        print newLocation
        f.writerow([oldLocation]+[newLocation])
        shutil.move(oldLocation, newLocation)
    oldUnsampledLocation = os.path.join(root)
    if oldUnsampledLocation != filePath:
        project = root[root.rfind('/')+1:]
        root1 = root[:root.rfind('/')]
        root2 = root1[:root1.rfind('/')]
        newUnsampledLocation = os.path.join(root2, 'unsampled', project)
        shutil.move(oldUnsampledLocation, newUnsampledLocation)

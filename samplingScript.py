from __future__ import division
import os
import shutil
import csv
from datetime import datetime

filePath = '[Enter File Path]'
f=csv.writer(open('sampledLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['oldLocation']+['newLocation'])
f2=csv.writer(open('unsampledLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f2.writerow(['oldLocation']+['newLocation'])

for root, dirs, files in os.walk(filePath, topdown=True):
    print root
    number = 1
    while number < len(files):
        oldLocation = os.path.join(root, files[number])
        project = root[root.rfind('/')+1:]
        root1 = root[:root.rfind('/')]
        root2 = root1[:root1.rfind('/')]
        newLocation = os.path.join(root2, 'sampled', project)
        if not os.path.exists(newLocation):
              os.makedirs(newLocation)
              print newLocation
        newLocation = os.path.join(newLocation, files[number])
        print oldLocation
        print newLocation
        f.writerow([oldLocation]+[newLocation])
        number = number + 10
        shutil.move(oldLocation, newLocation)
    oldUnsampledLocation = os.path.join(root)
    if oldUnsampledLocation != filePath:
        project = root[root.rfind('/')+1:]
        root1 = root[:root.rfind('/')]
        root2 = root1[:root1.rfind('/')]
        newUnsampledLocation = os.path.join(root2, 'unsampled', project)
        print oldUnsampledLocation
        print newUnsampledLocation
        f2.writerow([oldUnsampledLocation]+[newUnsampledLocation])
        shutil.move(oldUnsampledLocation, newUnsampledLocation)

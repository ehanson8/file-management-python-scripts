import os
import shutil
import csv
from datetime import datetime

filePath = input('Enter file path (C:/Test/): ') + '/'

f = csv.writer(open('moveLog' + datetime.now().strftime('%Y-%m-%d %H.%M.%S')
               + '.csv', 'w'))
f.writerow(['oldLocation'] + ['newLocation'])
print(filePath)
for root, dirs, files in os.walk(filePath, topdown=True):
    for name in files:
        if os.path.join(root, name).count('/') > 8:
            level0 = root.index('/') + 1
            level1 = root.index('/', level0) + 1
            level2 = root.index('/', level1) + 1
            level3 = root.index('/', level2) + 1
            level4 = root.index('/', level3) + 1
            level5 = root.index('/', level4) + 1
            level6 = root.index('/', level5) + 1
            level7 = root.index('/', level6) + 1
            oldLocation = os.path.join(root, name)
            print(oldLocation)
            newLocation = root[:level7] + name
            print(newLocation)
            shutil.move(oldLocation, newLocation)
        f.writerow([oldLocation] + [newLocation])

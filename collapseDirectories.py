import os
import shutil
import csv
from datetime import datetime

filePath = raw_input('Enter file path: ')

f=csv.writer(open(filePath+'moveLog'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv','wb'))
f.writerow(['oldLocation']+['newLocation'])
for root, dirs, files in os.walk(filePath, topdown=True):
    for name in files:
        if os.path.join(root, name).count('/') > 9:
            level1 = root.index('/')+1
            level2 = root.index('/', level1)+1
            level3 = root.index('/', level2)+1
            level4 = root.index('/', level3)+1
            level5 = root.index('/', level4)+1
            level6 = root.index('/', level5)+1
            level7 = root.index('/', level6)+1
            level8 = root.index('/', level7)+1
            level9 = root.index('/', level8)+1
            oldLocation = os.path.join(root, name)
            print oldLocation
            newLocation = root[:level9]+name
            print newLocation
            shutil.move(oldLocation, newLocation)
	    f.writerow([oldLocation]+[newLocation])

import hashlib
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='the directory of the files. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = raw_input('Enter directory (C:/Test/): ')

fileList = []
for root, dirs, files in os.walk(directory, topdown=True):
    for file in files:
        fileList.append(os.path.join(root, file).replace('\\','/'))

f = open('checksum.md5','wb')

for file in fileList:
    fileName = file[file.rindex('/')+1:]
    print fileName
    file = open(file,'rb').read()
    checksum = hashlib.md5(file).hexdigest()
    f.write(checksum+'  '+fileName+'\n')

import os
import zipfindandextract

p = ''

while os.path.exists(p) is False:
    p = input('Valid Instance Path: ')
    p = p.strip("\"")

zfolder, instance = zipfindandextract.find(p)

zipfindandextract.extract(zfolder, instance)
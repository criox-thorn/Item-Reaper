import os
import stat
from shutil import copytree, copy
import datetime as dt
from zipfile import ZipFile

cwd = os.getcwd()

def find(master=str):
    instance = master.split("\\")[-1]
    zipfolder = f"{cwd}\ZIP-{instance}"
    os.makedirs(zipfolder)
    print("Copying Mods")
    copytree(master+"\\mods", zipfolder, dirs_exist_ok=True)
    print("Copied")
    return zipfolder, instance

def extract(internal, instance):
    instance = internal.split("-")[-1]
    extractfolder = f"{cwd}\EXT-{instance}"
    os.makedirs(extractfolder)
    print("Extracting")
    for mod in os.listdir(internal):
        print(f"Extracting: {mod}")
        with ZipFile(internal + "\\" + mod, 'r') as zf:
            print(zf.infolist())
            for file in zf.namelist():
                if file.startswith('data/'):
                    zf.extract(file, path=extractfolder)


            zf.close()

    print("Deleting .jar")
    for f in os.listdir(internal):
        print(f'Deleting {f}')
        os.remove(internal+'\\'+f)
    os.chmod(internal, 0o777)
    os.remove(internal)
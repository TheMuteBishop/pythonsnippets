import os
import sys
'''
This script will rename every file in given folder and sub folders
with given file extension
e.g. change filename from README.md to README.txt
'''
def get_rootdir():
    while True:
        root = input('Enter full path of folder : \n')
        if os.path.exists(root):
            return os.path.abspath(root)
        else:
            print(root + ' not found.\n')
def get_extention():
    return input('Enter Extention : \n')
            
def rename_files(rootdir, ext):
    for root, subdirs, files in os.walk(rootdir):
        print('--\nroot = ' + root)
        for file in files:
            
            if not file == 'convert.py':
                print('\trenaming : ' + file)
                file_path = os.path.join(root, file)
                dest_file = file_path.split('.')[0] + '.' + ext
                os.rename(file_path , dest_file)

if __name__ == '__main__':
    rootdir = get_rootdir()
    ext = get_extention()
    rename_files(rootdir, ext)

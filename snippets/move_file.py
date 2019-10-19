import os


"""
Script to organize file into folders based on file type.
It moves similar files into target folder with parent directory structure.
"""
def get_rootdir(directory):
    while True:
        root = input('Enter full path of ' + directory+ ' folder : \n')
        if os.path.exists(root):
            return os.path.abspath(root)
        else:
            print(root + ' not found.\n')
def organise(src, target):            
    for root, subdirs, files in os.walk(src):
        print('\nroot = ' + root)
        for file in files:
            
            if not file == 'convert.py':
                print('\tmoving : ' + file)
                file_path = os.path.join(root, file)
                if file.split('.')[-1] == 'py':
                    tr = root.replace(src , '').replace('\\' , '')
                    if not os.path.exists(os.path.join(target,'Python', tr)):
                        os.makedirs(os.path.join(target,'Python', tr))
                    trgt_file = os.path.join(target,'Python', tr,file)
                    if os.path.exists(trgt_file):
                        choice = input(trgt_file + ' exists. Press Y to replace : ')
                        if choice.upper() == 'Y':
                            os.remove(trgt_file)
                    else:
                        try :
                            os.rename(file_path , trgt_file)
                        except:
                            print("Coul'd not move " + trgt_file)
    # Delete parent directory
    try:
        os.rmdir(src)
    except:
        print( src + ' is not empty')
                    
if __name__ == '__main__':
    src = get_rootdir('source')
    trgt = get_rootdir('destination')
    organise(src, trgt)


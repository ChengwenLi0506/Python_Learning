from os import listdir, remove, removedirs
from os.path import isdir, isfile, join
import shutil

path = "C:\localsymbols"

def work():
    print('-'*80)
    print('start to work')

    all_items = listdir(path)
    print(all_items.__len__())

    for item in all_items:
        if (isdir(join(path, item)) and item.endswith('.dll')):
            print(item)
            shutil.rmtree(join(path, item))

if __name__ == '__main__':
    work()





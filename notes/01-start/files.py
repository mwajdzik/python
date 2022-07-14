import datetime
import os
import shutil
import time
from os import path
from zipfile import ZipFile


def main():
    # w+, a+, r

    f = open('textfile.txt', 'w+')

    for i in range(10):
        f.write('This is line %d\n' % (i + 1))

    f.close()

    with open('textfile.txt', 'r') as f:
        # f.readline()
        # read until empty line found
        for line in iter(f.readline, ''):
            print(line.strip())


    print('\n-------------------------------------\n')

    print('OS name: ' + os.name)
    print('Item exists: ' + str(path.exists('textfile.txt')))
    print('Item is a file: ' + str(path.isfile('textfile.txt')))
    print('Item is a directory: ' + str(path.isdir('textfile.txt')))

    print('Item\'s path: ' + str(path.realpath('textfile.txt')))
    print('Item\'s path and name: ' + str(path.split(path.realpath('textfile.txt'))))

    print(time.ctime(path.getmtime('textfile.txt')))
    print(datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('textfile.txt'))
    print('It has been ' + str(td) + ' since the file was modified.' + ' Or, ' + str(td.total_seconds()) + ' seconds')

    print('\n-------------------------------------\n')

    if path.exists('textfile.txt'):
        src = path.realpath('textfile.txt')
        dst = src + '.bak'

        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        os.rename('textfile.txt', 'newfile.txt')

        root_dir, tail = path.split(src)
        shutil.make_archive('archive', 'zip', root_dir)

        with ZipFile('testzip.zip', 'w') as newzip:
            newzip.write('newfile.txt')
            newzip.write('textfile.txt.bak')

        os.remove(path.realpath('testzip.zip'))
        os.remove(path.realpath('archive.zip'))
        os.remove(path.realpath('textfile.txt.bak'))
        os.remove(path.realpath('newfile.txt'))


if __name__ == '__main__':
    main()

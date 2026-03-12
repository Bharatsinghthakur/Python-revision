# os module 
import os 
from datetime import datetime

# print(dir(os))

# getcwd() -- get current working directory
print(os.getcwd())

# listdir() -- files and folders inside that directory

print(os.listdir())

# mkdir() , makedirs()  --- create a new folder on directory and deep level path will be created for us
'''
os.mkdir()
os.makedirs() ## to create tree structure

# rmdir() , removedirs() -- remove the directory and will deleted the deep level 

os.rmdir()
os.removedirs()''' 

#  os.rename() -- to rename the directory 
os.rename('test.txt','test.txt')


# os.stat() -- It prints out all the information about the file
print(os.stat('test.txt'))
print(datetime.fromtimestamp(os.stat('test.txt').st_atime))

# modified time for file can be changes
mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# os.walk -- generator that yield of tuple as three values for each directory direcotry within that [ath ]
#    'Current Path:',dirpath
#     Directories:',dirnames
#    'Files',filenames
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:',dirpath)
    print('Directories:',dirnames)
    print('Files',filenames)


# extermely usesful when search something which we forgot to track

# os.environ - to access home environment variable

print(os.environ.get('Scripts'))

# file_path = os.environ.get('home') + 'test.txt' # easy to forget



# os.path() -- can we used many ways

path = os.path.join(os.environ.get('home') ,'test.txt')
print(path)


# os.path.dirname()
# os.path.basename() - It provides the basename
# os.path.split() - IT provides both basename & dirname
# os.path.exists - It provides boolean value either that path exist or not
# os.path.isdir() - it provides boolean value either the file is direcory or not
# os.path.split() - it will provide the root of the file path and extension in split
# os.path.isfile() - it provides the boolean value if it is a file


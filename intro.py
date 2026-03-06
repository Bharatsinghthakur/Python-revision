# importing file from same directory
import my_module as mm

# import system directory
import sys

# importing particular function
from my_module import find_index , test

# diff directory module 
import myfile.import_module
courses = ['History','Math','Physics','CompSci']

# this approch maybe only give us access to find index function not anything else
# if we need more functions we can specify them separting through commas
index = find_index(courses,'Physics')
print(index)
print(test)
print(sys.path)

# when we run sys.path we get information 
# 1 directory that contains script we are running 
# 2 python path environment variable
# 3 python standard library directory
# 4 site packages , or third party packages

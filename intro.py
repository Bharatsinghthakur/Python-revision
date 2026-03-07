# importing file from same directory
import my_module as mm
import random
import math
import datetime
import calendar
import os
# import system directory
import sys


# importing particular function
from my_module import find_index , test

# diff directory module 
import myfile.import_module
from myfile.import_module import my_function_import
courses = ['History','Math','Physics','CompSci']
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

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


''' we are importing our function from diffrent module'''
my_function_import()


print(os.getcwd())
print(os.__file__)



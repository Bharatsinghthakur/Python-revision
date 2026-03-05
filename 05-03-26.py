# iteration through range function
for i in range(10):
    print(i)

# if we want to start the range function from particular number

for i in range(1,11):
    print(i)


# functions
#functions are basically instructions packaged together to perform some specific Task

# def hello_func():
#    return 'Hello Function'
# hello_func()

# print(hello_func())

# Function are like black box they are there to take input and produce output

# print(hello_func().upper())

def hello_func(greeting,name="you"):
    return '{},{}'.format(greeting,name)

print(hello_func('Hey !','corey'))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Physics']  # we can pass arbitray values of these in parameter as well
info = {'name':'John','age':25}

student_info(*courses , **info) # unpacking the values of courses and info 

# number of days per month . First value placeholder for indexing purposes.
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    ''' Return True for leap year , False for non-leap years'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):

    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2017,3))

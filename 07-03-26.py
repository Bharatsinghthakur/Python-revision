# scope in python 
import builtins
print(dir(builtins))
'''
LEGB
LOCAL , ENCLOSING , GLOBAL , BUILD IN  - abbrevation
'''
x = 'global x'

def test():
    y = 'Local y'
    print(y) # this variable is local to function
    print(x) # python will check x exist in function if not then check if it exist outside of function
test()
print(x)

def test_2():
    x = 'local x'
    print(x)
test_2()
print(x)


# This is the case where we want to use the external global variable

def test_3():
    global x # here we have used global varibale and changed its value
    x = 'local x '
    print(x)
test_3()
print(x) # value printed here would be changed as we made changes inside function for global variable



# build in function scenrio

def min(x):
    pass

m = [1,4,5,2,3]
print(min(m))
# basically it overwrites the build in function that is bad for our 


# ENCLOSING - inner and outer function scope

def outer():
    x = 'outer x ' 

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()


# As we use global variable we cannot use that in function it can disrubt the global environmnet

def outer():
    x = 'outer x'

    def inner():
        nonlocal x # this will pick nonlocal scope variable that can be useful from outer function
        x = 'inner x'
        print(x)
    
    inner()
    print(x) # value of x will be changed here overwritten the outer x value

outer()
# decorators

''' a decorator is a function that takes another function 
as a argument adds some kind of functionality and then returns another
function all this without altering the source code of the original function
'''

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

def display():
    print('Display function ran')

decorated_display = decorator_function(display)

decorated_display()

# both are same functions
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display with new deco syntax function ran')


# we can add multiple functions as decorator for decorator_function
@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
display_info('Jack',3)


# convert the same function into class

#class decorator
'''
class decorator_class(object):
    def __init__(self,orginal_function):
        self.original_function = orginal_function
    
    def __call__(self,*args,**kwargs):
        print('__call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)
        
@decorator_class
def display():
    print('display with new deco syntax function ran')

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
display_info('decoratorclass',25)

'''


# logger decorator

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and Kwargs: {}'.format(args,kwargs)
        )
        return orig_func(*args,**kwargs)
    return wrapper

@my_logger
def display():
    print('display with new deco syntax function ran')

@my_logger
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
display_info('Jack',3)


# timer with decorator 

def my_timer(orig_func):
    import time

    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper


import time

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
display_info('Jack',3)

'''
This means that 
display_info = mylogger(my_timer(display_info))
display_info

my timer will execute first then mylogger
'''
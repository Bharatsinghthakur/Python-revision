# Closure in python

'''
Wikipedia says : " A closure is a record storing a function together with an environment
a mapping associating each free variable of the function with the value or storage location to 
which the name was bound when the closure was created. A closure , unlike
a plain function , allows the fucntion to access those captured variable through 
closure's reference to them, even when the function is invoked outside their 
scope

'''

def outer_function(msg):
    # message = "Hi"
    message = msg
    def inner_func():
        print(message)
    
    return inner_func

hi_func = outer_function('Hi')
hello_func = outer_function('Hello')

hi_func()
hello_func()


def html_tag(tag):
    
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

print_h1 = html_tag('h1')

print_h1('Test Headline !')
print_h1('another headline')

print_p = html_tag('p')
print_p('Test Paragraph !')


import logging 

logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))

    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10, 5)
sub_logger(20,10)

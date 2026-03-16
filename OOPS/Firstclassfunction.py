# first Class function 
'''
A programming language is said to have first class functions if it treats function 
as First class citizens

First class citizens - A first class citizens (sometimes called first-class objects) in a 
programming language is a entity which supports all the operations genrally available to 
other entities.
            These operations typically include being passed as an argument , returned 
            from a function and assigned to a variable.

'''

# Higher order function

def square(x):
    return x * x 
f = square
print(square)
print(f(5))


def cube(x):
    return x * x * x

def my_map(func , arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

cubes = my_map(cube, [1,2,3,4,5])
print(cubes)

def logger(msg):
    def log_message():
        print('Log:',msg)
    return log_message

log_hi = logger('Hi')
log_hi()

def html_tag(tag):
    def wrap_tag(msg):
        print('<{0}>{1}<{0}>'.format(tag,msg))
    
    return wrap_tag

print_h1 = html_tag('h1')
print_h1('test headline')
print_h1('another headline')

print_p = html_tag('p')
print_p('Test paragraph!')
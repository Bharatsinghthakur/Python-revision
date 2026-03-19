# python LEGB

# local enclosing global build-in 

# x = 'global x '

# def test():
#     global x 
#     x = 'local x'
#     print(x)
# test()
# print(x)
# import builtins
# print(dir(builtins))

# global function overwritten the built in funciton that why we are getting error
# def min():
#     pass


# m = min([2,5,3,1,8])
# print(m)

# def test(z):
#     x = 'local x'
#     print(z)

# test('local Z')


# nested function has enclosing scope -- local scope , global scope

def outer():
    x = 'outer x'
    def inner():
        x = 'inner x '
        print(x)    
    inner()
    print(x)
outer()

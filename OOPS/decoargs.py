# decorator with parameter

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix,"Executed Before", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix,"Executed after", original_function.__name__, "\n")
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('log')
def display_info(name,age):
    print('display_info ran with arguments({}, {})'.format(name,age))

display_info('John',25)
display_info('jack',4)

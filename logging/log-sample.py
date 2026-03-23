import logging
import employee

"""
# Debug: Detailed information, typically of interest only when diagnosing problems.

#Info: Confirmation that things are working as expected

# Warning: An indication that something unexpected happend, or indicative of some problem in the near future (e.g 'disk space low').
The software is still working as expected

# Error: due to a more serious problem , the software has not been able to perform some function.

# Critical : A serious error , indicating that the program itself may be unable to continue running.

"""

# setting configuration so we dont disturb root logger
# To set the file name to file which runs
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# formatter for log file 
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
# for filehandler not the root logger
file_handler = logging.FileHandler('sample.log')

# to set the levels on file handler
file_handler.setLevel(logging.ERROR)

# add formatter to file handler
file_handler.setFormatter(formatter)

# we have to add this handler to logger
# logger.addHandler(file_handler)

# AS WE ARE USING THIS CONFIGURATION REMEBER TO USE THE SPECIFIC LOGGER - logger

# logging.basicConfig(
#     filename="test.log",
#     level=logging.DEBUG,
#     format="%(asctime)s:%(levelname)s:%(message)s",
# )

#stream handler 
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)




def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    # return x / y
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result
        
num_1 = 20
num_2 = 0

# default level is set to warning & above .


add_result = add(num_1, num_2)
logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug("Subtract: {} + {} = {}".format(num_1, num_2, sub_result))

mul_result = add(num_1, num_2)
logger.debug("Mul: {} + {} = {}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug("Div: {} + {} = {}".format(num_1, num_2, div_result))

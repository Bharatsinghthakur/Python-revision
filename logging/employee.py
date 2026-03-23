import logging

# To set the file name to file which runs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# formatter for log file 
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
# for filehandler not the root logger
file_handler = logging.FileHandler('employee.log')

# add formatter to file handler
file_handler.setFormatter(formatter)
# we have to add this handler to logger
logger.addHandler(file_handler)

# not required
# logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(levelname)s:%(message)s')

class Employee:

    def __init__(self,first,last):
        self.name = first
        self.surname = last

        # logging.info('Created Employee : {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee : {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name,self.surname)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.name,self.surname)
    

emp_1 = Employee('Jack','Singh')
emp_2 = Employee('NEO','Singh')
emp_3 = Employee('billu','Singh')

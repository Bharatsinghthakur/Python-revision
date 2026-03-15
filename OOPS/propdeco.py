# property Decorator - getter , setter and Deleters
class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + '@company.com'
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    #getter
    @property
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    #setter
    @fullname.setter
    def fullname(self, name):
        first , last = name.split(' ')
        self.first = first
        self.last = last
    #deleter
    @fullname.deleter
    def fullname(self):
        print('DELETE NAME!')
        self.first = None
        self.last = None

    
emp_1 = Employee('jack','Smith')

emp_1.first = 'NEO'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email) # now as we have to run it as a function we 
print(emp_1.fullname)
del emp_1.fullname
emp_1.fullname = "jack Singh"
print(emp_1.fullname)

# we can avoid this problem by using @property decorator
# in class methods 


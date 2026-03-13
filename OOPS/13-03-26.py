# Python Object-Oriented Programming

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
   
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # both will work
        # self.pay = int(self.pay * Employee.raise_amount)

''' so whenever we want to access these class variable we need to acess them either through Class itself or 
    instance of the class
'''



'''
emp_1 = Employee()
emp_2 = Employee()

emp_1.first = "bharat"
emp_1.last = 'singh'
emp_1.email = "bharat.singh@mail.com"
emp_1.pay = 100000

emp_2.first = "niko"
emp_2.last = 'singh'
emp_2.email = "Niko.singh@mail.com"
emp_2.pay = 1000000000
print(emp_1.email,emp_2.email)

'''

# manually set these variable prone to errors 

class_emp1 = Employee('Jack','Singh',5000)
class_emp2 = Employee('Niko','Singh',8000)

print(class_emp1, class_emp2.email)
print('{}{}'.format(class_emp1.first,class_emp1.last))
print(class_emp1.fullname()) # not required anything because we are calling out from instance of class then method

# here we are calling out class directory and then its method requires instance -- here its passed as self as an instance
print(Employee.fullname(class_emp1)) # will require instance as argument to known for which we are calling out

print(class_emp1.apply_raise())


# lets create how to access class variables

print(class_emp1.raise_amount) # instance access
print(Employee.raise_amount)   # class access


# now check some important things
print(class_emp1.__dict__)
print(Employee.__dict__)

# this will work because it will be created inside the instance of the class
class_emp1.raise_amount = 1.05
print(class_emp1.__dict__)

print(Employee.num_of_emps)
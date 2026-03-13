# Python Object-Oriented Programming

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
   
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
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

# lets create a methi
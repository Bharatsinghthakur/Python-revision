# Regular Method , Class method and static method

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first , last , pay = emp_str.split('-')
        return  cls(first,last,pay)  # insted of employee class
    
    # static methods 
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


    
class_emp_1 = Employee('jack','singh',5000)
class_emp_2 = Employee('niko','singh',6000)

# using class method 
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(class_emp_1.raise_amt)
print(class_emp_2.raise_amt)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-5000'

## customer wants to have employee form the strings


# first , last , pay = emp_str_1.split('-')
# new_emp_1 = Employee(first,last,pay)

## Now this approch is little wired to parse everytime the string and 
## split it into instance


## Class Method as Constructor

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2026,3,21)

print(Employee.is_work_day(my_date))


''' The giveaway to know its a static method is class shouldn't be
accessed inside the method or function 
because they dont take class or instance as first arguments 
they dont operate on instance or class
'''
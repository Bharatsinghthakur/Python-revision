#SORTING IN PYTHON 

li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Varible:\t', s_li)

li.sort()

print('Original variable:\t', li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t',s_tup)

# dictionary

di = {'name':'corey','job':'programming','age':None,'os':'Mac'}

s_di = sorted(di)
print('Dict\t', s_di)


li = [-6,-5,-4,1,2,3]

s_li = sorted(li,key=abs)

print(s_li)

from operator import attrgetter
class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'({self.name},{self.age},${self.salary})'
    

e1 = Employee('Carl',37,70000)
e2 = Employee('jack',5,7000000)
e3 = Employee('Niko',3,9000000)

employee = [e1,e2,e3]

def e_sort(emp):
    return emp.name # we can sort on age,salary as well


# s_employee = sorted(employee,key=e_sort)
# s_employee = sorted(employee,key=lambda e:e.name,reverse=True)
s_employee = sorted(employee,key=attrgetter('age'),reverse=True)


print(s_employee)
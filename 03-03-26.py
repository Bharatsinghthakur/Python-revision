#Dictionaries

student = {'name':'Bharat','age':25,'courses':['Math','CompSci']}

student['phone'] = '555-555'
print(student['name'])
print(student['age'])
print(student['courses'])
print(student['phone'])

# Methods in Python

print(student.get('name'))
print(student.get('address','Not Found'))

student['phone'] = '777-777'
student.update({'name':'Niko','age':4,'address':'delhi'})
print(student)
print(student.get('phone'))


# delete key 

del student['address']
print(student)

#pop  - pop method is used to remove the key value pair and returns type is pair value

pop = student.pop('age')
print(pop)

print(student)

#len : to find out the length of the dictionary it gives the number of key pairs in dict


print(len(student))

# keys :It will give all the keys from the dictionary

print(student.keys())

#values : It will give all the values of the dictionary

print(student.values())

#items : It will give us the key and value pair in tuples in List

print(student.items())

#Loop in dictionary

for key in student:
    print(key)

print(student.items())
for key,values in student.items():
    print(key,values)




#########################################
# conditionals & Loops

if True:
    print('conditonals was True')


language = 'Python'

if language == "Python":
    print('conditonal was True')

'''
we have comparisons 
#equal: ==
#Not equal: !=
#Greater Than: >
#Less Than: <
#Greater or equal >=
#less or equal <=
#Object Identity: is

'''

language = 'Python'

if language == 'java':
    print('Language is Java')
elif language == 'python':
    print('language is Python')
else:
    print('No Match')


# boolean operations

#and
#or 
#not

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('admin')
else:
    print('Bad credentials')


if not logged_in:
    print('please Log In')
else:
    print('Welcome')


a = [1,2,3]
b = [1,2,3]
c = a
print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(id(c))
print(id(a))
print(id(a) == id(c))

# false Values

    # False
    # None
    # zero of any numeric type
    # any empty sequence for example '' ,{} , []
    # any emplty mapping. for example {}.

condition = {}
if condition: 
    print('Evaluated to True')
else:
    print('Evaluated to False')

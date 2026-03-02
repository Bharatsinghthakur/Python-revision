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
#len : to find out the length of the dictionary


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

# string methods for list
# join - convert the elements of a iterable into a string
# courses = ['history','Physics','Chemistry','Maths','Economics']

# courses_str = ' - '.join(courses)
# print(courses_str)

# new_list = courses_str.split(' - ')
# print(new_list)

#Tuples

#first understand the scenrio of mutablity 
#list are mutable as shown in example

# list_1 = ['a','b','c','d']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'z'

# print(list_1)
# print(list_2)


#Tuples - are immutable and we cannot modify them .Tuples can be looped

# tuple_1 = ('History','Math','Physics','compsci') 
# tuple_2 = tuple_1

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2) 


#sets

cs_courses = {'History','Math','Physics','Compsci','Math'}
print(cs_courses)

cs_courses = {'History','Math','Physics','CompSci'}
art_courses = {'History','Math','Art','Design'}

print('Math' in cs_courses)

#intersection 
print(cs_courses.intersection(art_courses))

#difference
print(cs_courses.difference(art_courses))

#union
print(cs_courses.union(art_courses))

#empty Lists
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty sets
empty_sets = {} # This is wrong as it will create dictionary
empty_sets = set()

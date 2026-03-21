# LIST TUPLES AND SETS

# LIST 
courses = ['History','Math','Physics','CompSci']
print(len(courses))
print(courses[3])

# for accessing the last index - always last index
print(courses[-1])

# for accessing index - index slicing 
print(courses[0:2])
print(courses[0:])
print(courses[:])
print(courses[:3])
print(courses[::-1])
print(courses[-1::1])


num = [1,2,3,4,5,6,7,8]
print(num[1:9:2])

# LIST METHODS

#1 append
courses.append('Arts')
print(courses)

#2 insert

courses.insert(1,"Economics")
print(courses)


#3 extend -  to extend multiple item given in the list 
lecture = ['a','b','c']
lecture_2 = ['d','e','f'] 
print(lecture.extend(lecture_2))

#4 remove 
rem = lecture.remove('c')
print(lecture,"printed lecture")
print(rem,'removed or not')

#5 pop

pop = lecture.pop()
print(lecture)
print(pop)

# sorting 
A = sorted(lecture)
print(A)
print('sorted function')
#6 reverse
courses.reverse()
print(courses)
num = [5,3,2,1,8,9]
# sort method will sort in ascending order default
num.sort()
print(num)

# for desecding order
num.sort(reverse=True)

print(num)

#7 sorted - to return the sorted value of the list


courses = ['History','Math','Physics','CompSci']
sorted_list = sorted(courses)
print(sorted_list)

#8 min - It will give the minimum of the all the list

print(min(num))

#9 max - It will give the maximum of the all the list

print(max(num))

#10 sum - It will give the sum of the list

print(sum(num))

#11 index - It helps to find out the index of the element of the list 

print(courses.index('History'))


print('Math' in courses)

print(courses)

for index ,course in enumerate(courses):
    print(index,course)
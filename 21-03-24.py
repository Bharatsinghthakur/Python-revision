# Generator
# Generator dont hold entire result in memory it yield one result at a time



# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5,6])
# print(my_nums)
# my_nums = [n*n for n in [1,2,3,4,5]]
# print(my_nums)


# def square_nums(nums):
#     for i in nums:
#         yield i*i

# my_nums = square_nums([1,2,3,4,5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# for num in my_nums:
#     print(num)

# we can also create generator comprehension

# my_nums = (x*x for x in [1,2,3,4])
# print(my_nums)
# print(list(my_nums))


import psutil
import os
import random
import time

names  = ['Jack','Neo','Niko','Nody','Moji','lucy']
majors = ['Math','Engineering','CompSci','Arts','Business']

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

print('Memory (Before):{}Mb'.format(memory_usage()))



def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id':i,
                    'name':random.choice(names),
                    'major':random.choice(majors)
                    }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                'id':i,
                'name':random.choice(names),
                'major':random.choice(majors)
                }
        yield person

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

t1 = time.time()
people = people_generator(1000000)
t2 = time.time()

print('Memory (After) : {}Mb'.format(memory_usage()))
print('Took {} Seconds'.format(t2 -t1))
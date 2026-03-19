# List comprehension

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# list comprehension
# my_list = [n for n in nums]
# print(my_list)

# I want 'n*n' for each n in nums

# my_list = []
# for n in nums:
#     my_list.append(n * n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# using map + lambda
# my_list = map(lambda n:n**n, nums)
# print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even

# my_list = []

# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2==0]
# print(my_list)

# using filter + lambda

# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)


# i want a (letter,num) pair for each letter in 'abcd' and each number in '01234'

# my_list = []

# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)


# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)


#dictionary comprehension
# names = ['Bruce','Clark','Peter','Logan','Wade']
# heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

# print (zip(names,heros))
# # I want a dict{'name','hero'} for each name, hero in zip(names, heros)
# my_dict = {}
# for name , hero in zip(names,heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {names:heros for names , heros in zip(names,heros) if (names != 'Peter')} 
# print(my_dict) 


# SET comprehension 

# nums = [1,1,2,1,3,4,4,5,5,5,9,9,8]

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print (my_set)


# my_set = {n for n in nums}
# print(my_set)

# print(*nums,'_')



# GENERATOR EXPRESSION

nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)











































# python LEGB

# local enclosing global build-in 

# x = 'global x '

# def test():
#     global x 
#     x = 'local x'
#     print(x)
# test()
# print(x)
# import builtins
# print(dir(builtins))

# global function overwritten the built in funciton that why we are getting error
# def min():
#     pass


# m = min([2,5,3,1,8])
# print(m)

# def test(z):
#     x = 'local x'
#     print(z)

# test('local Z')


# nested function has enclosing scope -- local scope , global scope

# def outer():
#     x = 'outer x'
#     def inner():
#         x = 'inner x '
#         print(x)    
#     inner()
#     print(x)
# outer()




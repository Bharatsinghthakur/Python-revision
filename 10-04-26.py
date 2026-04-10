# # tuple packing means grouping multiple values into tuple
# #implicit 
# my_tuple = (1,2,3)
# print(my_tuple)
# #explicit
# my_tuple2 = 1,2,3
# print(my_tuple2)

# # generator comprehension 


# a = [1,2,3,4,5,6,7,8]
# res = [num for num in a if num%2==0]
# print(res)

# res = [num**2 for num in range(1,6)]
# print(res)

# # dictionary comprehension
# res = {num: num**3 for num in range(1,6)}
# print(res)

# a = ["texas","california","florida"]
# b = ["austin","sacramento","tallasse"]

# res = {state:capital for state,capital in zip(a,b)}
# print(res)
# # zip = zip(a,b)
# # print(zip)
# # for a,b in zip:
# #     print(a,b)


# # zip in python 
# """ 
# no iterable -> empty list
# One iterable -> each element becomes a one-item tuple
# two iterable -> pairs elelements at matching indexes
# """

# #Iterable of diffrent lengths

# # names = ['Hiro','Mila','Tariq']
# # scores = [88,94]
# # names , scores = zip(*names)
# # print(list(res))

# a = [('Apple',10),('Banana',20),('Orange',30)]
# fruits , quantities = zip(*a)
# print("Fruits:",fruits)
# print("Quantities:",quantities)

# oops

class xmp:
   def __init__(self,name,age):
      self.name = name
      self.number = age
      vivek
      bharat

# Iterable and Iterator

''' Iterable - something that can be looped over '''
nums = [1,2,3]
print(dir(nums),"this is dir of LIST")
# i_num = nums.__iter__()

'''Iterator is an object with an state so that it remebers where it is during iteration.
Iterators also know how to get next value ie dunder  __next__() or next() method'''
# we can also use the method
# i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break



# for num in nums:
#     print(num)

# print(next(num))

class MyRange():

    def __init__(self,start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)

# for num in nums:
#     print(num)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


def my_range(start,end):
    current = start
    while current < end:
        yield current
        current += 1


my_range(1,10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)

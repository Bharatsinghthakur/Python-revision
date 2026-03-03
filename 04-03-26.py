#Loops

nums = [1,2,3,4,5]

for num in nums:
    print(num)

# break statement will break the loop and come out of it
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)


#Continue will continue the iteration of the loop 

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)


nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc':
        print(num,letter)


# we have range function which helps when we want to go to loop certain number of times

for num in range(1,11):
    print(num)



# While loop

x = 0

while x < 10:
    print(x)
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
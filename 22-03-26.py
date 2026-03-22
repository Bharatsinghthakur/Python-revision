# Difference between == and is 

# def main():
#     print("first Module's Name: {}".format(__name__))

# if __name__ == "__main__":
#     main()


#  "==" checks equality
#  "is" checks identity

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

# two cans of pepsi can be equal because they have same ingredients


# if l1 == l2:
#     print("True")
# else:
#     print('False')

l2 = l1 # we are assinging the same object to variable
l1[0] = 6
print(l1)
print(l2)

if l1 is l2:
    print("True")
else:
    print('False')

print(id(l1))
print(id(l2))

from collections import namedtuple

# names tuples are more readable and is compromised between tuple and dictionary
Color = namedtuple('color',['red','green','blue'])

color = Color(55,155,255)
color = Color(red=55,blue=155,green=255)

print(color.red)
print(color)
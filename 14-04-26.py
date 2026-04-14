#Shallow copy and deep copy in python
import copy
a = [1,2,3,4]
b = a
a[2] = 100
print(a)
print(b)
# In normal assignment operator changes are visible

# shallow copy  -- will also take care nested changes

# c = [[1,2,3],[4,5,6]]
c = [10,20,30,40]
d = c.copy()
# c[1][2] = 50
d[3] = 400

print(c)
print(d)

# deep copy -- changes on only the assigned list - will also take care nested changes

e = [[1,2,3,4],[5,6,7,8]]
f = copy.deepcopy(e)
f[1][2] = 600
print(e)
print(f)
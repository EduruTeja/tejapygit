print("hello")
print("jnibibibu")
a=(1,2,3,4)
print(list(map(name,a)))


numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


l = ['sat', 'bat', 'cat', 'mat']
test = list(map(tuple, l))
print(test)


import math
numbers=[1, 2, 3, 4, 5]
a=list(map(math.sqrt, numbers))
a


circle_areas = [23.12,4.4500,556,1.03908,23.1]
result = list(map(round, circle_areas))
print(result)



def name(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
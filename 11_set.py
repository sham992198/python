# empty set
a = set()
print(type(a))

# set is not give th repeated value in output
a = {1,3,4,5,3,6,3,76}
print(a)

a = {12,3,2,"hary"}
print(a,(type(a)))

#methods add
a = {22,54,7,84,"harry"}
a.add(3333)
print(a)

#remove
a = {22,54,7,84,"harry"}
a.remove(22)
print(a)

#pop, random element are delete in set
a = {22,54,7,84,"harry"}
a.pop()
print(a)

#clear,set are empty
a = {22,54,7,84,"harry"}
a.clear()
print(a)

# union intersection
a = {1,2,3,4}
b = {5,6,4,7}
print(a.union(b))
print(a.intersection(b))
#


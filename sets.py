"""

    set is one of the basic datatypes in python
    - unsorted datatype
    - doesn't allow duplication
    - no indecies
"""

"1- to define a set "
myset = {"python", 'computervision', 'machine learning01', 'python', 'probability', 10 , True}
""" 
    domain ---> 
    weight 
"""
print(myset)

"2- get len of items in the set "
print(len(myset))

"3- access certain element in the set ? ---> not allowed "
"4- get position in the set ? ---> not allowed "
"5- add element to the set ? "
myset.add("added element")
print(myset)

"6- pop element from the set"
popped = myset.pop()  # pop random element from the set
print(popped)
print(myset)

"7- remove element from the set "
if 'python' in myset:
    myset.remove("python")
else:
    print("element already removed")

"8- add duplicated"
myset.add("Yasser")
print(myset)
myset.add("Yasser")
print(myset)

"9- set copy "

s1 = {"python", 'ml1'}
# s2 = {"ml2", "reinforcement learning "}
s2 = s1.copy()  # copy ---> create new object (new address)
# --> contain the same content of the object
print(s2)


####
s3 = s1

s1.add("my element ")

"loop over the sets...."
for item in s1:
    print(item)


"empty set "
s = set([])

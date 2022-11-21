"""  -------------- lists --------------------------"""
"1- to define a list "
l  = []
myl  = list([])

"2- list can hold different data from different datatypes "
l = ["Ahmed",'Mariam', "Salma", "Asmaa", "Israa", "Amgad", "Yasser", "Israa"]
"3- get len of the list "
print(len(l))
"3- access list elements using index "
print(l[3])
"4- count no of occurance of certain element in a list "
print(l.count("Israa"))

"5- list is are mutable datatype --> update value of certain index "
l[3] ='noha'

"6- appned new item to the list "
# l[10] = 'added'  #  list assignment index out of range
l.append("asmaa")
"7- insert element at certain index "
l.insert(4, 'inserted')
"8- pop element from the list "
# popped_item = l.pop()  # remove the last element in the list
#
# "pop element at certain index "
# other_popped = l.pop(5)

"9- remove element "
l.remove("Israa") # remove the first occurence of the element

"10- get index of the element "
print(l.index("noha")) # get the index of the  first occurence of the element

"11- list concatenation "
l = ["python", 'linux']
l2 = ["reinforcement learning" , 'nlp', 'python']
list_of_courses = l + l2
print(l , l2)
print(list_of_courses)

"12- extend a list "
l.extend(l2)
print(l)

"13- sort ---> list items must be from the same type ---> sort the same  variable "

# print("iti" > "ITI")

# print("iti" > 100)

names = ['Ahmed', 'Osama', 'Khaled', 'Amgad', 'Abdelwahab', 'Yasser', "Israa",
         'Israa', 'Rana', 'Mariam', 'Rawan', 'Asmaa', 'Salma', 'Yasmin', 'Radwa']

print(names)
names.sort()  # ascending
#### sorted
names.sort(reverse=True)
print(names)


"14- reverse the list ---"
myl =['abc', 'iti', 10 , 1000, False ]

myl.reverse()
print(myl)

"15- membership "
print('Israa' in names )

"loop over the list items "
for abbass in names:
    print(abbass)


for c in 'noha':
    print(c)

print("-------")

print(abbass)
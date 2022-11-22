"""
    LIST , TUPLE , SET ---> REPRESNET UNLABLED DATA

"""
#
# info = ['noha', 'mansoura', 'iti']
# """
#     --> key , value
#     dictionary
#     ---> dict ---> from python 3.6 --> dictionary ordered datatypes
#
# """
#
# "1- define dictionary "
# d = {}
myd = dict([("name", "noha"), ("work", "iti")])
# info = {
#     "name": "Noha",
#     'work': "iti"
# }
#
# # ## dictionary ---> doesn't allow key duplicated
#
# "2- count no of pairs in the dict"
# print(len(myd))
#
# "3- mutable datatype ---> change content of the dict --> "
# info["name"]= 'Noha Shaheb'  # update the value
# info['city'] = 'Mansoura'
#
#
# "4- pop element from the dictionary "
# popped_item =info.pop("name")
# print(popped_item)
#
# # popped_item = info.pop()  # must provide the key you want to pop
#
# "5- dict update "
# d1 = {
#     "name":"Ahmed"
# }
# d2 = {
#     "course" : "python",
#     "name": "Asmaa"
# }
# # d3 = d1 + d2  not allowed
#
# d1.update(d2)
# print(d1)
# print(d2)

"6- check existance of element "

emp = {
    "name": "Ahmed",
    "company": "Google",
    "salary": 50000,
    "age": 30
}

# print("Ahmed" in emp)  ### check if Ahmed exists in the dictionary keys
# print("name" in emp)  ### in operator scan dict keys
#
# "7- get the dict keys "
# keys = emp.keys()  # dict_keys ---> can be casted to a list or tuple
# print(keys, type(keys))
# for i  in emp.keys():
#     print(i)
# "8- get the dict values"
# values = emp.values()
# print(values, type(values))
# for val  in emp.values():
#     print(val)
#
# print("Ahmed" in emp.values())
#
# "9- get dict items"
# print(emp.items())  # dict_items
# if(("name", 'Ahmed') in emp.items()):
#     print("found")

"10- loop over the dict "
emp = {
    "name": "Ahmed",
    "company": "Google",
    "salary": 50000,
    "age": 30
}
for item in emp:  # item ---> represent the keys
    print(item)

for k, v in emp.items():  # [(k,v), (k,v)]
    print(f"key={k}, value={v}")

for k in emp:
    print(f"key={k}, value={emp[k]}")

###################
"11- clear dictionary elements"

# emp.clear()

print(emp)  # remove the content of the key-value in the dictionary

##############################
enum_emp = enumerate(emp)
print(list(enum_emp))

for index, item in enumerate(emp.items()):
    print(index, item[0], item[1])

#### delete part of the dictionary
username = 'nohashehab'
# del username  # delete variable from memory in the runtime

# del emp["salary"]


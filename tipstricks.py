#
# def sumnums(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res


#
#
# r=sumnums(2,3)
##############################################
""" anonymous functions  ---> function I don't to call it again"""

# def sumnums(num1, num2):
#     res = num1 + num2
#     print(res)
#     return lambda num:res+num
#
# r=sumnums(2,3)
# # #################3
# # ###################3
# num = input("please enter num")
# if num.isdigit():
#     num = int(num)
#     res = r(num)
# #
# # #####################################################
# l = [5,6,7,8]
# def mullist(mylist ,num ):
#     newlist = []
#     for item in mylist:
#         newlist.append(item*num)
#     return newlist
# #
# l  =mullist(l, 4)
# print(l)
# l = map(lambda x:x*4, l)
# print(l)  # map object can be casted to a list .
# print(list(l))


# l = [10,31,33,45,7,4]
#
# l = filter(lambda x:x%2==0, l)
# print(l) # filter object
# print(list(l))
########################################################################################
# counter = list(range(1, 100))
# print(counter)


# generator --->  generate the value when you need it
# def generate_counter():
#     for i  in range(100):
#         yield i
#
# g = generate_counter()
#
#
# # for i in g: # each time ---> you trigger the object ---> generate a value
# #     print(i)
#
# print(next(g))
#
# print(next(g))
#
# counter= 0
#
#
# for i in range(5):
#     print(next(g))
#
# for i in range(5):
#     print(next(g))


###########################
"iterators in python ----> "
fruits = ["orange", "Kiwi", "apple", "banana", "Mango"]

# for item in fruits:
#     print(item)

fruits = iter(fruits) # list_iterator object
print(next(fruits))
print(next(fruits))
print(next(fruits))
print(next(fruits))
print(next(fruits))





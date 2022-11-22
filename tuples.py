"""built-in datatype ---> non primitive
store different data from data-different datatypes
---> immutable ---> once created cannot be change


"""
# "1- to define a tuple "
# t = tuple([])
# myt = ()
#
# "2- tuple can hold different data from different datatypes "
# myt = ('python', 'cloud', 'big data', 2022, 9.8, True, "cloud")
#
# "3- get length of the tuple "
# print(len(myt))
#
# "4- access tuple elements using index "
# print(myt[3])
#
# "5- count no of occurance of certain element in a tuple "
# print(myt.count("cloud"))
#
# "6- get index of the element "
# print(myt.index("cloud"))
#
#
# "7- tuple concatenation "
# t1 = ("python", 'linux')
# t2 = ("reinforcement learning" , 'nlp', 'python')
# list_of_courses = t1 + t2
# print(t1 , t2)
# print(list_of_courses)
#
# "8- membership "
# print('python' in list_of_courses )
#
#
# "9- loop over the tuple items "
# for abbass in list_of_courses:
#     print(abbass)


"10--- notes"
# mixed_tuple=(1,2,4,'text','flowers',
#     ['Ahmed', 'Ali', 'Omar']
#     ,('Yasmin', 'Amgad'))
# # print(mixed_tuple[5][1])
# mixed_tuple[5].append("new item")
# print(mixed_tuple)
#
# ###################
# l = ['osama', 'Ahmed']
# tt = ('python', 'pandas', l)
# l.append("bla bla bla ")
#
#
# "11- convert tuple to a list and viseverca"
# # ll = []
# # import sys
# # print(sys.getsizeof(ll))
#
#
# # names = ("Ahmed", 'Ali', "Rawan", 'Rana', 'Radwa')
# # names = list(names)
# # print(names)
# #
# # "cast list to tuple"
# # mixed_list=[1,2,4,'text','flowers',
# #     ['Ahmed', 'Ali', 'Omar']
# #     ,('Yasmin', 'Amgad')]
# #
# #
# # mixed_tuple= tuple(mixed_list)
# # print(mixed_tuple)
#
# "11- tuple of one item "
# one_item= ('noha',)
# print(type(one_item))
#
# tt = tuple(['a', 1, 2,3])
# print(tt)

# ################################  non primitive datatype #############################################
"""
     obj1 = obj2 ----> shallow copy ---> copy content and the address 
        ---> when you change the content of obj1 this will reflect in obj2 content. 
"""


l= [3,4,5]
l2 = l   #### alais for the variable name ---> copy

# l.append("new item")

t = (4,5, [7,8])
t2=t  # copy

t[2].append("new item added to t ")
###################################################################################
"""
    ##  copy 
    = with the primitive datatype ---> will create new copy from the object ===> (create new object)
"""
myname = 'noha'
newname = myname

myname +='#'



############################
l = [4,5,6]
newl=l.copy()  # deep copy












"""
            ############## Global scope ######################
"""
"1- any variable defined in the python script -module-  is considered to have a global scope "
"global ---> variable can be accessed(read , write ) anywhere  in the script after defining it , " \
"can be read --> from the function "
# num = 10 ### variable
#
# num+=10
# print(num)

# "2- global variable and the functions "
#
#
# def myfun():
#     print(f"from inside my fun num= {num}")
#
#
# myfun()


"3- modify global variable from inside the function  the functions "

year = 2022
# def modifyyear():
#     year = 2023
#     print(f"from inside my fun num= {year}")
#
# """any variable defined in the function scope ---> has a local scope """
#
# modifyyear()
# print("------------------")
# print(f"Year after calling the function = {year}")


########################
# "4- modify variable from inside any function ----> use global keyword"
# course= 'Python'
#
# print(f"Before calling the function , course  = {course}")
# def changeCourse():
#     global course
#     course = 'Python for machine learning'
#     print(f"inside the function , course  = {course}")
#
#
# changeCourse()
# print(f"After calling the function , course  = {course}")
# print('------------------------------')
###################################
"6- python support creating nested functions "
"""
    local variable can be accessed only inside the function 
"""
# def outerfunction():
#     abbass = 'winter'  # local variable
#
#     def innerfun():
#         print(f"from the inner function abbass = {abbass}")
#
#     innerfun()
#
#     def modifyabbass():
#         abbass = 'spring'  # create new local variable for this function
#         print(f"from the modifyabbass function abbass = {abbass}")
#     modifyabbass()
#     print(f"after calling the modifyabbass function abbass = {abbass}")
#
#
# outerfunction()
# print("---------------------------")

#########################

# def outerfunction():
#     abbass = 'winter'  # local variable
#
#     def modifyabbass():
#         nonlocal abbass
#         abbass = 'spring'  # create new local variable for this function
#         print(f"from the modifyabbass function abbass = {abbass}")
#     modifyabbass()
#     print(f"after calling the modifyabbass function abbass = {abbass}")
#
#
# outerfunction()
# print("---------------------------")
#########################################################################################3

# def outer():
#     # abbass = 'Python'
#     def inner():
#         print("================ the inner fun==================")
#         def subinner():
#             nonlocal  abbass
#             abbass = 'modified '
#
#         subinner()
#     inner()
#     print(f"after calling the subinner = {abbass}")
#
# outer()
###############################################
#
# abbass = 'test'
# def outer():
#     abbass = 'initial'
#     def inner():
#         abbass = 'intermediate'
#         print("================ the inner fun==================")
#         def subinner():
#             nonlocal  abbass
#             abbass = 'modified'
#
#         subinner()
#         print(f"after calling the subinner = {abbass}")
#     inner()
#     print(f"after calling the inner = {abbass}")
# outer()


# abbass = 'test'
# def outer():
#     abbass = 'initial'
#     def inner():
#         nonlocal abbass
#         abbass = 'intermediate'
#         print("================ the inner fun==================")
#         def subinner():
#             nonlocal  abbass
#             abbass = 'modified'
#
#         subinner()
#         print(f"after calling the subinner = {abbass}")
#     inner()
#     print(f"after calling the inner = {abbass}")
# outer()


#######################################
# name= None
# def A():
#     def B():
#         def C():
#             def D():
#                 global name
#                 name ='noha'
#             D()
#         C()
#     B()
#
#
# A()
# print(name)
#################################
name = None
def A():

    def B():
        def C():
            global name
            name = 'noha'
            def D():
                nonlocal  name
                name = 'iti'
            D()
        print(f"name = {name}")
        C()
    B()


A()
print(name)













































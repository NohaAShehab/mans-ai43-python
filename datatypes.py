"""
                Python data types

"""
#
# "1- to check the datatype of variable"
# name= 'Ahmed'
# print(type(name))   # type object ---> represent the string
# t = type(name)
#
# print(t=="<class 'str'>")
#
# t = str(t)
#
# "2- check variable is from specific datatype"
# student = 'Israa'
# print(isinstance(student, str))
#
# "3- type conversion between different types "
# "3.1 convert from int to string "
# num = 2022
# num = str(num)
#
# "3.2 convert from string to int "
# year = '2023'  # contain numeric value
# year = int(year)
#
# "3.3 convert from string to int "
# std_name = 'Khaled'
# # std_name = int(std_name)
# if std_name.isdigit():
#     std_name = int(std_name)
# else:
#     print("Sorry we cannot convert string to int 000")
#
# num = 10
# num += 5
# #####
# "Boolean True , False " \
"""
    True==1 
    False ==0 
"""

"""
truly values :: any value except the falsy values is considered to reperesnt true

falsy values: 0 , False , '', "", '''''', """""" None , empty collections 
"""
print(1 and "iti")  # iti

print("noha" and "iti")

print(None and "iti" )
#####################
print("iti" or "python")

print("" or None or 'AI')


####
print(True==100)



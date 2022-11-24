
#
# import os
#
# print(os.getcwd())
# #
# # print(os.mkdir("mydir"))
# # os.chmod( 'mydir', 7777)
# # os.chdir('/home/noha')
# print(os.getcwd())
#
# os.system('ls -l')
#
# print(os.getlogin())
##########################

# import time
#
# print(int(time.time()))
#
# import datetime
# print(datetime.date.today())
# print(datetime.datetime.now())

#####
import  array
# x= array.array('i', [3,4,5])  # iterable object
#
# for i in x :
#     print(i)
#
# print(x[0])

# ############################## regular expression


# @cc-ddd


import re

pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email = input("please enter your email: ")

# matched = re.match(pattern, email)
# print(matched)
# if matched:
#     print("wellformerd")
# else:
#     print("not wellformed ")



# matched = re.fullmatch(pattern, email)
# print(matched)
# if matched:
#     print("wellformerd")
# else:
#     print("not wellformed ")





matched = re.search(pattern, email)
print(matched)


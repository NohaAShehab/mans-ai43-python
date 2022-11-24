

"""
def funname():
    function body
    return

"""
# "1- simple basic function"
# def sayhello():
#     print("Hello")
##################################
# def sayhello():
#     print("Hello")
#     return
# r = sayhello()

"1- function return something"
# def askforfullname():
#     fname = input("please enter firstname: ")
#     lname = input("please enter lastname: ")
#     fullname = f"{fname} {lname}"
#     return fullname
#
#
# fullname = askforfullname()

# def askforfullname():
#     fname = input("please enter firstname: ")
#     lname = input("please enter lastname: ")
#     fullname = f"{fname} {lname}"
#     return fullname, fname, lname
#
#
# fullname = askforfullname()


# def askforfullname():
#     fname = input("please enter firstname: ")
#     lname = input("please enter lastname: ")
#     fullname = f"{fname} {lname}"
#     return [fullname, fname, lname], fname
#
#
# fullname = askforfullname()

############################
# "3- function that accepts arguments "
# def sumnum(num1, num2):  # num1 , num2 ---> arguments
#     print(f"num1 ={num1}, num2={num2}")
#     res = num1 + num2
#     return res
#
#
# result = sumnum(10 ,20) # 10 , 20 --> parameters
# print(result)
#
# m= sumnum(num2=100, num1=40)
# # m = sumnum(10)
#
# nn = sumnum(None, None)

####
"4- function with default arguments "
# def saywelcome(name, greetingmessage='Nice to meet you'):
#     print(f"Welcome {name}, {greetingmessage}")
#
# # saywelcome("Mohamed", "Nice to meet you ")
# saywelcome("Omar", "we are happy to see you ")
# saywelcome("Ali")


# def saywelcome(name='User', greetingmessage='Nice to meet you'):
#     print(f"Welcome {name}, {greetingmessage}")
#
# # saywelcome("Mohamed", "Nice to meet you ")
# saywelcome("Omar", "we are happy to see you ")
# saywelcome("Ali")
# saywelcome()
# saywelcome(greetingmessage='Hi', name="Mostafa")


################
"5- define function with variable number of arguments "

# print("ahmed", "omar", "ali")

# def addnums(* nums):  # * ---> zero or more
#     print(nums) # tuple
#     res =0
#     for num in nums:
#         res +=num
#
#     return res
#
# addnums(10, 20)
# addnums(10)
# addnums()
#
# r = addnums(10,20,340,233,-100)


# print("Ahmed", "Ali", "Omar", sep="")
# print("Ahmed", end="% ")
# print("Ali")
# print("test")


# def classinfo (classname, * students ):
#     print(classname, students)
#
# classinfo("ai43", "Ahmed", "Maraim", "Asmaa", "Israa", "Salma")

############################

# def classinfo (classname='ai43', * students ):
#     print(f"classname={classname}, students = {students}")
#
# classinfo( "Ahmed", "Maraim", "Asmaa", "Israa", "Salma")
###################
# def classinfo ( *students, classname='ai43' ):
#     print(f"classname={classname}, students = {students}")
#
# classinfo( "Ahmed", "Maraim", "Asmaa", "Israa", "Salma", classname='sd')

#######################
"5- define function with variable number of arguments "
# def introudceYourSelf(** kwargs):
#     print(kwargs)
# def introudceYourSelf(** info):
#     print(info)
#
# noha = introudceYourSelf(name='noha', lives_in='Mansoura', faculty='enginerring')
# osame = introudceYourSelf()
# ahmed= introudceYourSelf(fullname='Ahmed Mohamed')
# israa = introudceYourSelf(name='israa')
#
#
# temp = "My name is {username}, I love {company}"
# print(temp.format(username='noha', company='iti'))

#####################################################################

# def addnums(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res
#
#
# r = addnums(10,20)
#
# r2 = addnums("10", "20")
#
# r3 = addnums(10 , "30")

###############################

# def addnums(num1 :int, num2:int):
#     # if (isinstance(num1, int ) or isinstance(num1, float) )and \
#     #     (isinstance(num2,int) or isinstance(num2, float)):
#     #     res = num1 + num2
#     #     print(res)
#     #     return res
#     if type(num1) in [int, float] and type(num2) in [int, float]:
#         res = num1 + num2
#         print(res)
#         return res
#     print("=====> unsupported data types ")


# r = addnums(10,20)
# #
# r2 = addnums("10", "20")
# #
# r3 = addnums(10 , "30")


def addnums(num1 :int, num2:int)-> int:
    res = num1 + num2
    print(res)
    return res


x = addnums('20', '30')






































































"""
    errors :

        syntax error:
                    must be solved --->  interpreter help
        logical error:
                you must solve it by yourself
        runtime error:
            handling
            raising

"""
#
# def mulnums (num1, num2):
#     res = num1 + num2
#     print(res)
#
#
# mulnums(2 ,2 )
#
# mulnums(20 ,30)
################################ Runtime errors ########################
# print("----------------- runtime errors-----------------------")
# print(name)


print("#########################################################")

# try:
#     print(name)
# except:
#     name = None
#     print("variable not found ")
#     # exit()
#
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# if name:
#     print('found')
# else:
#     print('not found ')


# try:
#     res = 5/0
# except:
#     print("------ problem happended ")


# try:
#     # res = 5/0
#     print(iti)
# except Exception as e :
#     print(f"------ problem happended {e} ")

# # num=10
# num2 = 0
# try:
#     res = num/num2
# except ZeroDivisionError as ze:
#     print(f"problem with division---> {ze}")
# except NameError as ne:
#     # print(f"You must define the variable ---> {ne}")
#     pass
# except Exception as e:
#     # print(f"{e}")
#     pass
#
# print("---------------------------")

###############################  Else block #######################
# num1=20
# num2 = 10
# try:
#     res = num1/num2
# except Exception as e:
#     print(f"---> {e}")
# else:
#     "this block will be executed only if there is no exception "
#     print(res)

######################## finally block #####################
num1=20
num2 = 0
# try:
#     res = num1/num2
# except Exception as e:
#     print(f"---> {e}")
# else:
#     "this block will be executed only if there is no exception "
#     print(res)
# finally:
#     "this block will be exected if there is exception or not "
#     print("-------- End of the program -------------------- ")
##########################################3
# try:
#     res = num1/num2
# except Exception as e:
#     print(f"---> {e}")
# finally:
#     "this block will be exected if there is exception or not "
#     print("-------- End of the program -------------------- ")
#     exit()
######################## Raising the exceptions #####################################
def calculator ():
    num1 = input("please enter num1 ")
    if not num1.isdigit():
        raise  Exception("Num1 should numeric not string value ")

    num2= input("please enter num2 ")


    # num1 = int(num1)
    # num2 = int(num2)

    res = int(num1)/int(num2)
    return res


r = calculator()
print(r)




























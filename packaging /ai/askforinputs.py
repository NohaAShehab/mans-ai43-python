

# def askforInt(message):
#     while True:
#         intvar = input(message)
#         if intvar.isdigit():
#             return int(intvar)
#
#
# age = askforInt("please enter your age : ")
# print(age)
#

def askforInt(message):
    intvar = input(message)
    if intvar.isdigit():
        return int(intvar)

    return askforInt(message)


# age = askforInt("please enter your age : ")
# print(age)


def greeting(username):
    print(f"{username},....")
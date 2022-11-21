# name = 'Noha'
# work = "Information Technology  Institute"
# "1- get len of the string "
# print(len(name))
# "2- access part of the string using index"
# print(name[2])
# print(work[-1])
# print(work[2:5])  # get chars at position from start to end-1
# # print(work[100])
# "3- count no of char occurance in the string"
# print(work.count("t"))
# "4- check type of value is string or not "
# print(isinstance("noha", str))
# "5- string concatentation "
# firstname= 'Noha '
# midname= 'Abdel Hady '
# lastname='Shehab'
#
# # fullname = firstname + midname +midname + lastname
# # print(fullname)
#
# "string contcatenation is allowed only between strings "
# # fullname +=5
# "6- string interploation"
# fullname = firstname + midname*2 + lastname
# print(fullname)
#
# "7- captilize "
# message = 'good morning team'
# print(message.capitalize())
# print(message.upper())
# print(message.lower())
#
# "8- check if the string capital or small "
# print(message.islower())
# print(message.isupper())
# "9- check if the string is spaces"
# print(message.isspace())

"""
    mystr = '                                   '

"""
mystr = ' '
print(mystr is False)
print(mystr.isspace())

"10 - check if string contain numeric values "
mystr = '2022'
print(mystr.isdigit())
print(mystr.isnumeric())  # assigment ?
"check if the value in the string is float "

'11- check spaces in the string'
mystr = "This lecture is so interesting"
print(mystr.count(" "))

"12- check value in the string in alphas "
name = 'Amagad'
print(name.isalpha())

## search isnum()

"13- string formatting "
# temp = "My name is {0} I works at {1}"
# print(temp.format("noha", "iti"))
# print(temp.format("Ahmed", "Facebook"))
# print(temp.format("google", "Mohamed"))


# temp = "My name is {name} I works at {company}"
# #
# print(temp.format(company='Google', name='Yasmin'))
"14- accept input from user "
# firstname = input("Please enter name : ")  # input function always returns with string
# age = input("Please enter age : ")
#
# if age.isdigit():
#     age = int(age)

"14- f-format string "
# username = input("please enter your name: ")
# # greeting = f"Greeting {username}, Nice to meet you ... "
# # print(greeting)
# year = 2022
# year= float(year)
# # greeting = "Greeting" + username+  "Nice to meet you ... " + year
# greeting = f"Greeting {username}, {year}"
# print(greeting)

"15- string replacement "
# mymessage = 'My name is Noha I works at iti '
# print(mymessage.replace("o", "@"))


"16- strip spaces "
message ='                  Python is simple        the lecture is interesting        @'

print(message)

print(message.strip()) # strip spaces from the begining and the end of the string

print(message.strip("@ Pi"))
#######
print(message.lstrip("@"))
print(message.rstrip("@"))
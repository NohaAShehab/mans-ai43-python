

"""
    sequence unpacking
"""

# def askforinfo():
#     fname = input("please enter firstname : ")
#     lname = input("please enter lastname: ")
#
#     return fname, lname
#
# # res = askforinfo()  # tuple
# firstname, lastname= askforinfo()

##########################

# def askforinfo():
#     fname = input("please enter firstname : ")
#     lname = input("please enter lastname: ")
#
#     return fname, lname, True, 'iti'
#
# # res = askforinfo()  # tuple
# *firstname, lastname= askforinfo()
###########################################3
with open("mycv", "w") as fileobject:
    fileobject.write("test")

##################################3
# l=list(range(10))

# l  = [i*i  for i in range(10) if i%2==0]

l = [6,7,6,9, False]
print(all(l))

print(any(l))
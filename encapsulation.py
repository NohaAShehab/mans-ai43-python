"""
    limit accessibility to the properties and method
    Access modifiers
    public ---> can access the property / method ---> using object --> in/out the class
    private  ---> property / method ---> can be accessed only in the class
    protected ---> property / method ---> can be accessed in the class/ derived class

    in python explicit no-access modifiers
    ---> propertyname start with char ----> public property
    ---> propertyname start with _chars ----> protected property
    ---> propertyname start with __chars ----> private property

"""


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # instance variable ---> public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#     def printinfo(self):
#         print(f"{self.name}, {self._email}, {self.__salary}")
#
#     def _myfun(self):
#         print(self.name)
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 20000)
# print(e._email)  # ethically don't do that
# # print(e.__salary)  # not founf
# e.printinfo()
# # print(e._Employee__salary) # scope binding
# e._myfun()
#
# e.__city = "Cairo"  # initialized in the runtime
# print(e.__city)  # called in the runtime

##############################################

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # instance variable ---> public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#
#     def setSalary(self, salary):
#         self.__salary = 0
#         if type(salary) in [int, float]:
#             self.__salary = salary
#         elif isinstance(salary, str):
#             if salary.isdigit():
#                 self.__salary = int(salary)
#
#
#
#     def getSalary(self):
#         return self.__salary*8
#
#
# # e = Employee("Ahmed", "Ahemd@gmail.com", 30000)
# # print(e.getSalary())
# # e.setSalary("iti")
#
#
#
# emp = Employee("noha", "noha@gmail.com", "iti")
# print(emp.getSalary())
########################################################

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # instance variable ---> public
#         self._email = email  # protected
#         # self.__salary = salary  # private
#         self.setSalary(salary)
#
#
#     def setSalary(self, salary):
#         self.__salary = 0
#         if type(salary) in [int, float]:
#             self.__salary = salary
#         elif isinstance(salary, str):
#             if salary.isdigit():
#                 self.__salary = int(salary)
#
#
#
#     def getSalary(self):
#         return self.__salary*8
#
#
# # e = Employee("Ahmed", "Ahemd@gmail.com", 30000)
# # print(e.getSalary())
# # e.setSalary("iti")
#
#
# #
# # emp = Employee("noha", "noha@gmail.com", "iti")
# # print(emp.getSalary())
#
#
# emp = Employee("noha", "noha@gmail.com", 10)
# print(emp.getSalary())
###########################################################
class Employee:
    def __init__(self, name, email, salary):
        self.name = name  # instance variable ---> public
        self._email = email  # protected
        self.salary = salary


    @property
    def salary(self):
        return self.__salary*.8

    @salary.setter
    def salary(self, salary):
        if type(salary) in [int, float]:
            self.__salary = salary
        elif isinstance(salary, str):
            if salary.isdigit():
                self.__salary = int(salary)
            else:
                raise Exception("please enter valid number ")



    def printEmpInfo(self):
        print(f"this {self.salary} {self.name}")



emp = Employee("ahmed", "ahmed@gmail.com", "iti")
print(emp.salary)
# print(emp.salary)

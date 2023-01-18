"""
    python provide special methods ---> do functionality
    __len__
    __str__
    __rper__
    __call__
"""
# l = [2,4,5,5]
# print(len(l))
# print(l)

# class Employee:
#     def __init__(self,name,email, salary):
#         self.name = name
#         self.email =email
#         self.salary = salary
#     def __len__(self):
#         return len(self.__dict__)
#
# e = Employee("Test", "test", 1000)
# e.city = 'Cairo'
#
# print(len(e))
# print(e.__dict__)  # represent the object in form of dict --->

# e3 = Employee("Test", "test", 1000)
# print(len(e3))


#########################################33
# class Employee:
#     def __init__(self,name,email, salary):
#         self.name = name
#         self.email =email
#         self.salary = salary
#
#     def __str__(self):
#         # must return with string ---> user
#         return f"Employee({self.name}, {self.email}, {self.salary})"
#
#
# e = Employee("Test", "test", 1000)
# print(e)
#
#
# e2= Employee("Abccccccccc", "test", 1000)
# print(e2)
###############################
#
# class Employee:
#     def __init__(self,name,email, salary):
#         self.name = name
#         self.email =email
#         self.salary = salary
#
#     def __str__(self):
#         print("-----------------")
#         return f"{self.name}"
#
#     def __repr__(self):
#         print(f"name: type = {type(self.name)}")
#         return f'Employee(name={self.name}, email={self.email}, salary={self.salary})'
#
#
# e = Employee("Test", "test", 1000)
# print(e)
#
# print(e.__repr__())
#
# e2= Employee("Abccccccccc", "test", 1000)
# print(e2)
# #######################


class Employee:
    def __init__(self,name,email, salary):
        self.name = name
        self.email =email
        self.salary = salary

    def __call__(self, *args, **kwargs):
        print("Employee object has been called ")



e = Employee("Test", "test", 1000)
e()

#######################











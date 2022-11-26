

# class Person:
#     pass
#
# class Employee(Person):
#     pass
#
# e = Employee()
# print(type(e))
# print(isinstance(e, Person))

# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Employee(Person):
#     pass
#
# e = Employee("noha")
# print(type(e))
# print(isinstance(e, Person))

###############################

# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Employee(Person):
#     def __init__(self, salary):
#         self.salary = salary
#
# e = Employee("noha")
# print(type(e))
# print(isinstance(e, Person))
#############################################
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
# class Employee(Person):
#     def __init__(self,name, salary):
#         # super().__init__(name)
#         super(Employee, self).__init__(name)
#         self.salary = salary
#
# e = Employee("noha", 30000)
# print(type(e))
# print(isinstance(e, Person))
# e.speak()
# ################################################ Python support multiple inheritance

# class Parent():
#     def __init__(self,name):
#         self.name = name
#     pass
#
# class A(Parent):
#     def __init__(self, username):
#         self.name = username
#         print("calling A constructor")
#
# class B(Parent):
#     def __init__(self,email):
#         self.email = email
#
# class M:
#     def __init__(self,id):
#         self.id = id
# class Child(A,B):
#     def __init__(self, name):
#         super(Child, self).__init__(name)
#         B.__init__(self, email='iti')
#         M.__init__(self, id=10)

# c = Child("noha")
# print(isinstance(c, B))
# print(isinstance(c, A))
# print(isinstance(c, Parent))

############################### inheritance
class Base:
    def __init__(self,name):
        self.name = name

# first case ---> inherit from mutiple classes doesn't inherit from the same class


class Person(Base):
    def __init__(self, name, nid):
        print("---- Person -------")
        super(Person, self).__init__(name)
        self.nid = nid

class Employee():
    def __init__(self, name, salary=10):
        print("---- Employee -------")
        super().__init__(name)
        self.salary = salary

class Engineer(Person, Employee):
    def __init__(self, name, id , dept ):
        super().__init__(name, id)
        self.dept = dept


e = Engineer("Ahmed",10 , "Ai")  # the constructor of the person class will only be called
##########################################3
"""
    if Employee and Person are inherited from the same class ? the 2 Person , and Employee constructors will
    be called 
"""


class Person(Base):
    def __init__(self, name, nid):
        print("---- Person -------")
        super(Person, self).__init__(name)
        self.nid = nid


class Employee(Base):
    def __init__(self, name, salary=10):
        print("---- Employee -------")
        super().__init__(name)
        self.salary = salary
#
class Engineer(Person, Employee):
    def __init__(self, name, id , dept ):
        super().__init__(name, id)  # this will call the constructor of Employee and Person
        self.dept = dept
#
#
e = Engineer("Ahmed",10 , "Ai")



























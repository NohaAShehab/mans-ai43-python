"""
    OOP --->

"""
# employee= [1, 'ahmed', 'amazon']

# employee = {
#     "id":1,
#     "name":"Ahmed",
#     "company":"Amazon"
# }
#
# employee2 = {
#     "emp_id":2,
#     'emp_name':"Ali",
#     "company_name":"Google"
# }
"# create your first class"
# class Employee:
#     pass
#
#
# "1- take object from Employee"
# e = Employee()
# print(e)
# print(type(e))
#
# l=[3,4] # object built-in class (list )
# print(type(l))

######################################33
"""all classes in the Python ---> inherits implicitly from class Object"""
# class Employee:
#     pass
#
#
# e = Employee()
# e.name='Noha'
# e.salary=1000
# e.email ='nshehab@gmail.com'
#
# print(e.__dict__)
#
#
# e2 = Employee()
# e2.username ='Ahmed'
# e2.emp_email='ahmed@google.com'
# e2.address = 'Cairo'

###########################################################

# """ class is considered to be object factory """
# class Employee:
#     def __init__(self):  # is the class constructor
#         print("--- this function is being called using the object creation")
#         print(self)
#         self.name = 'Ahmed'
#         self.id = 1
#         self.email = 'ahmed@facebook.com'
#
#
#
#
# e = Employee()
# print(e)
# print("------------------------------------")
#
# e2= Employee()


""" class is considered to be object factory """
# class Employee:
#     def __init__(self, name, id , email):  # is the class constructor
#         print("--- this function is being called using the object creation")
#         print(self)
#         self.name = name
#         self.id = id
#         self.email = email
#
# e = Employee("Noha", 1, 'nshehab@iti.com')
# print(e.name)
# e.name='Noha Shehab'
# print("------------------------------------")
# e.country='Egypt'
#
# e2= Employee('Mostafa', 100, 'm@iti.com')

#################################################################
#
# class Employee:
#
#     __slots__ = ["name", "id", "email", "image"]
#     def __init__(self, name, id , email):  # is the class constructor
#         print("--- this function is being called using the object creation")
#         print(self)
#         self.name = name
#         self.id = id
#         self.email = email
#
# e = Employee("Noha", 1, 'nshehab@iti.com')
# print(e.name)
# e.name='Noha Shehab'
# print("------------------------------------")
# e.image='Egypt'
#
# e2= Employee('Mostafa', 100, 'm@iti.com')

#################################################################


# class Employee:
#     def __init__(self, name='iti', id=100 , email='iti@iti.com'):  # is the class constructor
#         """ name , id , email are instance variable """
#         self.name = name
#         self.id = id
#         self.email = email
#
# e = Employee("Noha", 1, 'nshehab@iti.com')
# print(e.name)
# e.name='Noha Shehab'
# print("------------------------------------")
#
# e2 = Employee()

##############################################
""" define function in a functions """


# class Employee:
#     def __init__(self, name='iti', id=100 , email='iti@iti.com'):  # is the class constructor
#         """ name , id , email are instance variable """
#         self.name = name
#         self.id = id
#         self.email = email
#
#     # instance method
#     def printEmpInfo(self, message='Hi'):
#         print(f"My name is {self.name}, You can reach me at {self.email}, {message}")
#     # def printEmpInfo(message):  # message  ---> represent the object in the memory
#     #     print(f" message = {message}")
#
#     def abc():
#         print("abc")
#
#
# e = Employee("Noha", 1, 'nshehab@iti.com')
# e.printEmpInfo()
# print("------------------------------------")
# # e.abc()  # send the self --->
# Employee.abc()  # like static in python
#
#
# e2 = Employee()
# e2.printEmpInfo()

############################################################################
# class Employee:
#     company = 'iti'  # company is class varaible
#
#     def __init__(self, name='iti', id=100, email='iti@iti.com'):  # is the class constructor
#         """ name , id , email are instance variable """
#         self.name = name
#         self.id = id
#         self.email = email
#
#     def printEmpInfo(self, message='Hi'):
#         print(f"My name is {self.name}, You can reach me at {self.email}, {message}")
#
#
# e = Employee("Noha", 1, 'nshehab@iti.com')
# e.printEmpInfo()
# print("------------------------------------")
# print(Employee.company)
#
# e2 = Employee()
# e2.printEmpInfo()
# Employee.company = 'MCIT'
#
# Employee.location  = 'Africa'
#
# e.company = 'Amazon'
#
# Employee.company= "Google"

#######################################3
"define behaviour the class can do ---> class method "
#
# class Employee:
#     company = 'iti'  # company is class varaible
#     count = 0
#
#     def __init__(self, name, id, email):  # is the class constructor
#         """ name , id , email are instance variable """
#         self.name = name
#         self.id = id
#         self.email = email
#         Employee.count +=1
#
#     def printEmpInfo(self, message='Hi'):
#         print(f"My name is {self.name}, You can reach me at {self.email}, {message}")
#
#     @classmethod
#     def get_emp_count(cls):
#         print(cls)
#         print(cls.count)
#
#     @classmethod # act like object factory -==> create object or set of objects
#     def create_simplified_object(cls):
#         return cls("Default",1000, 'defautl@emp.com')
#
#     @classmethod
#     def create_bulkemp(cls, num):
#         listofemps = []
#         for i in range(num):
#             listofemps.append(cls("Default",1000, 'defautl@emp.com'))
#         return listofemps
#
#     #
#     # def __add__(self, other):
#     #     pass
#
# e= Employee("Ahmed",10,'ahmed@gmail.com')
# e2 = Employee("Mostafa", 20, 'm@gmail.com')
# Employee.get_emp_count()
# print(Employee.count)
#
# e3= Employee.create_simplified_object()
#
# e4, e5, e6 = Employee.create_bulkemp(3)




"""
    c1=4+3j
    c2 = 5+6j 
    
    c1 +  c2 = c3 ---> class method 
    
    c1  = c1+ c2


"""
###################################### static method


class Employee:
    count = 0

    def __init__(self, name, id, email, salary=20000):  # is the class constructor
        """ name , id , email are instance variable """
        self.name = name
        self.id = id
        self.email = email
        self.salary=salary
        Employee.count += 1

    def printEmpInfo(self, message='Hi'):
        print(f"My name is {self.name}, You can reach me at {self.email}, {message}")

    @classmethod
    def get_emp_count(cls):
        print(cls)
        print(cls.count)

    @classmethod  # act like object factory -==> create object or set of objects
    def create_simplified_object(cls):
        return cls("Default", 1000, 'defautl@emp.com')

    @classmethod
    def create_bulkemp(cls, num):
        listofemps = []
        for i in range(num):
            listofemps.append(cls("Default", 1000, 'defautl@emp.com'))
        return listofemps

    @staticmethod  # function doen't depend on the object or the class ---> just a helper function
    def calNeTsal(salary):
        return salary * .8


e = Employee("Ahmed", 10, 'ahmed@gmail.com')
print(e.salary)
# def calNeTsal(salary):
#     return salary*.8
# net = calNeTsal(e.salary)
# print(f"Net salary = {net}")

print(e.calNeTsal(e.salary))
print(Employee.calNeTsal(e.salary))


print(Employee.calNeTsal(50000))
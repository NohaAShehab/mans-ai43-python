"""
    polymorphism

    ---> overloading

    ----> overriding

"""
#
# class Test:
#     def __init__(self, name):
#         self.name = name
#     # def sayHello(self):
#     #     print(f"My name is {self.name}")
#
#     def sayHello(self,message=''):
#         if message:
#             print(f"My name is {self.name}, {message}")
#         else:
#             print(f"---- {self.name}")
#
# t = Test("Khaled")
# t.sayHello("Hi")
# t.sayHello("mmmmmmm")

#### overloading -----> dispatch ---> dispatch decorator ---> overloading --> datatypes ---> retrun type


##################################################

class Parent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")


class Child(Parent):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def speak(self, message = 'iti'):
        super().speak()
        print(f"My name is {self.name}, My salary is {self.salary}, {message}")


c = Child("Ahmed", 10000)
c.speak()












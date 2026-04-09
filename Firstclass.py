# class Student:
#     pass
#
# s1=Student()
# s2=Student()
#example Two

# class Student:
#     def init__self__(self):
#       self.name="Student"
#       self.age=19
#
# s1=Student()
# print(s1.name)
# print(s1.age)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# s1=Student("Std1",48)
# print(s1.name)
# print(s1.age)
#
# s2=Student("Std2",19)
# print(s2.name)
# print(s2.age)

# class Student:
#     def __init__(abc,name):
#         abc.name=name
#
#     s1=Student("Hello Jiiii")
#     print(s1.name)
#function Inside the class

# class Student:
#     def __init__(self):
#         self.name="Ram"
#     def display(self):
#         print(self.name)
#     s1= Student()
#     s1.display()
#6th Example

# class demo:
#     def __init__(self):
#         self.x=10 #instance Memeber
#
# objj=demo()
# objj.x=100
# print(objj.x)
# obj=demo()
# print(obj.x)

#7th Example
# class demo:
#     x=100
#     # def __init__(self):
# obj=demo()
# obj1=demo()
# print(obj.x)
# print(obj1.x)

#Example 8th

# class demo:
#     x=100
#
# obj1=demo()
# obj2=demo()
# obj1.x=1000
#
# print(obj1.x)
# print(obj2.x)
#Example of Sqare

# class demo:
#     def sqare1(self):
#         num1=100
#         res=num1*num1
#         print(res)
#     def sqare2(self,num1):
#         res=num1*num1
#         print(res)
#     def sqare3(self):
#         num1=100
#         res=num1*num1
#         return res
#     def sqare4(self,num1):
#         return num1 *num1
#
#     obj=demo()
# #     obj.sqare1()
#     obj.sqare2(100)
#
#     res1=obj.sqare4(100)
#     print(res1)

# class Demo:
#     x=10
#
#     @classmethod
#     def test_method(cls):
#         print(cls.x)
#
# obj=Demo()
# obj.test_method()


#parent Class And Chold Class Exapmle

class parent:
    def __init__(self):
        self.x=100

class Child(parent):
    def __init__(self):
        super().__init__()
        self.y=1000

obj=Child()
print(obj.y)
print(obj.x)

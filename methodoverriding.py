# class parent:
#     def db_conn(self):
#         return "Sql conn"
#
# class Child(parent):
#     def db_conn(self):
#         return "Mongo db"
#
#     obj=Child()
#     res= obj.db_conn()
#     print(res)

# class parent():
#     def db_conn(self):
#         return " Mongo db soon !"
#
# class Child(parent):
#     def test_fun(self):
#         return super().db_conn()
#
# obj=Child()
# res=obj.test_fun()
# print(res)
#access the Private Variablr

# class class1:
#     def __init__(self):
#         self.__x=100
#
# obj=class1()
# print(obj.__class__x)

#polymorphisim
#(Behaves Like Many)
# class Demo():
#     def addn(self,param1,param2):
#         print(param1+param2)
#
# obj=Demo()
# obj.addn(100,230)
# obj.addn("Maroti","Ingale")

# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(shape)
#     def __init__(self,redious):
#
#     def area(self):
#         return 3.14*self.radious*self.radious
#
# class Rect
#there is code remaining



class test1():
    def show(self):
        print("Tesst1")

class test2():
    def show(self):
        print("Test2")
class test3(test1,test2):
    def show(self):
        print("Print 4")
        pass

obj=test3()
obj.show()
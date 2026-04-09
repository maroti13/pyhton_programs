# def fun_1(**data):
#     print(data)
#     print(type(data))
# fun_1(name="AshokIt",course="GenerativeAI")
# def test_fun(num,num1=1000,num2=2000):
#     print(num,num1,num2)
#
# test_fun(100,num1=1,num2=2)

# def test_fun(num1,num2):
#     return num1+num2,num1-num2,num1*num2,num1/num2
#
# add,sub,mul,div=test_fun(100,200)
# print(add)
# print(sub)
# print(mul)
# print(div)
# def test_fun():
#     num=100
#     print(num)
# test_fun()
# print(num)
#global
a=200
# def test_fun():
#     a=10
#     print(a) #local
# test_fun()
# print(a) #global
def outer():
    x=10

# def inner():
#     print(x)
# inner()
# def test_1():
#     num1=100
#     def test_2():
#         nonlocal  num1
#         num1=num1+num1
#         print(num1)
#     test_2()
# test_1()

name="HpSchool" #global
# def student():
#     name="STD1"
#     def info():
#         name="Class X" #local
#         print(name)
#     info()
#
# student()

# def test_fun(param1=[]):
#     param1.append(1)
#     return param1
# print(test_fun())
# print(test_fun())
#Map
# To manipulate
# print(list(map(lambda x:x*x,[1,2,3,4])))

#filter

f= lambda x=10:x+10
print(f())







class parent:
    def fun_1(self):
        print("Hello,Parent")

class child(parent):
    def fun_2(self):
        print("Hello,child")

class subchild(child):
    def fun_3(self):
        print("Hello,SubChild")

obj=subchild()
obj.fun_1()
obj.fun_2()
obj.fun_3()
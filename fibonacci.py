#to get a fibonacci number you hav eadd two number then it gets
#0 1 1 2 3 5 8 13 21.........
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):


        c=a+b
        a=b
        b=c

        print(a+b)


fib(5)
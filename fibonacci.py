# method 1 using recursion
def fibonacci(n):
    if n<0:
        print("incorrect Input")
    elif n==0:
        return 0
    elif n == 1 or n==2:
        return 1
    else :
        return fibonacci(n-1)+ fibonacci(n-2)
for i in range(5):
    print(fibonacci(10)) 

# fib=[0]*5
# fib[0]=0
# fib[1]=1
# for i in range(2,5):
#     fib[i]=fib[i-2]+fib[i-1]
# print(fib)

# def generator(n):
#     p=0
#     q=1
#     while p<n:
#         yield p
#         p,q=q,p+q

# x=generator(10)
# print(x.__next__())
# print(x.__next__())

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

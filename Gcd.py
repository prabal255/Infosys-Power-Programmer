#Recursion

def hcfnaive(a,b):
    if b==0:
        return a
    else:
        return hcfnaive(b,a%b)

a=60
b=48
print(hcfnaive(a,b))

#Eucledian Algorithm

def computegcd(x,y):

    while(y):
        x,y=y,x%y
        print(x,y)
    return x
print("Gcd Uisng Eucledian",computegcd(60,48))

#using Loops
def loops(c,d):
    if c>d:
        small=d
    else:
        small=c
    for i in range(1,small+1):
        if ((c%i == 0) and (d%i==0)):
            gcd=i
    return gcd

print('GCD using Loop',loops(60,48))

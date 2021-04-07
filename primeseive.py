def seiveprimenumber(n):
    prime=[True for i in range(n+1)]
    p=2
    while p*p <=n:
        if prime[p]==True :
            for i in range(p*p,n,p):
                prime[i]=False
        p=p+1
    print(prime)

    for i in range(2,n+1):
        if prime[i] == True:
            print(i)

seiveprimenumber(30)
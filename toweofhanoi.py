def tower(n,source,dest,aux):
    if n==1:
        print("Move disk 1 from",source ,"to",dest)
        return

    else :
        tower(n-1,source,aux,dest)
        print("Move disk",n, "from",source ,"to",dest)
        tower(n-1,aux,dest,source)


n=4
tower(n,'A','C','B')
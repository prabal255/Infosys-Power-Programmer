class soln:
    def watertap(self,ls):
        n=len(ls)
        left=[0]*n
        right=[0]*n
        final=0
        left[0]=ls[0]

        for i in range(1,n):
            left[i]=max(left[i-1],ls[i])

        right[n-1]=ls[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],ls[i])
            
        for i in range(0,n):
            final+=min(left[i],right[i])-ls[i]
        print(final)
        
ls=list(map(int,input().split()))
a=soln()
a.watertap(ls)
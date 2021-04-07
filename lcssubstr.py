def Lcs(x,y,m,n):
    lcsmat = [[0 for k in range(n+1)] for l in range(m+1)]
    rsl=0
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j == 0 :
                lcsmat[i][j]=0
            elif x[i-1]==y[j-1]:
                lcsmat[i][j]=lcsmat[i-1][j-1]+1
                rsl=max(rsl,lcsmat[i-1][j-1])
            else :
                lcsmat[i][j]=0

    return rsl

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
 
m = len(X)
n = len(Y)
 
print('Length of Longest Common Substring is',Lcs(X, Y, m, n))

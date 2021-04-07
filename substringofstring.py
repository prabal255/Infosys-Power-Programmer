def subString(s, n):
	for i in range(n):
		for lenk in range(i+1,n+1):
			print(s[i: lenk]);

s = "abcd";
subString(s,len(s));

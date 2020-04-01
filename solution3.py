k=[]
a=list(map(str,input().split()))
print(a)
s=input("Enter the query string--:")
for i in a:
	if i.startswith(s):
		k.append(i)
print(k)

		
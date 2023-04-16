print("Give me number f ")
f=int(input())
print("Give me number b ")
b=int(input())
print("Give me number n ")
n=int(input())

for i in range(1,n+1):

    if (i%f==0):
	print("F")
    if (i%b==0):
	print("B")
    if (i%f==0 and i%b==0):
	print("FB")
else:
	print(i)
x=int(input())
s=0
while x:
    r=x%10
    x=x//10
    print (r,'+10',s)
    s+=1
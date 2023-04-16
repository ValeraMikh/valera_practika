x=int(input("Please give me number "))
if not x%2==0:
    if x%3==0 and x%5==0 and x%10!=0:
        print(x)
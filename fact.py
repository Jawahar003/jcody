def facto(n):
   if n==1:
       return n
   else:
       return n*facto(n-1)
num=int(input())
if num<=20:
    if num==0:
        print("1")
    else:
        print(facto(num))

lst=[]
num=int(input())
m=int(input())
k=0
for n in range(num):
    numbers=int(input())
    lst.append(numbers)
for i in range(m):
    k=k+lst[i]
print(k)

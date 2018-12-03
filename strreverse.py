def reversestr(s):
    return s[::-1]

s=input("enter a string")
if(len(s)<1000):
  print(reversestr(s))

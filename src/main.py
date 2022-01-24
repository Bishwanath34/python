x=int(input("Enter your number:"))
a=0
sum=0
while a<x:
  sum=sum+1
  sum=sum+a
  a=a+1
print(sum)
for i in range(1,x+1):
  for j in range(1,i+1):
   print(i,end=" ")
  print()
import math
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
y=math.pow(b,2)-4*a*c
if y>0:
  x1=(-b+math.sqrt(y))/2*a
  x2=(-b-math.sqrt(y))/2*a
  print(x1)
  print(x2)
elif y==0:
  x1=x2=-b/2*a
  print(x1)
  print(x2)
else:
  print("No real roots.")
  

  



  
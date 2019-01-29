import math

a=int(input("Enter the coefficient of x"))
b=int(input("Enter the coefficient of y"))
c=int(input("Enter the coefficient "))

d=(b*b)-(4*a*c)

if(d==0):
 print("Roots are equal")
elif(d<0):
 print("Roots are complex")
else:
 Alpha=(-b+math.sqrt(d))/(2*a)
 Beta=(-b-math.sqrt(d))/(2*a)
 print("The roots are",Alpha)
 print("The roots are",Beta)
 
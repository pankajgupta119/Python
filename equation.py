import math

a=int(input("Enter the coefficient of x"))
b=int(input("Enter the coefficient of y"))
c=int(input("Enter the coefficient "))

d=math.sqrt((b*b)-(4*a*c))
Alpha=(-b+d)/(2*a)
Beta=(-b-d)/(2*a)
 
print("Result for alpha",Alpha)
print("Result for Beta",Beta)
 

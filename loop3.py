#loops for prime number

num=int(input("Enter the number"))
c=0
if (num<0):
 print("it is a negative number")

elif(num==1):
 print("It is neither prime nor composite")
 
else:
 for i in range(2,num):
   if(num%i==0):
    c=c+1
 if(c!=0):
  print("the number is not prime")
 else:
  print("the number is prime")
  
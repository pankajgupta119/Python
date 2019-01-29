#Generate electricity bill from the following conditions: 
#Condition 1. If meter reading is more then 100 charagble amount will be 6.95 Rs per unit.
#Condition 2. If meter reading is less then 100 charagble amount will be 5.95 Rs per unit.



units=int(input("\t ENTER THE UNITS OF ELECTRICITY USED"))

 if units<=100:
 bill=units*5.95
 else:
 num1=100*5.95
 num2=units-100
 num3=num2*6.95
 bill=num1+num3
 print("THE BILL IS ",units,"UNITS IS",bill)
#Employee NetSalary Calculation

Basic_pay=int(input("ENTER THE BASIC SLARY OF THE EMPLOYE"))

TA= int(input("ENTER THE TA OF THE EMPLOY"))

HA= int(input("ENTER THE DA OF THE EMPLOY"))

Working_days=int(input("ENTER THE TOTAL WORKING DAYS OF THE EMPLOY IN A MONTH"))

netsalary=Basic_pay+TA+HA

Tax=(netsalary*10)/100

tax_netsalary=netsalary-Tax

total=tax_netsalary/31

total1=total*25

print("THE TOTAL SALRY RECEIVED BY THE EMPLOYE IS::",total1)


#CGPA/Percentage Calculator







course_code=input("ENTER THE COURSE CODE::\t") 

Ete=float(input("Enter the total marks obtained in ETE out of 100::"))


Mte=float(input("Enter the total marks obtained in MTE out of 40::"))

Ca=float(input("Enter the total marks obtained in 3CA out of 100::"))

Att=float(input("Enter the Total Attendance marks"))

Etew=(Ete/100)*50

Mtew=(Mte/40)*20

Caw=(Ca/100)*25

print("ETE MARKS OUT OF 50",Etew)
print("MTE MARKS OUT OF 20",Mtew)
print("CA MARKS OUT OF 25",Caw)
print("ATTENDANCE MARKS OUT OF 5",Att)

Total=Ete+Mte+Ca+Att

percent=(Total/245)*100

print("\tPERCENTAGE IS",percent)

cgpa=(percent/10)

print("\tTOTAl CGPA IS::::", cgpa)
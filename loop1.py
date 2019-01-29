#This is example of for loop statement

i=0
limit=int(input("Enter the Number"))
for i in  range(1,11):
 # print(i,"X",limit,"=",(i*limit))
 print("{}x{}={}".format(i,limit,i*limit))
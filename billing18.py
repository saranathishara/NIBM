import sys
#import os
c=0
tot=0
dis=0

while True:
    try:
        price = float(input("\n Enter Item Price:"))
        c = c + 1
        itmTot = price
        tot = tot + itmTot
    except ValueError as e:
	
        break


if (tot>5000):   #Greater than 5000

    dis = tot * 20 /100

    disPr = "20%"   #Discount
elif (tot>3000):
    dis = tot * 15/100
    disPr = "15%"
elif (tot>2000):
    dis = tot * 10/100
    disPr = "10%"
elif (tot>1000):
    dis = tot * 5/100
    disPr = "5%"
else:
    dis=0
    disPr = "0%"

print("\nTotal of the bill:",tot)
print("Discount(",disPr,"):",dis)
sub=0
sub=tot-dis
print("\nAmount to pay:",sub)



f = open("bills.txt","a") 
f.write("\nTotal Bill : ")
f.write(str(sub))
f.close()
    

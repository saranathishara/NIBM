#Define Variables
tot = 0
discount=0
prices = []

while True:
        try:
                price = input("Enter your Item's Price :")
                if not price:
                        print("Enter your Price and try again")
                        quit()
                break
                prices.append(float(price))
                tot = tot + float(price)
        except ValueError:
                print("Invalid Charactor") #When some one enter Varcha type

if tot > 10000:
        discount = 20
elif tot >= 7000:
        discount= 10
elif tot >= 2000:
        discount = 5

discounttot = float(tot * (discount/100.00))
fulltot = tot - discounttot  #Net Amount
print("Total :",tot,"Discount : ",discounttot , "Net tot:",fulltot)

while True:
        try:
                file = open("BillReport.txt","a")
                
        except IOError:
                print("File Error")
                option = input("Enrer value and retry")
                if not option:
                        print("Error Save the file")
                        quit()
                else:
                        continue
        break

for x in range(0,len(prices)):
        if x ==len(prices)-1:
                file.write(str(prices[x]) + "\n\n")
        else:
                file.write(str(prices[x]) + "\n")
file.close()

        
                
        

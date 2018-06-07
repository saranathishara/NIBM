import os
print(" ")
print("==== PING TOOL IN PYTHON ====")
pop = input("Enter Your IP Address or Web Address :")
ping = os.system("ping " + str(pop))
if ping ==0:
    print("UP")
else:
    print("Down")

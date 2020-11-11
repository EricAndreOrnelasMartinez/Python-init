user = int(input("How many users do you want to insert?    "))
aruser = []
for i in range (user) :
    aruser.append(input("Insert user " + str(i + 1) + "    "))

for i in range (aruser.__len__()):
    print("The user 1, is: " + aruser[i])
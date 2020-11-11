def pay(price) :
    money = int(input("Isert money   "))
    if money == price :
        print("Complided!!" + "\n" + "Thanks!!")
    elif money < price :
        print("Error, not enoght money")
    elif money > price :
        cambio = money - price
        print("Complided, your change is: " + str(cambio)) 
print("Select product")
product1 = "Coca"
product2 = "Fanta"
product3 = "Sprite"
selection = ""
aux = 1
price = 0
#product = []
while(True):
    print("Coca" + "\n"
    + "Fanta" + "\n" + "Sprite")
    selection = (input("Product:  "))
    if selection.upper().strip() == "COCA":
        product = [0, "COCA", 12]
    elif selection.upper().strip() == "FANTA" :
        product = [1, "FANTA", 13]
    elif selection.upper().strip() == "SPRITE" :
        product = [1, "SPRITE", 14]

    if product[1] == "COCA" :
        price += product[2]
    elif product[1] == "FANTA" :
        price += product[2]
    elif product[1] == "SPRITE" : 
        price += product[2]
    yesno = input("do you wish other product?     ")
    if yesno.upper().strip() == "YES" :
        continue
    else :
        pay(price)
        break
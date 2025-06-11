from random import randint

maxfiy_son = randint(1, 10)  
urinishlar = 3
counter = 0  

while counter < urinishlar:
    taxmin = int(input(f"{counter + 1}-urinish. Sonni toping (1-10): "))
    counter += 1  

    if taxmin == maxfiy_son:
        print(f"Topdingiz! {counter}-urinishda topdingiz ")
        break
    else:
        print("Noto‘g‘ri. Yana urinib ko‘ring.")

else:
    print(f"Urinishlar tugadi. Maxfiy son: {maxfiy_son}")

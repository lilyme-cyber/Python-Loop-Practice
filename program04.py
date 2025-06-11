from random import randint

maxfiy_son = randint(100, 999)

taxmin = 0
while taxmin != maxfiy_son:
    taxmin = int(input("3 xonali son kiriting: "))
    if taxmin != maxfiy_son:
        print("Yana urinib ko‘ring")

print("Siz to‘g‘ri topdingiz")

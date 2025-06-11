answer = "Toshkent"

while True:
    option = input("O'zbekiston poytaxti nima?")
    if option.capitalize() == answer:
        print("siz to'g'ri topdingiz")
        break
else:
    print("siz topolmadingiz")
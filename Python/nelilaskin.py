
def plus(x, y):
    vastaus = x + y
    return vastaus
def minus(x, y):
    vastaus = x - y
    return vastaus
def kerto(x, y):
    vastaus = x * y
    return vastaus
def jako(x, y):
    try:
        vastaus = x / y
    except ZeroDivisionError:
        return print("Tällä ohjelmalla ei pääse äärettömyyteen")
    else:
        return vastaus
valitse = input("Valitse operaatio (+, -, *, /): ")
if valitse in("+", "-", "*", "/"):
    try:
        luku_1 = float(input("Anna luku 1: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else: 
        try:
            luku_2 = float(input("Anna luku 2: "))
        except ValueError:
            print("Ei tämä ole mikään luku")
        else:
            if valitse == "+":
                print(f"Tulos: {plus(luku_1, luku_2)}")
            elif valitse == "-":
                print(f"Tulos: {minus(luku_1, luku_2)}")
            elif valitse == "*":
                print(f"Tulos: {kerto(luku_1, luku_2)}")
            elif valitse == "/":
                if not jako(luku_1, luku_2) is None:
                    print(f"Tulos: {jako(luku_1, luku_2)}")
else: 
    print("Operaatiota ei ole olemassa")

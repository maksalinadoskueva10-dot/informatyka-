

import math

# =====================================================================================================


def wysokosc_trojkata_rownobocznego(a:float)->float:
    return (a*math.sqrt(3))/2

def przekatna_kwadratu(a:float)->float:
    return a*math.sqrt(2)

def twierdzenie_pitagorasa(a:float, b:float, c:float)->bool:
    if math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2):
        return True
    else:
        return False


# =====================================================================================================


def legenda_warunki()->None:
    print("a -- wysokosc_trojkata_rownobocznego")
    print("b -- przekatna_kwadratu")
    print("c -- twierdzenie_pitagorasa")
    print("z -- wyjscie")


def jakie_warunki()->None:
    while True:
        legenda_warunki()
        inp = input().lower().strip()
        if inp == "z":
            print("wyjscie")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} wysokosc_trojkata_rownobocznego = {wysokosc_trojkata_rownobocznego(a)}")
        elif inp == "b":
            a = float(input("a = "))
            print(f"dla {a} przekatna_kwadratu = {przekatna_kwadratu(a)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} twierdzenie_pitagorasa = {twierdzenie_pitagorasa(a,b,c)}")


def menu_warunki()->None:
    jakie_warunki()



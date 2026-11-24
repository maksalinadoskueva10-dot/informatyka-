import math

# =====================================================================================================


def p_kwadratu(a:float)->float:
    return a**2

def p_prostokata(a:float, b:float)->float:
    return a*b

def p_rownolegloboku(a:float, h:float)->float:
    return a*h

def p_trapezu(a:float, b:float, h:float)->float:
    return ((a+b)*h)/2

def p_trojkata(a:float, h:float)->float:
    return (a*h)/2

def p_trojkata_rownobocznego(a:float)->float:
    return (a**2*math.sqrt(3))/4

def p_kola(r:float)->float:
    return math.pi*r**2

def p_rombu_bok_wysokosc(a:float, h:float)->float:
    return a*h

def p_rombu_przekatne(e:float, f:float)->float:
    return (e*f)/2


def legenda_p()->None:
    print("a -- p_kwadratu")
    print("b -- p_prostokata")
    print("c -- p_rownolegloboku")
    print("d -- p_trapezu")
    print("e -- p_trojkata")
    print("f -- p_trojkata_rownobocznego")
    print("g -- p_kola")
    print("h -- p_rombu_bok_wysokosc")
    print("i -- p_rombu_przekatne")
    print("z -- wyjscie")


def jakie_p()->None:
    while True:
        legenda_p()
        inp = input().lower().strip()
        if inp == "z":
            print("wyjscie")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} p_kwadratu = {p_kwadratu(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} p_prostokata = {p_prostokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} p_rownolegloboku = {p_rownolegloboku(a,h)}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"dla {a} {b} {h} p_trapezu = {p_trapezu(a,b,h)}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} p_trojkata = {p_trojkata(a,h)}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"dla {a} p_trojkata_rownobocznego = {p_trojkata_rownobocznego(a)}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"dla {r} p_kola = {p_kola(r)}")
        elif inp == "h":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} p_rombu_bok_wysokosc = {p_rombu_bok_wysokosc(a,h)}")
        elif inp == "i":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"dla {e} {f} p_rombu_przekatne = {p_rombu_przekatne(e,f)}")


# =====================================================================================================


def obw_kwadratu(a:float)->float:
    return 4*a

def obw_prostokata(a:float, b:float)->float:
    return 2*a+2*b

def obw_rownolegloboku(a:float, b:float)->float:
    return 2*a+2*b

def obw_trapezu(a:float, b:float, c:float, d:float)->float:
    return a+b+c+d

def obw_trojkata(a:float, b:float, c:float)->float:
    return a+b+c

def obw_trojkata_rownobocznego(a:float)->float:
    return a*3

def obw_kola(r:float)->float:
    return 2*math.pi*r

def obw_rombu(a:float)->float:
    return a*4


def legenda_obw()->None:
    print("a -- obw_kwadratu")
    print("b -- obw_prostokata")
    print("c -- obw_rownolegloboku")
    print("d -- obw_trapezu")
    print("e -- obw_trojkata")
    print("f -- obw_trojkata_rownobocznego")
    print("g -- obw_kola")
    print("h -- obw_rombu")
    print("z -- wyjscie")


def jaki_obw()->None:
    while True:
        legenda_obw()
        inp = input().lower().strip()
        if inp == "z":
            print("wyjscie")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} obw_kwadratu = {obw_kwadratu(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_prostokata = {obw_prostokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_rownolegloboku = {obw_rownolegloboku(a,b)}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"dla {a} {b} {c} {d} obw_trapezu = {obw_trapezu(a,b,c,d)}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} obw_trojkata = {obw_trojkata(a,b,c)}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"dla {a} obw_trojkata_rownobocznego = {obw_trojkata_rownobocznego(a)}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"dla {r} obw_kola = {obw_kola(r)}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"dla {a} obw_rombu = {obw_rombu(a)}")


# =====================================================================================================


def menu_plaskie()->None:
    while True:
        print("a -- pola figur plaskich")
        print("b -- obwody figur plaskich")
        print("z -- wyjscie")

        inp = input().lower().strip()

        if inp == "a":
            jakie_p()
        elif inp == "b":
            jaki_obw()
        elif inp == "z":
            print("wyjscie")
            break
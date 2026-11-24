import math

# =====================================================================================================


def ob_szescianu(a:float)->float:
    return a**3

def ob_prostopadloscianu(a:float, b:float, c:float)->float:
    return a*b*c

def ob_graniastoslupa(pp:float, h:float)->float:
    return pp*h

def ob_ostroslupa(pp:float, h:float)->float:
    return pp*h/3

def ob_walca(r:float, h:float)->float:
    return math.pi*r**2*h

def ob_stozka(r:float, h:float)->float:
    return (math.pi*r**2*h)/3

def ob_kuli(r:float)->float:
    return math.pi*(4/3)*r**3


def legenda_ob()->None:
    print("a -- ob_szescianu")
    print("b -- ob_prostopadloscianu")
    print("c -- ob_graniastoslupa")
    print("d -- ob_ostroslupa")
    print("e -- ob_walca")
    print("f -- ob_stozka")
    print("g -- ob_kuli")
    print("z -- wyjscie")


def jakie_ob()->None:
    while True:
        legenda_ob()
        inp = input().lower().strip()
        if inp == "z":
            print("wyjscie")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} ob_szescianu = {ob_szescianu(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} ob_prostopadloscianu = {ob_prostopadloscianu(a,b,c)}")
        elif inp == "c":
            pp = float(input("pp = "))
            h = float(input("h = "))
            print(f"dla {pp} {h} ob_graniastoslupa = {ob_graniastoslupa(pp,h)}")
        elif inp == "d":
            pp = float(input("pp = "))
            h = float(input("h = "))
            print(f"dla {pp} {h} ob_ostroslupa = {ob_ostroslupa(pp,h)}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"dla {r} {h} ob_walca = {ob_walca(r,h)}")
        elif inp == "f":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"dla {r} {h} ob_stozka = {ob_stozka(r,h)}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"dla {r} ob_kuli = {ob_kuli(r)}")


# =====================================================================================================


def pc_szescianu(a:float)->float:
    return 6*a**2

def pc_prostopadloscianu(a:float, b:float, c:float)->float:
    return 2*a*b+2*a*c+2*b*c

def pc_graniastoslupa(pp:float, pb:float)->float:
    return 2*pp+pb

def pc_ostroslupa(pp:float, pb:float)->float:
    return pp+pb

def pc_walca(r:float, h:float)->float:
    return 2*math.pi*r**2+2*math.pi*r*h

def pc_stozka(r:float, l:float)->float:
    return math.pi*r**2+math.pi*r*l

def pc_kuli(r:float)->float:
    return 4*math.pi*r**2


def legenda_pc()->None:
    print("a -- pc_szescianu")
    print("b -- pc_prostopadloscianu")
    print("c -- pc_graniastoslupa")
    print("d -- pc_ostroslupa")
    print("e -- pc_walca")
    print("f -- pc_stozka")
    print("g -- pc_kuli")
    print("z -- wyjscie")


def jakie_pc()->None:
    while True:
        legenda_pc()
        inp = input().lower().strip()
        if inp == "z":
            print("wyjscie")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} pc_szescianu = {pc_szescianu(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} pc_prostopadloscianu = {pc_prostopadloscianu(a,b,c)}")
        elif inp == "c":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"dla {pp} {pb} pc_graniastoslupa = {pc_graniastoslupa(pp,pb)}")
        elif inp == "d":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"dla {pp} {pb} pc_ostroslupa = {pc_ostroslupa(pp,pb)}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"dla {r} {h} pc_walca = {pc_walca(r,h)}")
        elif inp == "f":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"dla {r} {l} pc_stozka = {pc_stozka(r,l)}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"dla {r} pc_kuli = {pc_kuli(r)}")


# =====================================================================================================

def menu_bryly()->None:
    while True:
        print("a -- objetosci bryl")
        print("b -- pola powierzchni bryl")
        print("z -- wyjscie")

        inp = input().lower().strip()

        if inp == "a":
            jakie_ob()
        elif inp == "b":
            jakie_pc()
        elif inp == "z":
            print("wyjscie")
            break



import math

print("Bryly - a | Plaskie - b | Inne - c")
inp = input("inp: ").lower().strip()

if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print("ppSzecianu - a | ppProstopadloscianu - b | ppGraniastoslupa - c | ppOstroslupa - d | ppWalca - e | ppStozka - f | ppKuli - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            a = float(input("a = "))
            print(f"ppSzecianu o boku {a} = {6*a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu o bokach {a} {b} {c} = {2*a*b+2*b*c+2*c*a}")
        elif inp == "c":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"ppGraniastoslupa {pp} {pb} = {(2*pp)+pb}")
        elif inp == "d":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"ppOstroslupa {pp} {pb} = {pp+pb}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"ppWalca {r} {h} = {2*math.pi*r**2 + 2*math.pi*r*h}")
        elif inp == "f":
            r = float(input("r = "))
            i = float(input("i = "))
            print(f"ppStozka {r} {i} = {math.pi*r**2+math.pi*r*i}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"ppKuli {r} = {4*math.pi*r**2}")
        else:
            print("Nie ma takiej komendy: ")
    elif inp == "b":
        print("vSzecianu - a | vProstopadloscianu - b | vGraniastoslupa - c | vOstroslupa - d | vWalca - e | vStozka - f | vKuli - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            a = float(input("a = "))
            print(f"objetosc szescianu {a} = {a**3}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"objetosc prostopadloscianu {a} {b} {c} = {a*b*c}")
        elif inp == "c":
            pp = float(input("pp = "))
            h = float(input("h = "))
            print(f"vGraniastoslupa {pp} {h} = {pp*h}")
        elif inp == "d":
            pp = float(input("pp = "))
            h = float(input("h = "))
            print(f"vOstroslupa {pp} {h} = {(pp/3)*h}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"vWalca {r} {h} = {math.pi*r**2*h}")
        elif inp == "f":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"vStozka {r} {h} = {(math.pi/3)*r**2*h}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"vKuli {r} = {4/3*math.pi*r**3}")
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")

elif inp == "c":
    print("wysokosc trojkata rownobocznego - a | przekatna kwadratu - b | twierdzenie pitagorasa - c")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        a = float(input("a = "))
        print(f"wysokosc trojkata rownobocznego {a} = {(a*math.sqrt(3))/2}")
    elif inp == "b":
        a = float(input("a = "))
        print(f"przekatna kwadratu {a} = {a*math.sqrt(2)}")
    elif inp == "c":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f" twierdzenie pitagorasa {a} {b} {c} = {(a**2+b**2==c**2) or (b**2+c**2==a**2) or (c**2+a**2==b**2)}")
    else:
        print("nie ma takiej komendy")

elif inp == "b":
    print("obwody fig plaskie - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()
    
    if inp == "a":
        print("obwod kwadratu - a | obwod prostokata - b | obwod rownolegloboku - c | obwod trapezu - d | obwod trojkata - e | obwod trojkata rownobocznego - f | obwod kola - g | obwod rombu - h")
        inp = input("inp: ").lower().strip() 
        
        if inp == "a":
            a = float(input("a = "))
            print(f"obwod kwadratu {a} = {4*a}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"obwod prostokata {a} {b} = {a*2+b*2}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"obwod rownolegloboku {a} {b} = {a*2+b*2}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"obwod trapezu {a} {b} {c} {d} = {a+b+c+d}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"obwod trojkata {a} {b} {c} = {a+b+c}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"obwod trojkata rownobocznego {a} = {a*3}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"obwod kola {r} = {2*math.pi*r}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"obwod rombu {a} = {a*4}")
        else:
            print("nie ma takiej komendy")
            
    elif inp == "b":
        print("pole kwadratu - a | pole prostokata - b | pole rownolegloboku - c | pole trapezu - d | pole trojkata - e | pole trojkata rownobocznego - f | pole kola - g | pole rombu - h")
        inp = input("inp: ").lower().strip()
        
        if inp == "a":
            a = float(input("a = "))
            print(f"pole kwadtatu {a} = {a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"pole prostokata {a} {b} = {a*b}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pole rownolegloboku {a} {h} = {a*h}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"pole trapezu {a} {b} {h} = {((a+b)*h)/2}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pole trojkata {a} {h} = {(1/2)*a*h}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"pole trojkata rownobocznego {a} = {(a**2*math.sqrt(3))/4}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"pole kola {r} = {math.pi*r**2}")
        elif inp == "h":
            print("pole rombu z boku i wysokosci - a | pole rombu z przekatnych - b")
            inp = input("inp: ").lower().strip()
            if inp == "a":
                a = float(input("a = "))
                h = float(input("h = "))
                print(f"pole rombu {a} {h} = {a*h}")
            elif inp == "b":
                e = float(input("e = "))
                f = float(input("f = "))
                print(f"pole rombu {e} {f} = {(e*f)/2}")
            else:
                print("nie ma takiej komendy")
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")
else:
    print("nie ma takiej komendy")
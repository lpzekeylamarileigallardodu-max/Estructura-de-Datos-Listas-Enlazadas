class NodoC:
    def __init__(self, xd):
        self.id = xd
        self.sig = None

def juego(n):
    pri = NodoC(1); ult = pri
    for i in range(2, n + 1):
        nuevo = NodoC(i)
        ult.sig = nuevo
        ult = nuevo
    ult.sig = pri # Cierra el circulo
    
    act = pri
    while act.sig != act:
        print(f"Sale el: {act.sig.id}")
        act.sig = act.sig.sig
        act = act.sig
    print(f"Sobrevive el: {act.id}")

n = int(input("Numero de personas: "))
juego(n)

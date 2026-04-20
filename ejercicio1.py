from libreria import ListaX, random

l1 = ListaX()
for i in range(25):
    l1.meter_ordenado(random.randint(1, 1500))
print("Lista 1 (1-1500) ordenada:")
l1.ver_lista()

l2 = ListaX()
t = l1.cabeza
while t:
    if t.dato < 100:
        l2.meter_ordenado(t.dato)
    t = t.sig
print("\nLista 2 (solo menores a 100):")
l2.ver_lista()

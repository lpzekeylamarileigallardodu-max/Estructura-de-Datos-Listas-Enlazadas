from libreria import ListaX, random

n = int(input("Cuantos numeros para la lista N: "))
m = int(input("Cuantos numeros para la lista M: "))

ln = ListaX(); lm = ListaX()

for i in range(n): ln.meter_final(round(random.uniform(1, 10), 2))
for i in range(m): lm.meter_final(round(random.uniform(1, 10), 2))

lp = ListaX()
tn = ln.cabeza
while tn:
    tm = lm.cabeza
    while tm:
        lp.meter_final(round(tn.dato * tm.dato, 2))
        tm = tm.sig
    tn = tn.sig

print("\nLista P (Productos de N x M):")
lp.ver_lista()

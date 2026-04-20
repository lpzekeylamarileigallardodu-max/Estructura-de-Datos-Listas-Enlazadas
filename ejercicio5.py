from libreria import ListaX

def menu():
    lista = ListaX()
    while True:
        print("\n--- MENU ---")
        print("a. Crear lista\nb. Insertar final\nc. Posicion\nd. Borrar\ne. Reportar\nf. Contar\ng. Salir")
        op = input("Opcion: ").lower()
        if op == 'g': break
        elif op == 'a': lista = ListaX(); print("Lista limpia.")
        elif op == 'b': lista.meter_final(float(input("Valor: ")))
        elif op == 'c': lista.meter_en_pos(float(input("Valor: ")), int(input("Pos: ")))
        elif op == 'd': lista.borrar_pos(int(input("Pos: ")))
        elif op == 'e': lista.ver_lista()
        elif op == 'f': print("Total:", lista.contar())

menu()

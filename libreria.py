import random

class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.sig = None

class ListaX:
    def __init__(self):
        self.cabeza = None

    def meter_ordenado(self, num):
        nuevo = Nodo(num)
        if self.cabeza is None or self.cabeza.dato >= num:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo
        else:
            temp = self.cabeza
            while temp.sig and temp.sig.dato < num:
                temp = temp.sig
            nuevo.sig = temp.sig
            temp.sig = nuevo

    def meter_final(self, num):
        nuevo = Nodo(num)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            temp = self.cabeza
            while temp.sig:
                temp = temp.sig
            temp.sig = nuevo

    def meter_en_pos(self, num, pos):
        nuevo = Nodo(num)
        if pos == 0:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo
            return
        temp = self.cabeza
        for i in range(pos - 1):
            if temp: temp = temp.sig
        if temp:
            nuevo.sig = temp.sig
            temp.sig = nuevo

    def borrar_pos(self, pos):
        if not self.cabeza: return
        if pos == 0:
            self.cabeza = self.cabeza.sig
            return
        temp = self.cabeza
        for i in range(pos - 1):
            if temp: temp = temp.sig
        if temp and temp.sig:
            temp.sig = temp.sig.sig

    def ver_lista(self):
        temp = self.cabeza
        while temp:
            print(f"[{temp.dato}]", end=" -> ")
            temp = temp.sig
        print("Fin")

    def contar(self):
        c = 0
        temp = self.cabeza
        while temp:
            c += 1
            temp = temp.sig
        return c

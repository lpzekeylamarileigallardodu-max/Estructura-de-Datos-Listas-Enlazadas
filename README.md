LISTAS ENLAZADAS TEORIA
1. Definición de Lista Enlazada
Es una estructura de datos donde los elementos, llamados nodos, se conectan entre sí usando punteros. A diferencia de una lista normal, los datos no están uno al lado del otro en la memoria de la compu, sino ellos no tienen un odren específico y lo único que puede encontrarle uno, son sus next o direcciones. Existe uno que inicia todo llamado head y otro donde su puntero indica tierra o null.
2. Comparación con Array y Vector
Lista Enlazada: es editable siempre y cuando todos los nodos anteriores sean leídos para encontrar el lugar específico de modificación.
Array: Tiene un tamaño fijo desde el inicio. Es muy rápido para encontrar datos por su posición que es como un índice.
Vector: Es un punto medio, crece solo y los lugares de modificación se recorren una casilla.
3. Código de Estructura (Nodos y Punteros)
Base utilizada en el archivo libreria.py para que la lista funcione:
class Nodo:
    def __init__(self, xd):
        self.valor = xd  # El dato (numero real)
        self.sig = None  # El puntero al siguiente nodo
4. Métodos de Manipulación
Aquí se muestra cómo la lista puede agregar elementos al final y cómo podemos borrar uno en cualquier posición:
# insertar al final
def meter_final(self, lol):
    nuevo = Nodo(lol)
    if not self.cabeza:
        self.cabeza = nuevo
    else:
        temp = self.cabeza
        while temp.sig:
            temp = temp.sig
        temp.sig = nuevo
# eliminar
def borrar_pos(self, pos):
    if not self.cabeza: return
    if pos == 0:
        self.cabeza = self.cabeza.sig
5. Uso funcional en métodos
En los ejercicios, se demuestra que los métodos funcionan al generar listas aleatorias, ordenarlas automáticamente y realizar operaciones matemáticas (como la multiplicación de listas) recorriendo cada nodo de forma secuencial.
6. Aplicaciones Prácticas
Historial de Navegador: Para ir hacia atrás y adelante entre páginas.
Lista de Reproducción de Música: Para saltar a la siguiente canción.
Gestión de procesos en el sistema: Para turnos de programas en espera.

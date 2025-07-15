class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaClientes:
    def __init__(self):
        self.head = None
    
    def agregar(self, data):
        nuevo_nodo = Nodo(data)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

# Uso: clientes_db = ListaClientes()
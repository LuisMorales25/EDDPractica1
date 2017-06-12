class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaCircularDoblementeEnlazada:
    def __init__(self):
        self.primero=None
        self.Ultimo=None

    def vacia(self):
        if self.primero==None:
            return True
        else:
            return False

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.Ultimo=Nodo(dato)
        else:
            aux=Nodo(dato)
            aux.siguiente=self.primero
            self.primero.anterior=aux
            self.primero=aux
        self.__unirNodos()


    def agregar_final(self, dato):
        if self.vacia():
            self.primero=self.Ultimo=Nodo(dato)
        else:
            aux=self.Ultimo
            self.Ultimo=aux.siguiente=Nodo(dato)
            self.Ultimo.anterior=aux
        self.__unirNodos()

    def __unirNodos(self):
        self.primero.anterior=self.Ultimo
        self.Ultimo.siguiente=self.primero

    def recorrer_inicio_fin(self):
        aux=self.primero
        while aux:
            print(aux.dato)
            aux=aux.siguiente
            if aux==self.primero:
                break

    def recorrer_fin_inicio(self):
        aux=self.Ultimo
        while aux:
            print(aux.dato)
            aux=aux.anterior
            if aux==self.Ultimo:
                break
    
    
    

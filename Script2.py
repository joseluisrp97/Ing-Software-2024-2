# Función para contar el número de valles en una caminata
def contar_valles(caminata):
    """
    Cuenta el número de valles recorridos en una caminata.
    :param caminata: Cadena de caracteres donde 'U' representa un paso hacia arriba y 'D' un paso hacia abajo.
    :return: Número de valles recorridos.
    """
    nivel_mar = 0  # Inicialización del nivel del mar
    valles = 0  # Contador de valles
    en_valle = False  # Indicador de si el caminante está actualmente en un valle

    # Iterar sobre cada paso en la caminata
    for paso in caminata:
        if paso == 'U':  # Paso hacia arriba
            nivel_mar += 1
            # Si vuelve al nivel del mar y estaba en un valle, incrementar el contador de valles
            if nivel_mar == 0 and en_valle:
                valles += 1
                en_valle = False
        else:  # paso == 'D', Paso hacia abajo
            if nivel_mar == 0:
                en_valle = True
            nivel_mar -= 1

    return valles

# Clase Nodo para representar cada nodo en el árbol binario
class Nodo:
    """
    Nodo de un árbol binario.
    
    :param valor: Valor almacenado en el nodo.
    """
    def __init__(self, valor):
        self.valor = valor  # Valor del nodo
        self.izquierdo = None  # Nodo hijo izquierdo
        self.derecho = None  # Nodo hijo derecho

# Clase para representar un árbol binario ordenado
class ArbolBinarioOrdenado:
    """
    Árbol binario ordenado.
    """
    def __init__(self):
        self.raiz = None  # Raíz del árbol

    def agregar(self, valor):
        """
        Agrega un nuevo valor al árbol binario ordenado.
        
        :param valor: Valor a agregar al árbol.
        """
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo):
        """
        Método auxiliar para agregar un nuevo valor al árbol de forma recursiva.
        
        :param valor: Valor a agregar.
        :param nodo: Nodo actual en la recursión.
        """
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar(valor, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar(valor, nodo.derecho)

    # Métodos para realizar recorridos en el árbol
    def recorrido_preorden(self):
        """
        Realiza un recorrido pre-orden del árbol y devuelve una lista de los valores.
        
        :return: Lista con los valores del árbol en pre-orden.
        """
        elementos = []
        self._preorden(self.raiz, elementos)
        return elementos

    def _preorden(self, nodo, elementos):
        """
        Método auxiliar para realizar el recorrido pre-orden de forma recursiva.
        
        :param nodo: Nodo actual en la recursión.
        :param elementos: Lista acumulativa de elementos visitados.
        """
        if nodo:
            elementos.append(nodo.valor)
            self._preorden(nodo.izquierdo, elementos)
            self._preorden(nodo.derecho, elementos)

    def recorrido_inorden(self):
        """
        Realiza un recorrido in-orden del árbol y devuelve una lista de los valores.
        
        :return: Lista con los valores del árbol en in-orden.
        """
        elementos = []
        self._inorden(self.raiz, elementos)
        return elementos

    def _inorden(self, nodo, elementos):
        """
        Método auxiliar para realizar el recorrido in-orden de forma recursiva.
        
        :param nodo: Nodo actual en la recursión.
        :param elementos: Lista acumulativa de elementos visitados.
        """
        if nodo:
            self._inorden(nodo.izquierdo, elementos)  # Visita el subárbol izquierdo
            elementos.append(nodo.valor)              # Visita el nodo actual
            self._inorden(nodo.derecho, elementos)    # Visita el subárbol derecho

    def recorrido_postorden(self):
        """
        Realiza un recorrido post-orden del árbol y devuelve una lista de los valores.

        :return: Lista con los valores del árbol en post-orden.
        """
        elementos = []
        self._postorden(self.raiz, elementos)
        return elementos

    def _postorden(self, nodo, elementos):
        """
        Método auxiliar para realizar el recorrido post-orden de forma recursiva.
           
        :param nodo: Nodo actual en la recursión.
        :param elementos: Lista acumulativa de elementos visitados.
        """
        if nodo:
            self._postorden(nodo.izquierdo, elementos)  # Visita el subárbol izquierdo
            self._postorden(nodo.derecho, elementos)    # Visita el subárbol derecho
            elementos.append(nodo.valor)                # Visita el nodo actual

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de contar valles
    caminata = "DDUUDDUDUUUD"
    print("Número de valles:", contar_valles(caminata))

    # Ejemplo de uso del árbol binario ordenado
    valores = [3, 1, 4, 2, 5]
    arbol = ArbolBinarioOrdenado()
    for valor in valores:
        arbol.agregar(valor)

    print("Recorrido Preorden:", arbol.recorrido_preorden())
    print("Recorrido Inorden:", arbol.recorrido_inorden())
    print("Recorrido Postorden:", arbol.recorrido_postorden())


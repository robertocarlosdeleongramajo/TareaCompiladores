# src/arbol.py
class Nodo:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def mostrar_arbol(nodo, prefijo="", es_ultimo=True):
    conector = "└── " if es_ultimo else "├── "
    print(f"{prefijo}{conector}{nodo.tipo}{': ' + str(nodo.valor) if nodo.valor else ''}")
    
    prefijo += "    " if es_ultimo else "│   "
    contador = len(nodo.hijos)
    for i, hijo in enumerate(nodo.hijos):
        ultimo_hijo = (i == contador - 1)
        mostrar_arbol(hijo, prefijo, ultimo_hijo)
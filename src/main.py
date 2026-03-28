# Tarea: Árbol Sintáctico - Compiladores
# Fecha: 28 de marzo de 2026

class Nodo:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def mostrar_arbol(nodo, prefijo="", es_ultimo=True):
    # Formato visual tipo árbol de carpetas
    conector = "└── " if es_ultimo else "├── "
    print(f"{prefijo}{conector}{nodo.tipo}{': ' + str(nodo.valor) if nodo.valor else ''}")
    
    prefijo += "    " if es_ultimo else "│   "
    contador = len(nodo.hijos)
    for i, hijo in enumerate(nodo.hijos):
        ultimo_hijo = (i == contador - 1)
        mostrar_arbol(hijo, prefijo, ultimo_hijo)

# --- Construcción del Árbol Sintáctico ---
def ejemplo_javascript():
    print("Ejemplo 1: if (edad >= 18) { console.log(...) }")
    raiz = Nodo("SentenciaIf")
    
    # Condición
    cond = Nodo("Comparación", ">=")
    cond.agregar_hijo(Nodo("ID", "edad"))
    cond.agregar_hijo(Nodo("Número", "18"))
    raiz.agregar_hijo(cond)
    
    # Cuerpo
    cuerpo = Nodo("Bloque")
    print_log = Nodo("Llamada", "console.log")
    print_log.agregar_hijo(Nodo("String", "'Eres mayor de edad'"))
    cuerpo.agregar_hijo(print_log)
    raiz.agregar_hijo(cuerpo)
    
    mostrar_arbol(raiz)

if __name__ == "__main__":
    ejemplo_javascript()
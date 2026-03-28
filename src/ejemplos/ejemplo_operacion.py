# src/ejemplos/ejemplo_operacion.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from arbol import Nodo, mostrar_arbol

def ejecutar():
    codigo = """
    // Contador simple
    while (contador < 5) {
        contador = contador + 1;
        print(contador);
    }
    """
    print("\n" + "="*60)
    print("ANALIZANDO CÓDIGO FUENTE (Bucle While):")
    print(codigo)
    print("="*60)

    # Construcción del AST
    raiz = Nodo("BucleWhile")
    
    # Condición del bucle
    condicion = Nodo("Condición", "<")
    condicion.agregar_hijo(Nodo("ID", "contador"))
    condicion.agregar_hijo(Nodo("Número", "5"))
    raiz.agregar_hijo(condicion)
    
    # Cuerpo del bucle
    cuerpo = Nodo("CuerpoBucle")
    
    # contador = contador + 1
    incremento = Nodo("Asignación", "=")
    incremento.agregar_hijo(Nodo("ID", "contador"))
    suma = Nodo("Operación", "+")
    suma.agregar_hijo(Nodo("ID", "contador"))
    suma.agregar_hijo(Nodo("Número", "1"))
    incremento.agregar_hijo(suma)
    
    # print(contador)
    imprimir = Nodo("Llamada", "print")
    imprimir.agregar_hijo(Nodo("ID", "contador"))
    
    cuerpo.agregar_hijo(incremento)
    cuerpo.agregar_hijo(imprimir)
    raiz.agregar_hijo(cuerpo)
    
    print("\nAST GENERADO:")
    mostrar_arbol(raiz)
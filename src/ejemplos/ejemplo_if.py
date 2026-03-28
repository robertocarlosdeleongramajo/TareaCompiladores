# src/ejemplos/ejemplo_if.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from arbol import Nodo, mostrar_arbol

def ejecutar():
    codigo = """
    // Validación de acceso
    if (edad >= 18) {
        status = "Permitido";
        console.log("Acceso concedido");
    } else {
        console.log("Acceso denegado");
    }
    """
    print("\n" + "="*60)
    print("ANALIZANDO CÓDIGO FUENTE (Control de Acceso):")
    print(codigo)
    print("="*60)

    # Construcción del AST
    raiz = Nodo("SentenciaIfElse")
    
    # Condición
    cond = Nodo("Comparación", ">=")
    cond.agregar_hijo(Nodo("ID", "edad"))
    cond.agregar_hijo(Nodo("Número", "18"))
    raiz.agregar_hijo(cond)
    
    # Bloque IF
    bloque_if = Nodo("BloqueTrue")
    asig = Nodo("Asignación", "=")
    asig.agregar_hijo(Nodo("ID", "status"))
    asig.agregar_hijo(Nodo("String", "'Permitido'"))
    bloque_if.agregar_hijo(asig)
    
    log_ok = Nodo("Llamada", "console.log")
    log_ok.agregar_hijo(Nodo("String", "'Acceso concedido'"))
    bloque_if.agregar_hijo(log_ok)
    raiz.agregar_hijo(bloque_if)

    # Bloque ELSE
    bloque_else = Nodo("BloqueFalse")
    log_no = Nodo("Llamada", "console.log")
    log_no.agregar_hijo(Nodo("String", "'Acceso denegado'"))
    bloque_else.agregar_hijo(log_no)
    raiz.agregar_hijo(bloque_else)
    
    print("\nAST GENERADO:")
    mostrar_arbol(raiz)
# src/main.py
import sys
import os

# Añadir la ruta para que encuentre la carpeta ejemplos
ruta_src = os.path.dirname(os.path.abspath(__file__))
if ruta_src not in sys.path:
    sys.path.append(ruta_src)

try:
    from ejemplos import ejemplo_if, ejemplo_operacion
except ImportError as e:
    print(f"[!] Error: {e}")
    sys.exit(1)

def mostrar_menu():
    while True:
        print("\n" + "="*45)
        print("     MENÚ DE ÁRBOLES SINTÁCTICOS (AST)     ")
        print("="*45)
        print("1. Generar Árbol: Sentencia IF (JavaScript)")
        print("2. Generar Árbol: Operación Matemática")
        print("3. Salir del programa")
        print("-"*45)
        
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            ejemplo_if.ejecutar()
        elif opcion == "2":
            ejemplo_operacion.ejecutar()
        elif opcion == "3":
            print("\nSaliendo... ¡Éxitos en tu tarea de Compiladores!")
            break

if __name__ == "__main__":
    mostrar_menu()
from colorama import init, Fore, Back, Style

init()

def main():
    print(Fore.GREEN + "==Menú del Gallinero==")

##Avance 1 Grupo 2##

opcion = ""

while opcion != "5":
    print(Fore.GREEN + "==Menú del Gallinero==")
    print("1. Incluir datos")
    print("2. Consultar datos")
    print("3. Modificar datos")
    print("4. Borrar datos")
    print("5. Salir")
    opcion = input(Fore.BLUE + "Seleccione una opcion: ")

    if opcion == "1":
       print(Fore.RED + "_-Opción en Mantenimiento-_")

    elif opcion == "2":
        print(Fore.RED + "_-Opción en Mantenimiento-_")

    elif opcion == "3":
       print(Fore.RED + "_-Opción en Mantenimiento-_")

    elif opcion == "4":
        print(Fore.RED + "_-Opción en Mantenimiento-_")

    elif opcion == "5":
        print(Fore.WHITE + "Fin del programa")

    else:
        print(Fore.LIGHTRED_EX + "Opción no válida")
        print(Fore.YELLOW + "=====Fin del Programa=====")

    

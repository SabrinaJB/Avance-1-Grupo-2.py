from colorama import init, Fore, Back, Style

try:
    from colorama import init, Fore
    init()
    verde = Fore.GREEN
    rojo = Fore.RED
    azul = Fore.BLUE
    blanco = Fore.WHITE
    rosa = Fore.LIGHTRED_EX
    amarillo = Fore.YELLOW
except ImportError:
    # Si no hay colorama, se desactivan los colores
    verde = rojo = azul = blanco = rosa = amarillo = ""

gallinas = [[0 for _ in range(7)] for _ in range(6)]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]

def mostrar_menu():
    print(Fore.YELLOW + "\n=== MENÚ ===" + Style.RESET_ALL)
    print("1. Ingresar datos de huevos")
    print("2. Consultar datos")
    print("3. Borrar datos")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input(Fore.BLUE + "Seleccione una opción (1-4): " + Style.RESET_ALL)

    if opcion == "1":
        print(Fore.GREEN + "\n--- Ingreso de datos ---" + Style.RESET_ALL)
        for i in range(6):
            print(f"\nGallina #{i + 1}")
            for j in range(7):
                huevos = int(input(f"¿Cuántos huevos puso el {dias[j]}? "))
                gallinas[i][j] = huevos
        print(Fore.GREEN + "Datos registrados correctamente." + Style.RESET_ALL)

    elif opcion == "2":
        print(Fore.GREEN + "\n--- Consulta de datos ---" + Style.RESET_ALL)
        total_general = 0
        for j in range(7):
            total_dia = sum(g[j] for g in gallinas)
            print(f"{dias[j]}: {total_dia} huevos")
            total_general += total_dia

        print("\nTotal por gallina en la semana:")
        for i in range(6):
            total_gallina = sum(gallinas[i])
            print(f"- Gallina #{i + 1}: {total_gallina} huevos")

        print(f"\nTOTAL GENERAL: {total_general} huevos")

    elif opcion == "3":
        gallinas = [[0 for _ in range(7)] for _ in range(6)]
        print(Fore.GREEN + "Todos los datos han sido borrados." + Style.RESET_ALL)

    elif opcion == "4":
        print(Fore.YELLOW + "Saliendo del programa. ¡Hasta luego!" + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "Opción no válida. Intente de nuevo." + Style.RESET_ALL)

    

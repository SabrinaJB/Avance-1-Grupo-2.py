while True:
    print("MENÚ DE OPCIONES")
    print("1. Incluir")
    print("2. Consultar")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        print("Has elegido incluir datos.")
    elif opcion == "2":
        print("Has elegido consultar datos.")
    elif opcion == "3":
        print("Has elegido modificar datos.")
    elif opcion == "4":
        print("Has elegido borrar datos.")
    elif opcion == "5":
        print("Saliendo del programa. ¡Adios!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
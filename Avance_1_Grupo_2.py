# 6 Avance_1_Grupo_12
#   KENDALL ELIAS QUIRÓS PANIAGUA
#   ANA SABRINA JIMENEZ BARQUERO
#   JOSE ANDRES RIVERA HERRERA



#menu principal
x = 0
while x !=5:
    print("MENU de Opciones")
    print("1 Incluir")
    print("2 Consultar")
    print("3 Modificar")
    print("4 Borrar")
    print("5 Salir")
    x = input('Ingrese la opcion deseada')
    x = int(x)

#1 Incluir
    if (x == 1):
        print("Elegiste la opcion: Incluir")

#2 Consultar
    elif(x == 2):
        print("Elegiste la opcion: Consultar")

#3 Modificar
    elif(x == 3):
        print("Escogiste la opcion: Modificar")

#4 Borrar
    elif(x == 4):
        print("Escogiste la opcion: Borrar")

#5 Salir
    elif(x == 5):
        print("Escogiste la opcion: Salir")
        break

#6 Opcion incorrecta volver a intentar
    else:
        print("opcion no valida")
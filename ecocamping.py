print("Gestion de Eco-Camping 'Bosque vivo'")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENÚ DE CONTROL DE REGISTRO===")
    print("1.- Ver sitios disponibles")
    print("2.- Registro de nuevos vehiculos en el sitio(Entrada)")
    print("3.- Registro de salida de vehiculo(Salidad)")
    print("4.- Estado actual del camping")
    print("5.- Salir")
    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida, por favor seleccione entre 1 y 5")
        continue
    #Despliegue de opciones
    if opcion == 1:
        disponibles = capacidad_maxima-sitios_ocupados
        print(F"\n[INFO] Sitios libres para recibir vehiculos: {disponibles}")
    elif opcion == 2:
        sitios_libres = capacidad_maxima-sitios_ocupados
        if sitios_libres == 0:
            print("Lo sentimos, no quedan espacios en el camping")
        else:
            try:
                ingreso = int(input("¿Cuantos sitios o vehiculos van a ingresar"))
                if ingreso <= 0:
                    print("Error: la cantidad de ingreso debe ser mayor a 0")
                elif ingreso > sitios_libres:
                    print(f"Solo puede ingresar un maximo de {sitios_libres} sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"Ingreso registrado, se han ocupado {ingreso} de sitios")
            except ValueError:
                print("Error: Debe ingresar un número valido")
    elif opcion == 3:
        print(f"\n-- Registrar salida (Vehiculos o sitios ocupados: {sitios_ocupados})")
        if sitios_ocupados = 0:
            print("No hay vehiculos registrados en el camping actualmente")
        else:
            try:
                salida = int(input("¿Cuantos vehiculos se retiran?: "))
                if salida <= 0:
                    print("Error: la cantidad a retirar debe ser mayor a 0")
                elif salida > sitios_ocupados
                    print(f"Error: no se pueden retirar mas de {sitios_libres} vehiculos")
                else:
                    sitios_ocupados -= salida
                    print(f"Salida registrada, se han liberado {salida} sitios")
            except ValueError:
                print("Error: Debe ingresar un numero entero valido")
    else:
        print("Opcion fuera de rango")
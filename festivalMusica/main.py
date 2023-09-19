opcion=0
print("\n******** Festival de Musica ********")
print("***********************************")
print("1. Cual es la agrupación musical que se va a presentar:")
print("2. Agrupaciones ingresadas: ")
print("3. Cambiar la hora de la presentacion: ")
print("4. Retirar una agrupación: ")
print("5. Salir")

agrupaciones = []
while opcion != 5:
    agrupacion={}
    opcion=int(input("Digita la opción deseada: "))
    if opcion == 1:
        print("\n**** Ingresa nuevo agrupación ****")
        agrupacion["codigo"] = int(input("Ingresa el ID de la banda: "))
        agrupacion["nombre"] = input("Ingresa nombre de la banda: ")
        agrupacion["genero"] = input("Ingresa el genero musical de la banda: ")
        agrupacion["hora"] = input("Ingrese la hora en la que se presenta: ")
        agrupacion["pago"] = float(input("Ingrese el pago que se le va a dar a la banda: "))
        agrupacion["estado"] = False
        agrupaciones.append(agrupacion)
    elif opcion == 2:
        print("\n**** Mostrando Agrupaciones ****")
        for agrupacionSeleccionada in agrupaciones:
            print (f"Codigo = {agrupacionSeleccionada['codigo']}")
            print(f"Nombre = {agrupacionSeleccionada['nombre']}")
            print(f"Genero =  {agrupacionSeleccionada['genero']}")
            print(f"Hora =  {agrupacionSeleccionada['hora']}")
            print(f"Pago =  {agrupacionSeleccionada['pago']}")
            print(f"Estado = {agrupacionSeleccionada['estado']}")
    elif opcion == 3:  
        
        id_buscar = int(input("\nIngrese el ID de la agrupación cuya hora de presentación desea cambiar: "))
        for agrupacion in agrupaciones:
            if agrupacion["codigo"] == id_buscar and not agrupacion["estado"]:
                nueva_hora = input("Ingrese la nueva hora de presentación: ")
                agrupacion["hora"] = nueva_hora
                print("Hora de presentación actualizada con éxito.")
                break
        else:
            print("\nAgrupación no encontrada o ya se ha presentado.")
    elif opcion == 4: 
        # buscar = int(input("Ingresa el código de la banda que desea eliminar: "))
        # for eliminarBanda in agrupaciones:
        #     if eliminarBanda['codigo'] == buscar:
        #         agrupaciones.pop(agrupacion)
        #         break
            
            # Retirando una agrupación que no se ha presentado del listado de agrupaciones
        id_retirar = int(input("\nIngrese el ID de la agrupación que desea retirar: "))
        for agrupacion in agrupaciones:
            if agrupacion["codigo"] == id_retirar and not agrupacion["estado"]:
                agrupaciones.remove(agrupacion)
                print("Agrupación retirada con éxito.")
                break
        else:
            print("\nAgrupación no encontrada o ya se ha presentado.")
    elif opcion == 5:
        print("Gracias, hasta pronto.")
    else:
        print("Opción inválida.")
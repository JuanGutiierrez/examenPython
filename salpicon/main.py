opcion=0
print("\n******** Prepare su salpicon ********")
print("***********************************")
print("1. Defina las frutas con las que va a preparar su salpicon:")
print("2. Frutas ingresadas para preparar el salpicon: ")
print("3. Fruta mas barata: ")
print("4. Fruta mas cara: ")
print("5. Salir")

frutas = []
frutas.sort(reverse=True)
while opcion != 5:
    fruta={}
    opcion=int(input("Digita la opción deseada: "))
    if opcion == 1:
        print("\n**** Ingresa nuevo producto ****")
        fruta["codigo"] = int(input("Ingresa el ID de la fruta: "))
        fruta["nombre"] = input("Ingresa nombre de la fruta: ")
        fruta["precioUnitario"] = float(input("Ingresa el precio unitario de la fruta: "))
        fruta["cantidad"] = input("Ingrese la cantidad: ")
        frutas.append(fruta)
    elif opcion == 2:
        
        print("\n**** Mostrando frutas ****")
        for frutaSeleccionada in frutas:
            print (f"Codigo = {frutaSeleccionada['codigo']}")
            print(f"Nombre = {frutaSeleccionada['nombre']}")
            print(f"Descripcion =  {frutaSeleccionada['precioUnitario']}")
            print(f"esta es la cantidad de la fruta ingresada = {frutaSeleccionada['cantidad']}")
        
    elif opcion == 3:
        costoTotal = ['precioUnitario'] * ['cantidad']
        print(f"El consto total es: {costoTotal}")
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("Gracias, hasta pronto.")
    else:
        print("Opción inválida.")
reservas = []

# FUNCIONES

def calcular_categoria(total):
    if total < 200000:
        return "Economica"
    elif total <= 500000:
        return "Estandar"
    else:
        return "Premium"

def buscar_posicion(reservas, codigo):
    for i in range(len(reservas)):
        if reservas[i]["Codigo"] == codigo:
            return i
    return -1

def validar_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto.strip() != "":
            return texto
        print("Error: No puede estar vacío.")

def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Debe ser mayor que 0.")
        except:
            print("Ingrese un número entero válido.")

# OPCION 1

def registrar_reserva():

    codigo = validar_texto("Código: ")

    if buscar_posicion(reservas, codigo) != -1:
        print("Ese código ya existe.")
        return

    nombre = validar_texto("Nombre huésped: ")
    noches = validar_entero("Cantidad de noches: ")
    valor_noche = validar_entero("Valor por noche: ")

    total = noches * valor_noche
    categoria = calcular_categoria(total)

    reserva = {
        "Codigo": codigo,
        "Nombre": nombre,
        "Noches": noches,
        "Valor noche": valor_noche,
        "Total": total,
        "Categoria": categoria
    }

    reservas.append(reserva)

    print("Reserva registrada correctamente.")

# OPCIÓN 2

def buscar_reserva(reservas):

    codigo = input("Ingrese código: ")

    item = buscar_posicion(reservas, codigo)

    if item == -1:
        print("Reserva no encontrada.")
        return
    else:
        print("Item:", item)

        for clave, valor in reservas[item].items():
            print(clave, ":", valor)

# OPCIÓN 3

def actualizar_reserva(reservas):

    if len(reservas) == 0:
        print("No hay reservas registradas para actualizar.")
        return

    codigo=validar_texto("Ingrese el codigo a actualizar:\n")

    pos = buscar_posicion(reservas, codigo)

    if pos == -1:
        print("El codigo de la reservacion no existe.")
        return            
    
    #Actualizacion nombre reservante

    nuevo_nombre = validar_texto("Ingrese el nuevo nombre del reservador:\n").strip()

    reservas[pos]["Nombre"] = nuevo_nombre
  
    print(f"Nombre de reservador actualizado a {nuevo_nombre} exitosamente.")

    #Actualizacion valor por noche

    nueva_noches = validar_entero("Ingrese la cantidad de noches:\n")

    reservas[pos]["Noches"] = nueva_noches

    print(f"Cantidad de noches actualizada a: {nueva_noches}")

    #Actualizacion valor total de las noches

    nuevo_valor_noche = validar_entero("Ingrese el valor por noche:\n")

    reservas[pos]["Valor noche"] = nuevo_valor_noche

    print(f"Nuevo valor por noche actualizado a ${nuevo_valor_noche} correctamente.")
   

    total = nueva_noches * nuevo_valor_noche

    reservas[pos]["Total"] = total
    
    nueva_categoria = calcular_categoria(total)

    reservas[pos]["Categoria"] = nueva_categoria

# OPCIÓN 4

def eliminar_reserva(reservas):

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return

    codigo = validar_texto("Ingrese el codigo de la reserva que desea eliminar:\n").strip()

    pos = buscar_posicion(reservas, codigo)

    if pos == -1:
        print("Codigo de reserva no encontrado.")
        return

    del reservas[pos]
    print(f"Reserva {codigo} eliminada exitosamente.")
        

# OPCIÓN 5

def mostrar_reservas(reservas):

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return
    
    for reserva in reservas:
        print("----------------------")
        for clave, valor in reserva.items():
            print(clave,": ", valor)

# OPCIÓN 6

def mostrar_estadisticas(reservas):

    if len(reservas) == 0:
        print("No existen reservas.")
        return
    
    cantidad = len(reservas)

    ingresos = 0

    for reserva in reservas:
        ingresos += reserva["Total"]

    mayor = reservas[0]

    for reserva in reservas:
        if reserva["Total"] > mayor["Total"]:
            mayor = reserva

    promedio = ingresos / cantidad

    print("Cantidad de reservas: ", cantidad)
    print("Ingresos totales: $", ingresos)
    print("Reserva de mayor valor:")
    print("Código: ", mayor["Codigo"])
    print("Cliente: ", mayor["Nombre"])
    print("Total: $", mayor["Total"])
    print("Promedio por reserva: $", round(promedio))

#Menu Principal
def menu():
    opcion = 0
    while opcion != 7:
        print("\n===== HOTEL =====")
        print("1. Registrar reserva")
        print("2. Buscar reserva")
        print("3. Actualizar reserva")
        print("4. Eliminar reserva")
        print("5. Mostrar reservas")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione opción: "))

            if opcion == 1:
                registrar_reserva()

            elif opcion == 2:
                buscar_reserva(reservas)

            elif opcion == 3:
                actualizar_reserva(reservas)

            elif opcion == 4:
                eliminar_reserva(reservas)

            elif opcion == 5:
                mostrar_reservas(reservas)

            elif opcion == 6:
                mostrar_estadisticas(reservas)

            elif opcion == 7:
                print("Gracias por utilizar el sistema.")
                break

            else:
                print("Opción inválida.")

        except ValueError as e:
            print(F"Debe ingresar un número.", e)


#Programa Principal
def main():
    
    menu()
    


main()

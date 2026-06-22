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
        if reservas[i]["codigo"] == codigo:
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

    if buscar_posicion(codigo) != -1:
        print("Ese código ya existe.")
        return

    nombre = validar_texto("Nombre huésped:\n")
    noches = validar_entero("Cantidad de noches:\n")
    valor_noche = validar_entero("Valor por noche:\n")

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

def buscar_reserva():

    codigo = input("Ingrese código:\n ")

    item = buscar_posicion(codigo)

    if item == -1:
        print("Reserva no encontrada.")
        return
    else:
        print("Item:", item)

        for clave, valor in reservas[item].items():
            print(clave, ":", valor)

# OPCIÓN 3

#3. Actualizar Reserva

def actualizar_reserva(reservas):

    codigo=input("Ingrese el codigo a actualizar:\n")

    if not buscar_posicion(reservas, codigo):
        print("El codigo de la reservacion no existe.")
        return            
    
    print(f"Nombre de reservador actualizado a {nuevo_nombre} exitosamente.")

    nueva_noches = int(input("Ingrese la cantidad de noches:\n"))

    if not validar_entero(codigo):
        print("")

    print(f"Cantidad de noches actualizada a: {nueva_noches}")
    codigo["Noches"] = nueva_noches

    nuevo_valor_noche = int (input("Ingrese el valor por noche:\n"))

    if not validar_entero(codigo):
        print("")

    print(f"Nuevo valor por noche actualizado a ${nuevo_valor_noche} correctamente.")
    codigo["Valor noche"] = nuevo_valor_noche

    total = nueva_noches * nuevo_valor_noche

    codigo["Total"] = total
    
    nueva_categoria = calcular_categoria(total)

    codigo["Categoria"] = nueva_categoria

# OPCIÓN 4

def eliminar_reserva():

    codigo = input("Ingrese el codigo de la reserva que desea eliminar:\n").strip()

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return

    if buscar_posicion(reservas, codigo) is None:
        print("Codigo de reserva no encontrado.")
        return

    del reservas[codigo]
        

# OPCIÓN 5

def mostrar_reservas():

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return
    
    for reserva in reservas:
        print("----------------------")
        for clave, valor in reserva.items():
            print(clave,": ", valor)

# OPCIÓN 6

def mostrar_estadisticas():

    if len(reservas) == 0:
        print("No existen reservas.")
        return


#Menu Principal
def menu():
    print("""   Sistema de reservas de hotel    
          
          1. Registrar Reserva
          2. Buscar Reserva
          3. Actualizar Reserva
          4. Eliminar Reserva
          5. Mostrar Reservas
          6. Mostrar Estadisticas
          7. Salir
                    """)  

#Programa Principal
def main():
    
    cantidad = len(reservas)

    ingresos = 0

    for reserva in reservas:
        ingresos += reserva["Total"]

    mayor = reservas[0]

    for reserva in reservas:
        if reserva["Total"] > mayor["Total"]:
            mayor = reserva

    promedio = ingresos / cantidad

    print("Cantidad de reservas:", cantidad)
    print("Ingresos totales:", ingresos)
    print("Reserva de mayor valor:")
    print("Código:", mayor["Codigo"])
    print("Cliente:", mayor["Nombre"])
    print("Total:", mayor["Total"])
    print("Promedio por reserva: ", promedio)

# MENU

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
        opcion = int(input("Seleccione opción:\n"))

        if opcion == 1:
            registrar_reserva()

        elif opcion == 2:
            buscar_reserva()

        elif opcion == 3:
            actualizar_reserva()

        elif opcion == 4:
            eliminar_reserva()

        elif opcion == 5:
            mostrar_reservas()

        elif opcion == 6:
            mostrar_estadisticas()

        elif opcion == 7:
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida.")

    except ValueError as e:
        print(F"Debe ingresar un número.", e)
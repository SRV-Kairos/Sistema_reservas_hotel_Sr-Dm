# Lista donde se almacenarán las reservas
reservas = []

# FUNCIONES

def calcular_categoria(total):
    if total < 200000:
        return "Economica"
    elif total <= 500000:
        return "Estandar"
    else:
        return "Premium"

def buscar_posicion(codigo):
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

    nombre = validar_texto("Nombre huésped: ")
    noches = validar_entero("Cantidad de noches: ")
    valor_noche = validar_entero("Valor por noche: ")

    total = noches * valor_noche
    categoria = calcular_categoria(total)

    reserva = {
        "codigo": codigo,
        "nombre": nombre,
        "noches": noches,
        "valor_noche": valor_noche,
        "total": total,
        "categoria": categoria
    }

    reservas.append(reserva)

    print("Reserva registrada correctamente.")

# OPCIÓN 2

def buscar_reserva():

    codigo = input("Ingrese código: ")

    item = buscar_posicion(codigo)

    if item == -1:
        print("Reserva no encontrada.")
        return
    else:
        print("Item:", item)

        for clave, valor in reservas[item].items():
            print(clave, ":", valor)


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
        opcion = int(input("Seleccione opción: "))

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

    except:
        print("Debe ingresar un número.")
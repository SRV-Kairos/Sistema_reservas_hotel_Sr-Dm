#Validaciones

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

#1. Registrar Reserva
def registrar_reserva(reservas):
    print("\n===== REGISTRAR RESERVA =====\n")

    codigo=input("Ingrese el codigo de la reservacion a registrar:\n").strip()

    #Validar Codigo
    if not validacion_codigo(codigo):
        print("Error: El codigo no puede estar vacio.\n")
        return

#2. Buscar Reserva
def buscar_reserva(reservas):
    pass

#3. Actualizar Reserva
def actualizaar_reserva(reservas):

    codigo=input("Ingrese el codigo a actualizar:\n")

    if not buscar_posicion(codigo):
        print("El codigo de la reservacion no existe.")
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

def leer_opcion():
    try:
        opcion=int(input("Ingrese la opcion del menú a la que desea ingresar:\n"))

        if not 1 <= opcion <= 6:
            print("Opcion inexistente, ingrese nuevamente.")
            return
    except ValueError as e:
        print(f"Error: {e}")   


#Programa Principal
def main():
    
    import os
    import time
    reservas = []

    while True:
        menu()

        opcion = leer_opcion()

        if opcion == 1:
            pass

        if opcion == 2:
            pass

        if opcion == 3:
            pass

        if opcion == 4:
            pass

        if opcion == 5:
            pass

        if opcion == 6:
            pass

        if opcion == 7:
            print("Hasta luego.\nGracias por usar nuestro programa.")
            break

main()        
            
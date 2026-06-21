#Validaciones

def validacion_codigo(codigo):
    return codigo.strip() != ""

def validacion_nombre(nombre):
    return nombre.strip() != ""

def buscar_codigo(reservas):
    for codigo in reservas:
        if reservas["codigo"] == codigo:
            return codigo

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
    pass

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
    pass


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
            
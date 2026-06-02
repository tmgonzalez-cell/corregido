historico = 0
cupos = 75
opc = 0
while opc != 5:
    print("""¡Bienvenido al sistema de gestión de cupos del Gimnasio Titan!
      *** MENU PRINCIPAL ***
        1.- Cupos disponibles.
        2.- Realizar reserva.
        3.- Cancelar reserva.
        4.- Historial de reservas.
        5.- Salir""")
    opc = 0
    while opc < 1 or opc > 5:
        try:
            opc = int(input("Ingrese su opcion:  "))
            
            if opc < 1 or opc > 5:
                print("Error: Fuera de rango")
        except:
            print("Opcion debe ser un numero...")
    if opc == 1:
        if cupos != 0:
            print(f"la cantidad de cupos disponibles son: {cupos}")
        else:
            print("Ya no quedan cupos")
    elif opc == 2:
        res = 0
        while res <= 0:
            try:
                res = int(input("cuantos cupos desea reservar?:  "))
                if res < 0:
                    print("Error: Debe ser positivo")
                elif res > cupos:
                    print("reserva fuera de rango")
                elif cupos < res:
                    print("error fuera de rango")
            except:
                print("debe ser un numero")  
            if res <= 0 or res > 75:
                print("Error..")
            elif cupos <= 0:
                print("Error: no quedan cupos")
            elif cupos < res:
                print("Error..")
            elif res != 0:
                cupos -= res
                historico += res
            else:
                print("bye")
    elif opc == 3:
        can = 0
        while can <= 0:
            try:
                can = int(input("Cuantas reservas desea cancelar?:  "))
                if can < 0:
                    print("Error: Debe ser positivo")
                elif cupos > can:
                    print("reserva fuera de rango")
            except:
                print("debe ser un numero")  
            if can <= 0 or can > 75:
                print("Errorf..")
            elif cupos > can:
                print("se excedio el limite")
            elif can != 0:
                cupos += can
                historico -= can
            else:
                print("bye")
    elif opc == 4:
        print(f"el historico de ventas es: {historico}")
print("bye bye")

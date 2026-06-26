citas = []

def menu():

    try:

        print("--- Seguimiento de citas médicas ---")
        print("")

        print("1 - Agregar citas")
        print("2 - Buscar citas")
        print("3 - Eliminar citas")
        print("4 - Actualizar estado")
        print("5 - Mostrar registros")
        print("6 - Salir")
        opciones = int(input("Ingrese una opcion: "))

        if opciones < 1 or opciones > 6:

            print("¡Porfavor ingrese una opcion valida!")
            print("")
            return 0
        
        return opciones
    
    except ValueError:
        
        print("¡No se permiten letras!")
        print("")
        return 0

def opcion_1():
    
    print("--- Agregar citas ---")
    print("")

    while True:

        campo_paciente = input("Ingrese el nombre de la cita: ").strip().title()
        
        if campo_paciente == "":

            print("¡No puede estar vacio!")
            print("")
        
        else:

            break

    while True:
        
        try:

            campo_urgencia = int(input("Ingrese el nivel de urgencia (1-10): "))
            
            if campo_urgencia < 1 or campo_urgencia > 10:
                
                print("¡Sobrepasa los limites!")
                print("")

            else:

                break
        
        except ValueError:

            print("¡No se permiten letras!")
            print("")

    while True:

        try:

            campo_costo = float(input("Ingrese el costo de la cita: "))

            if campo_costo <= 0:

                print("¡Debe ser un numero mayor a cero!")
                print("")

            else:

                break
        
        except ValueError:

            print("¡No se permiten letras!")
            print("")

    campo_prioritaria = False

    diccionario_significado_citas = {

        "paciente": campo_paciente, # nombre
        "urgencia": campo_urgencia, # urgencia
        "costo": campo_costo,   # costo
        "prioritaria": campo_prioritaria,   # estado

    }
    
    citas.append(diccionario_significado_citas)

    print("")
    print("¡Perfecto!, cita añadida correctamente")
    print("")

def opcion_2():

    print("--- Buscar cita ---")
    print("")

    encontrado_buscar = False
    buscar_cita = input("Ingrese el nombre de la cita que desea buscar: ").strip().title()
    
    for citas_etc in citas:

        if citas_etc["paciente"] == buscar_cita:
            
            encontrado_buscar = True
            print("--- Cita encontrada ---")
            print("")

            posicion_indice = citas.index(citas_etc)

            print(f"{posicion_indice + 1} - Nombre: {citas_etc["paciente"]} | Urgencia: {citas_etc["urgencia"]} | Costo: {citas_etc["costo"]} | Estado: {citas_etc["prioritaria"]}")
            print("")
            break

    if not encontrado_buscar:

        print("¡La cita no fue encontrada!")
        print("")

def opcion_3():

    print("--- Eliminar cita ---")
    print("")

    encontrado_eliminar = False
    eliminar_cita = input("Ingrese el nombre de la cita que desea eliminar: ").strip().title()
    
    for citas_etc in citas:

        if citas_etc["paciente"] == eliminar_cita:
            
            encontrado_eliminar = True

            print("--- Cita encontrada ---")
            print("")

            si_o_no = input("¿Esta seguro que desea eliminar la cita? (S/N): ").strip().upper()

            if si_o_no == "S":

                print("¡Perfecto!, eliminando cita")
                citas.remove(citas_etc)

            else:

                print("Se ha cancelado la eliminacion...")
                print("")

    if not encontrado_eliminar:

        print("¡La cita no ha sido encontrada!")
        print("")

def opcion_4():

    print("--- Actualizar estado ---")
    print("")

    for citas_etc in citas:
        
        if citas_etc["urgencia"] >= 8:

            citas_etc["prioritaria"] = True # prioritaria

        else:

            citas_etc["prioritaria"] = False # regular

    print("--- Se ha actualizado exitosamente ---")
    print("")

def opcion_5():

    if len(citas) <= 0:

        print("")
        print("¡No hay citas registradas!")
        print("")

    else:

        print("--- Mostrar registros ---")
        print("")

        for indice , citas_etc in enumerate(citas):

            if citas_etc["prioritaria"] == True: # Primero va la variable creada, con la lista y si es verdadero

                estado_final = "Cita prioritaria" #This

            else: # Si es falso
                
                estado_final = "Cita regular"

            print(f"{indice + 1 } - Nombre: {citas_etc["paciente"]} | Urgencia: {citas_etc["urgencia"]} | Costo: {citas_etc["costo"]} | Estado: {estado_final}")
            print("")
            
while True:

    muestra_esto = menu()

    if muestra_esto == 1:

        opcion_1()

    elif muestra_esto == 2:

        opcion_2()

    elif muestra_esto == 3:

        opcion_3()

    elif muestra_esto == 4:

        opcion_4()

    elif muestra_esto == 5:

        opcion_5()

    elif muestra_esto == 6:

        print("")
        print("--- Saliendo del programa, Gracias por utilizar el software ---")
        print("")
        break
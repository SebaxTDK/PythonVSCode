cursos = []

def menu():

    try:

        print("--- Administración de cursos cortos ---")
        print("")

        print("1 - Agregar cursos")
        print("2 - Buscar cursos")
        print("3 - Eliminar cursos")
        print("4 - Actualizar estado")
        print("5 - Mostrar registros")
        print("6 - Salir")
        opciones = int(input("Ingrese una opcion: "))
        
        if opciones < 1 or opciones > 6:

            print("Porfavor ingrese una opcion valida")
            return 0

        return opciones
    
    except ValueError:

        print("¡No se permiten letras!")
        print("")
        return 0

def opcion_1():

    print("")
    print("--- Agregar cursos ---")
    print("")

    while True:

        nombre = input("Ingrese el nombre del curso: ").strip().title()

        if nombre == "":

            print("¡El nombre no puede estar vacio")
            print("")

        else:

            break

    while True:

        try:

            cupos = int(input("Ingrese la cantidad de cupos (0-40): "))

            if cupos < 0 or cupos > 40:

                print("¡Sobrepasa la cantidad!")
                print("")
            
            else:

                break
        
        except ValueError:

            print("¡No se permiten letras!")
            print("")

    while True:

        try:

            duracion_horas = float(input("Ingrese la duracion en horas: "))
            
            if duracion_horas <= 0:

                print("¡El numero tiene que ser mayor a 0!")
                print("")

            else:

                break
        
        except ValueError:

            print("¡No se permiten letras!")
            print("")

    abierto = False

    diccionario_significado_cupos = {

        "nombre": nombre,
        "cupos": cupos,
        "duracion": duracion_horas,
        "abierto": abierto

    }

    cursos.append(diccionario_significado_cupos)

    print("")
    print("¡Perfecto!, curso registrado correctamente")
    print("")

def opcion_2():

    print("--- Buscar cursos ---")
    print("")
    
    encontrado_buscar = False
    buscar_curso = input("Ingrese el nombre del curso que desea buscar: ").strip().title()
    
    for cursos_etc in cursos:

        if cursos_etc["nombre"] == buscar_curso:

            print("--- Curso encontrado ---")
            print("")
            
            posicion_indice = cursos.index(cursos_etc)
            print(f"{posicion_indice + 1} - Nombre: {cursos_etc["nombre"]} | Cupos: {cursos_etc["cupos"]} | Duracion: {cursos_etc["duracion"]} | Estado: {cursos_etc["abierto"]}")
            print("")
            encontrado_buscar = True

    if not encontrado_buscar:

        print("¡El curso no ha sido encontrado!")
        print("")

def opcion_3():

    print("")
    print("--- Eliminar cursos ---")
    print("")

    encontrado_eliminar = False
    eliminar_curso = input("Ingrese el nombre del curso que desea eliminar: ").strip().title()
    
    for cursos_etc in cursos:

        if cursos_etc["nombre"] == eliminar_curso:
            
            encontrado_eliminar = True
            print("--- Curso encontrado ---")
            print("")

            si_o_no = input("¿Esta seguro que desea eliminar este curso? (S/N): ").strip().upper()
            
            if si_o_no == "S":

                print("¡Perfecto!, curso eliminado correctamente")
                print("")
                cursos.remove(cursos_etc)
                break
            
            else:

                print("Se ha cancelado la eliminacion...")
                print("")

    if not encontrado_eliminar:

        print("¡El curso no ha sido encontrado!")
        print("")

def opcion_4():

    print("--- Actualizar estado ---")
    print("")

    for cursos_etc in cursos:
        
        if cursos_etc["cupos"] >= 1:

            cursos_etc["abierto"] = True

        else:

            cursos_etc["abierto"] = False

    print("--- Estado actualizado correctamente ---")
    print("")

def opcion_5():

    if len(cursos) <= 0:

        print("")
        print("--- No hay registros para mostrar ---")
        print("")

    else:

       
        print("--- Mostrar registros ---")
        print("")

        for indice , cursos_etc in enumerate(cursos):

            if cursos_etc["abierto"] == True:

                estado_final = "Cupo abierto"

            else:

                estado_final = "Cupo cerrado"

            print(f"{indice + 1 } - Nombre: {cursos_etc["nombre"]} | Cupos: {cursos_etc["cupos"]} | Duracion: {cursos_etc["duracion"]} | Estado: {estado_final}")
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
        print("--- Saliendo del programa ---")
        print("Gracias por usar nuestro software...")
        print("")

        break
    
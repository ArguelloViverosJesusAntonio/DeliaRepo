print ("Programa que hace la funcion de un menu basico de deportes y sus caracteristicas")
print ("Hecho por Arguello Viveros Jesus Antonio y Corona Aguilera Joshua Amaitzin")
contraseña = "coronaarguello"

intentos = 3
while intentos > 0:
    entrada = input("Introduce la contraseña: ")
    if entrada == contraseña:
        print("Contraseña correcta. Accediendo al sistema...\n")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Has superado el número de intentos permitidos. Cerrando el programa.")
else:
    deportes = []

    while True:
        print("\nMenú:")
        print("1. Agregar/Insertar/Alta de deporte")
        print("2. Consulta/Mostrar deportes")
        print("3. Modificar/Editar deporte")
        print("4. Eliminar/Borrar deporte")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            nombre = input("Introduce el nombre del deporte: ")
            jugadores = input("Introduce el número de jugadores: ")
            duracion = input("Introduce la duración del partido (en minutos): ")
            equipo_necesario = input("Introduce el equipo necesario: ")
            superficie = input("Introduce el tipo de superficie (césped, pista, etc.): ")
            popularidad = input("Introduce la popularidad (baja, media, alta): ")
            origen = input("Introduce el origen del deporte: ")
            contacto = input("Introduce el contacto fisico entre jugadores: ")
            año_creacion = input("Introduce el año de creación del deporte: ")
            competencias = input("Introduce algunas competencias famosas del deporte: ")

            deporte = {
                "nombre": nombre,
                "jugadores": jugadores,
                "duracion": duracion,
                "equipo_necesario": equipo_necesario,
                "superficie": superficie,
                "popularidad": popularidad,
                "origen": origen,
                "contacto": contacto,
                "año_creacion": año_creacion,
                "competencias": competencias
            }
            deportes.append(deporte)
            print("Deporte agregado exitosamente.")

        elif opcion == "2":
            if deportes:
                print("\nLista de deportes:")
                for i, deporte in enumerate(deportes, start=1):
                    print(f"{i}. Nombre: {deporte['nombre']}, Jugadores: {deporte['jugadores']}, "
                          f"Duración: {deporte['duracion']} minutos, Equipo necesario: {deporte['equipo_necesario']}, "
                          f"Superficie: {deporte['superficie']}, Popularidad: {deporte['popularidad']}, "
                          f"Origen: {deporte['origen']}, Contacto: {deporte['contacto']}, "
                          f"Año de creación: {deporte['año_creacion']}, Competencias famosas: {deporte['competencias']}")
            else:
                print("No hay deportes registrados.")

        elif opcion == "3":
            if deportes:
                consulta = int(input("Introduce el número del deporte a modificar: ")) - 1
                if 0 <= consulta < len(deportes):
                    print("\nModificando el deporte seleccionado...")
                    deportes[consulta]['nombre'] = input("Introduce el nuevo nombre del deporte: ")
                    deportes[consulta]['jugadores'] = input("Introduce el nuevo número de jugadores: ")
                    deportes[consulta]['duracion'] = input("Introduce la nueva duración del partido (en minutos): ")
                    deportes[consulta]['equipo_necesario'] = input("Introduce el nuevo equipo necesario: ")
                    deportes[consulta]['superficie'] = input("Introduce el nuevo tipo de superficie: ")
                    deportes[consulta]['popularidad'] = input("Introduce la nueva popularidad (baja, media, alta): ")
                    deportes[consulta]['origen'] = input("Introduce el nuevo origen del deporte: ")
                    deportes[consulta]['contacto'] = input("Introduce cuanto contacto tienen los jugadores: ")
                    deportes[consulta]['año_creacion'] = input("Introduce el nuevo año de creación: ")
                    deportes[consulta]['competencias'] = input("Introduce las nuevas competencias famosas: ")
                    print("Deporte modificado exitosamente.")
                else:
                    print("Deporte no encontrado.")
            else:
                print("No hay deportes para modificar.")

        elif opcion == "4":
            if deportes:
                consulta = int(input("Introduce el número del deporte a eliminar: ")) - 1
                if 0 <= consulta < len(deportes):
                    del deportes[consulta]
                    print("Deporte eliminado exitosamente.")
                else:
                    print("Deporte no encontrado.")
            else:
                print("No hay deportes para eliminar.")

        elif opcion == "5":
            # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")

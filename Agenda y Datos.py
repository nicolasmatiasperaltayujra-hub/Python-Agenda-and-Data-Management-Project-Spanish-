agenda = []

while True:
    print("\n ===Agenda/Datos===")
    print("1. Mostrar Tarea")
    print("2. Agregar Tarea")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        for tarea in agenda:
            print("Titulo de la Agenda: ", tarea["titulo"])
            print("Prioridad de la Agenda: ", tarea["prioridad"])
    elif opcion == "2":
        titulotitulo = input("Ingrese el Titulo de la Agenda: ")
        prioridad = input("Ingrese la Prioridad de la Agenda (Alta/Media/Baja): ")
        entrada = {
            "titulo": titulotitulo,
            "prioridad": prioridad
        }
        agenda.append(entrada)
    elif opcion == "3":
        print("Saliendo del programa...")
        break

for tarea in agenda:
    print("Titulo de la Agenda: ", tarea["titulo"])
    print("Prioridad de la Agenda: ", tarea["prioridad"])
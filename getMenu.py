def menu():
    print("*****************************************")
    print("********* Gestió d'alumnes **************")
    print("*****************************************")

    oper = int(input("Tria una de les següents opcions:\n"
                     "1. Introduir alumnes\n"
                     "2. Mostrar alumnes\n"
                     "3. Analitzar registres\n"))
    while oper<1 or oper>3:
        oper = int(input("Tria una de les següents opcions (del 1 al 3): "
                         "1. Introduir alumnes"
                         "2. Mostrar alumnes"
                         "3. Analitzar registres"))
    return oper
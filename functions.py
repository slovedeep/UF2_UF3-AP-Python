import pandas as pd
import csv

def get_data():

    setHeader=0

    number = int(input("Indica el nombre d'alumnes que vols introduir: "))

    for i in range(number):
        student_ID = int(input("Introdueix l'identificador: "))
        first_name = input("Introdueix el nom de l'estudiant: ")
        last_name = input("Introdueix el cognom de l'estudiant: ")
        subject = input("Introdueix l'assignatura: ")
        grade = int(input("Introdueix la nota: "))

        student = {
            "student_ID": student_ID,
            "first_name": first_name,
            "last_name": last_name,
            "subject": subject,
            "grade": grade
        }

        fieldnames = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']

        with open('files/alumnes.csv', 'a', encoding='utf=8', newline='') as file:
            writeCSV = csv.DictWriter(file, fieldnames=fieldnames)
            if setHeader==0:
                writeCSV.writeheader()
                setHeader+=1
            writeCSV.writerow(student)
        file.close()

def show_std():
    try:
        show = pd.read_csv('files/alumnes.csv')
        print(show)
    except FileNotFoundError:
        print("No s'ha trobat el fitxer")

def analyze_records():
    n= int(input("Quants registres vol consultar?"))
    print("El total de registres")
    show = pd.read_csv('files/alumnes.csv')
    print(show)
    print("Els primers ",n," registres són:")
    print((show.head(n)))
    print("Els ultims ", n, " registres són:")
    print((show.tail(n)))
#Mini-proyecto: "Agenda de Contactos"
#Descripción:
#Crea una pequeña agenda que permita:
#Agregar un nuevo contacto (nombre y número de teléfono).
#Buscar un contacto por su nombre.
#Mostrar todos los contactos.
#Eliminar un contacto.
#Requisitos:
#Usar un diccionario donde el nombre sea la clave y el número sea el valor..
#Crear un pequeño menú en consola para elegir las acciones.

contactsList = []
contactos = {}

def createContacts ():
    while True:
        name = input("Ingresar el nombre del contacto: ")
        tel = input("Ingresar el numero del contacto: ")

        contactos = {name:tel}
        contactsList.append(contactos)
        print("Contacto agregado")
        b = input("¿Quieres agregar otro? \n Pulse cualquier tecla para continuar, n para salir")
        if b == "n" or b =="N":
            break

def searchContact(contactos):
    contact = input("Ingresa el nombre del contacto a buscar: ")
    if contact in contactos:
        value = contactos[contact]
        print(f"El número de {contact} es: {value}")
    else:
        print("Contacto ingresado No concontrado")


def deleteContact(contactos):
    contact = input("Ingresa el nombre del contacto a eliminar: ")
    if contact in contactos:
        del contactos[contact]
        print(contactos)



def showContacts():
    print(contactsList)

def menu():
    b = input("Bienvenido a tu agenda de datos: \n"
    "Ingresa 1 para agregar un contacto:  \n" 
    "Ingresa 2 para buscar un contacto por nombre: \n" 
    "Ingresa 3 para mostrar todos los contactos: \n" 
    "Ingresa 4 para eliminar un contacto: \n"
    "Ingresa 5 para salir: \n")
    match b:
        case "1":
            createContacts()
            menu() 
        case "2":
            searchContact(contactos)
            menu()
        case "3":
            showContacts()
            menu()
        case "4":
            deleteContact(contactos)
            menu()
        case "5":
            exit()

menu()


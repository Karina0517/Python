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

contactos = {"Policia" : "123",
             "Bomberos" : "456",
             "Mamá" : "3196164048",
             "Riwi" : "1035975643"}

def updateContacts (contactos):
    name = input("Ingresar el nombre del contacto: ")
    tel = input("Ingresar el numero del contacto: ")

    contactos[name] = tel
    print("Contacto agregado")
                    

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
    print(contactos)

def menu():
    b = input("Bienvenido a tu agenda de datos: \n"
    "Ingresa 1 para agregar un contacto:  \n" 
    "Ingresa 2 para buscar un contacto por nombre: \n" 
    "Ingresa 3 para mostrar todos los contactos: \n" 
    "Ingresa 4 para eliminar un contacto: \n"
    "Ingresa 5 para salir: \n")
    match b:
        case "1":
            updateContacts(contactos)
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

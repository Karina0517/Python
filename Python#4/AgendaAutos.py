#Diccionarios al fin de cada valor se tiene que poner , para diferenciar cada clave-valor

person = {
    "name" : "Karina",
    "lastname" : "Henao",
    "age" : 10,
    "id" : 103592,
}

House = {
    "Adress" : "calle 45b",
    "value" : 1000000000,
    "owner" : "Karina",

}

del person["age"]
person["other"] = "Mariana" #AGregar claves y valores
print(person)
for dat,prueba in person.items():
    print(f"{dat}: {prueba}")






fruits = ["naranja", "naranja", "naranja","limon","mango","borojo"]
contFruits = {}

for fru in fruits:
    if fru in contFruits:
        contFruits[fru] += 1
    else:
        contFruits[fru] = 1

print(contFruits)






paises = {
    "Colombia": "Bogotá",
    "Suecia": "Estocolmo",
    "Argentina": "Buenos Aires",
    "Venezuela": "Caracas"
}

pais = input("Escribe un país: ")
if pais in paises:
    print(f"La capital de {pais} es: {paises[pais]}")
else:
    print("País no encontrado")

invertCountry = {capital: pais for pais, capital in paises.items()}
print(invertCountry)
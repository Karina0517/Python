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
auto = {
    "marca": "Toyota",
    "modelo": "txl",
    "año": 2026
}

auto["modelo"] = "fortuner"
auto["color"] = "Blanco"
del auto["año"]

for ky in auto.keys():
    print(ky)

for keys in auto.values():
    print(keys)
contraseña_correcta = "Karina"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    contraseña = input("Ingresa la contraseña: ")
    
    if contraseña == contraseña_correcta:
        print("Bienvenida Karina")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos} de {max_intentos}.")
        
if intentos == max_intentos:
    print("Tú no eres Karina, has alcanzado el número máximo de intentos.")

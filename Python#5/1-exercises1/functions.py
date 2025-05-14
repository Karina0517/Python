from datetime import date

# 1. 💰 Calculadora de propina  
def calculate_tip(value,percent):
    total = value * (percent/100)
    return total

tip = calculate_tip(100,15)
print (tip)
  

# 2. 📏 Conversor de unidades  
def meters_to_kilometers(meters):
    km = meters/1000
    return km
kilometers = meters_to_kilometers(2000)
print(kilometers)
    

# 3. ✉️ Generador de email empresarial 
def create_email(n1,n2,n3):
    email = (n1 + "." + n2 + "@" + n3)
    return email.lower()
em = create_email("Lucia","Gomez","empresa.com")
print (em)
# 4. 🧾 Precio con impuestos  
def final_price(price, iva = 0.21):
     total = (price * iva) + price
     print (total)
     return total
final_price(1200000)
     

# 5. 🔐 Simulador de login  
def validate_login(user,password):
    userName = "admin"
    passwordUser = "1234"
    if user == userName and password == passwordUser:
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Credenciales incorrectas")
        return False
validate_login("admin","1234")   

# 6. 🧑‍💻 Generador de nombre de usuario
def generate_username(name, year):
    name = name.lower()
    year = str(year)[2:]
    username = name + year
    return username
print('\n6. Nombre de usuario', generate_username('Lucas', 1997))

# 7. ✨ Formateador de nombres  
def format_name(name):
    return name.title()
    print(name.title())

# 8. 🎂 Calculadora de edad  
def calculate_age(year):
    age = 2025 - int(year)
    return age

# 9. 📞 Validación de número telefónico  
def validate_phone(number):
    return isinstance(number, int) and len(str(number)) == 10

# 10. 🧠 Notas de estudiantes  
def student_average(name, *grades):
    if grades:
        average = sum(grades) / len(grades)
        print(f"{name}: Promedio = {average:.2f}")
    else:
        print(f"{name}: Sin notas registradas")
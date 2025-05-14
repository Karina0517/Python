import string
import random

# 1. Shopping cart simulator
def test_calculate_cart_total(dic, iva= 0.21):
    subT = 0
    for i in dic:
        priceP = i['price']
        qnt = i['quantity']
        subT += priceP * qnt
    total = subT *(1 + iva)
    return round(total,2)

cart = [
        {"name": "Shirt", "price": 20.0, "quantity": 2},
        {"name": "Pants", "price": 40.0, "quantity": 1}
    ]
print(test_calculate_cart_total(cart,0.21))

# 2. Text processing (word count)

# 3. Secure password generator

    
        



def analyze_temperatures(tempt):
    acum = 0
    l = len(tempt)
    for i in tempt:
        acum += i 
        
    mini = min(tempt) 
    maxi = max(tempt)  
    average = acum/l
    return average, maxi, mini
    
temps = [20, 25, 22, 18, 30]
average, maxi, mini = analyze_temperatures(temps)
print(average, maxi, mini)
# 5. Functional contact book



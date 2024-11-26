import random

numero = random.randint(1,10)
print(numero)
num1 = int(input("Inserisci un numero: "))
num2 = random.randint(1,100)

print(num1)
print(num2)

if num1 < num2:
    print("numero 1 maggiore")
else:
    print("numero 2 maggiore")
    

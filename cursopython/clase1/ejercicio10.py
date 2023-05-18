
numeros = [3,5,2,8,1,9,4,2,2,7,4,9,10]
pares = []
impares = []
#mostrar los numeros pares de la lista 

for numero in numeros:
    if (numero % 2 == 0):

        pares.append (numero)
    else:
        impares.append(numero)

print(pares)
print(impares)
print(f"en la lista hay : {len(pares)} pares y {len(impares)} impares ")
p = len(pares)
i = len(impares)
x = p - i 
if(x == 0 ):
    rta ="son iguales"
elif(x > 0):
    rta = "pares es mayor"
else:
    rta ="impares es menor"
    
    
print(rta)


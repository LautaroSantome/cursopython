i = 0 
mayor = None

while i < 5:
      numero = int(input("ingrese un numero:"))
      
      if i == 0 or numero > mayor:
           mayor = numero 
      
i += 1
print(f"el mayor numero es {mayor}")


nota = int(input("ingrese una nota 0 - 10: "))

while nota < 0 or nota > 10 : 
    nota = int(input("nota invalida, reingrese nota: "))

print(f"la nota es:  {nota}" )
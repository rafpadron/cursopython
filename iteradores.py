# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)
    
print("-----------------------------------------")
# Crear un iterador para los numeros pares

#Crear iterador
par_itter = iter(range(0,limit+1,2))

#Usar el iterador
for num in par_itter:
    print(num)
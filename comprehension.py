""" list = [1,2,3,4,5]
newlist = [l*2 for l in list]
print(newlist) """

""" list = ["sol", "mar", "montaña", "rio", "estrella"]
newlist = [tresletras.upper() for tresletras in list if len(tresletras) <= 3]
print(newlist) """

""" claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

dict = {claves[i]: valores[i] for i in range(len(claves))}
print(dict) """

""" matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

newmatriz = [[row[i] for row in matriz]for i in range(len(matriz[0]))]
print(newmatriz) """

""" personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

listmadrid = [persona["nombre"] for persona in personas if persona["ciudad"]=="Madrid" and persona["edad"]>30]
print(listmadrid) """

""" numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [num*2 if num % 2 == 0 else num for num in numlist ]
print(list) """
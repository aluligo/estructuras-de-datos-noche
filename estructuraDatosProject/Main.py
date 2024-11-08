#Ejemplo con Tuplas
from operator import truediv

tupla1 = {} # tupla vacia
print(tupla1)

tupla2 = ("apple",2018,"samsung",4,9,"t",True)#Tupla heterogenea
print(tupla2)
print(tupla2[1])
print(tupla2[3])

#operaciones con Tuplas
tuplas3 = ("A","B","C","D")
tupla4 = (1,2,3,4)

#concatenar tuplas
tupla5 = tuplas3 + tupla4
print(tupla5)

#Repetir tuplas
tupla6 = tupla5 * 3
print(tupla6)

#Tupla enlazada
tupla7 = (0,1,2,3)
tupla8 = ("A","B","C")
tupla9 = (tupla7,tupla8)
print(tupla9)
print(tupla9[1])#sacar una tupla enlazada
print(tupla9[1][1])#sacar un elemento de una tupla enlazada

#comparar tuplas
tupla10 = ("Rojas")
tupla11 = (1,2,3)
tuplas12 = ("Rosas")
tuplas13 = ("rosas")
print(tupla10 < tuplas12)

##########################################




#Ejemplo con Listas
lista = [] # lista vacia
lista1 = [1,"Hola",4.5,"8"] #lista con 4 elementos heterogenea
print(lista1)
print(lista1[1])
print(lista1[1][2])#elemento dentro del indice 1

#listas enlazadas
lista2 = [0,1,2,3]
lista3 = ["A","B","C"]
lista4 = [lista2,lista3]
print(lista4)
print(lista4[1])#sacar una lista enlazada
print(lista4[1][2])#sacar un elemento de una lista enlazada

#operaciones con Listas
lista5 = ["A","B","C"]
lista6 = [1,2,3,4]
lista7 = lista5 + lista6
print(lista7)

#Repetir Listas
lista8 = [1,2,3,4,5]
lista9 = lista8 * 4
print(lista9)

#comparar listas
lista10 = ["Juan"]
lista11 = ["Juan "]
print(lista10 == lista11)

#Determinar si un elemento se encuentra dentro de una lista
lista12 = ["cien","años","de","soledad"]
if "de" in lista12:
    print("si se encuentra en la lista")
else:
    print("no se encuentra en la lista")

#iterando en una lista
lista13 = ["Hola","estudiantes","programacion","FUP"]
for palabra in lista13:
    print(palabra, end = ",")


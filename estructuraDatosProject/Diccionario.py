#ejemplo con Diccionarios
diccionario = {} # diccionario vacio
puertos = {
    22:"ssh",
    23:"Telnet",
    80:"http",
    3306:"mysql",
    1526:"Oracle"
}
print(puertos)
print(puertos[80]) #sacar un valor del diccionario
puertos1 = {
    22:"ssh",
    80:"http",
}
puertos2 = {
    53:"DNS",
    443:"https"
}
print(puertos1)
puertos1.update(puertos2)#Actualizar el Diccionario
print(puertos1)

#Eliminar un elemento de un diccionario
calificaciones = {

    "alumno1":5,
    "alumno2":4,
    "alumno3":3,
    "alumno4":2,
}
print(calificaciones)
del calificaciones["alumno3"] #eliminar una pareja del diccionario
print(calificaciones)

#iteraccion con diccionarios
dicPuertos = {
    22:"ssh",
    23:"Telnet",
    80:"http",

}
for clave,valor in dicPuertos.items():#se puede colocar x,y
    print(clave,"->",valor)
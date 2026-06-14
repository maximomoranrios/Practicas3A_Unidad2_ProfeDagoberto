"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")

print("\033c")

set1={"Python","SQL","Estructurado","SQL"}
print(set1)

for i in set1:
  print(i)

  
set2={"Hola",True,33,3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={""}
print(set3)

set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)
print(set3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)

lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=list(conjunto)
print(lista)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
list_emails=[]
opc="S"
while opc=="S":
  list_emails.append(input("Ingrese email: " ).lower().strip())
  opc=input("¿Desea añadir otro (S/N)? ").upper().strip()
# print(list_emails)
set_emails=set(list_emails)
list_emails=list(set_emails)
print(list_emails)
# Solucion 2 pero manda los objetos al inicio
list_emails=[]
opc=True
while opc:
  list_emails.insert(0,input("Ingrese email: " ).lower().strip())
  opc=input("¿Desea añadir otro (S/N)? ").upper().strip()
  if opc=="N":
    opc=False
set_emails=set(list_emails)
list_emails=list(set_emails)
print(list_emails)

# append los manda al ultimo
# insert(posicion) al inicio
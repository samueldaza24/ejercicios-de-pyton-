nombre1=input("ingrese el nombre de la primera persona")
edad1=int(input("ingrese la edad de la primera persona"))
nombre2=input("ingrese el nombre de la segunda persona")
edad2=int(input("ingrese la edad de la primera persona"))

if edad1<0 or edad1>120 and edad2<0 or edad2>120:
              print("edad invalida")
elif edad1>edad2:
    print(nombre1,"es mayor que",nombre2)
elif edad2>edad1:
    print(nombre2<"es mayor que", nombre2)
else:
    print(nombre1, "y" ,nombre2,"tienen la misma edad")

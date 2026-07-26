nombre= input("ingrese su nombre")
numero1=int(input("ingrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))
if numero1<0 and numero2>100:
    print("numero invalido")
elif numero1>numero2:
    print(" el primer numero es mayor")
elif numero2>numero1:
    print(" el segundo numero es mayor")
elif numero1==numero2:
    print(" los dos numeros son iguales")
else:
    print(" numero valido")

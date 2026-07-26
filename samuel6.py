nombre=input("ingrese su nombre")
edad=float(input("ingrese su edad"))
if edad>0 and edad<=5:
    print(" es un nino pequeno")
elif edad>6 and edad<=12:
    print(" es un nino")
elif edad>13 and edad<=17:
    print(" es un adolescente")
elif edad>18:
    print(" es un adulto")
else:
    print("edad no valida")

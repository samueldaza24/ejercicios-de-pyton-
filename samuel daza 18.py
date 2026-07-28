saldo=500000
opcion=0
while opcion!=4:
    print(" bienvenido al cajero daza")
    print(" 1 consultar saldo")
    print(" 2 retirar dinero")
    print("  3 depositar dinero")
    print("  4 salir")
    opcion=int(input("eliga la opcion que desea"))
    if opcion==1:
        print(" su saldo es:", saldo)
    elif opcion==2:
        monto=float(input("ingrese el monto para pagar"))
        if monto>0 and monto<=saldo:
            saldo=saldo-monto
            print("su nuevo saldo es:", saldo)
        else:
            print("error su saldo es insuficiente")
    elif opcion==3:
            consigna=float(input("ingrese su monto a consignar"))
            if consigna>0:
                saldo=saldo+consigna
                print(" consigna exitosa")
                print(" su nuevo saldo es:", saldo)
            else:
                print(" error, el monto de la consigna debe ser mayor a cero")
    elif opcion==4:
        print(" gracias por estar en el cajero daza")
    else:
        print("error, intente ingresar nuevamente al cajero")
        
      
    
    

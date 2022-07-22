# convertir decimal a hexadecimal y viceversa

# recibir variables que contienen
# decimales iguales o menores a 2^31 
# la linea que contiene un numero decimal negativo termina la ejecucion
# S={0,1,2,3,4,5,6,7,8,9,{mathrm  {A}},{mathrm  {B}},{mathrm  {C}},{mathrm  {D}},{mathrm  {E}},{mathrm  {F}}},

def dechexadec():
    decimal = (input("Ingrese un numero decimal: "))
    hexa = (input("Ingrese un numero hexadecimal: "))

    if decimal.isdigit():
        decimal = int(decimal)
        if (decimal >= 0 and decimal <= pow(2, 31)):
            print("El numero decimal en hexadecimal es: ", hex(decimal))
    elif hexa is not None and hexa != "":
        print("El numero hexadecimal en decimal es: ", int(hexa, 16))
        return
    else:
        print("Numero decimal o hexadecimal no valido")
        return
dechexadec()

# convertir decimal a hexadecimal y viceversa

# recibir variables que contienen
# decimales iguales o menores a 2^31 
# la linea que contiene un numero decimal negativo termina la ejecucion
# S={0,1,2,3,4,5,6,7,8,9,{mathrm  {A}},{mathrm  {B}},{mathrm  {C}},{mathrm  {D}},{mathrm  {E}},{mathrm  {F}}}
# TODO: VALIDAR QUE EL HEXADECIMAL NO SEA VALIDO EN DIFERENTES CARACTERES  hexa is not None and

def dechex(decimal):
    if decimal.isdigit():
        decimal = int(decimal)
        if (decimal >= 0 and decimal <= pow(2, 31)):
            print("El numero decimal en hexadecimal es: ", hex(decimal))
        else:
            print("El numero decimal es mayor a 2^31")
    elif decimal == '':
        return
    else:
        print("Numero decimal no valido")

def hexdec(hexa):
    if hexa.isalpha():
        print("El 'hexadecimal' es una cadena de valores")
        return
    if hexa.isalnum() and int(hexa >= 0 and hexa <= pow(2, 31), 16):
        print("El numero hexadecimal en decimal es: ", int(hexa, 16))
    elif hexa == '':
        return
    else:
        print("Numero hexadecimal no valido")

def dechexadec():
    decimal = (input("Ingrese un numero decimal: "))
    hexa = (input("Ingrese un numero hexadecimal: "))
   
    if decimal != '' or  hexa != '': 
        dechex(decimal)
        hexdec(hexa)
    else: print("Numero hexadecimal o decimal no validos")

dechexadec()




        # if hexa.isdigit():
        #     print( "El numero hexadecimal es digito")
        # elif hexa.isalpha():
        #     print("El numero hexadecimal es alpha")
        # elif hexa.isalnum():
        #     print("El numero hexadecimal es alphanumero")
        # else:
        #     return "ninguno"
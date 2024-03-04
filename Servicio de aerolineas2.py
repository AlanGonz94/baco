"""
Crear un servicio para una aereolinea que permita realizar las siguientes acciones.

- Reservar un asiento en un vuelo con (7 filas*2columnas por fila*3asientos por fila) 

- Si el asiento esta libre puede ocuparlo
- Es necesario guardar el pasaporte y el nombre del usuario
- Indicar cuantos asientos vacíos quedan
- Indicar si un asiento esta ocupado y proponer el siguiente vacío
- Imprimir de alguna forma entendible la distribución de asientos mostrando con un O los libres y con una X los ocupados
"""

Contador = 0
Asientos = [["O","O","O","O","O","O"], 
            ["O","O","O","O","O","O"], 
            ["O","O","O","O","O","O"], 
            ["O","O","O","O","O","O"], 
            ["O","O","O","O","O","O"], 
            ["O","O","O","O","O","O"], 
            ["O","O","O","O","O","O"]]

for fila in Asientos:
    for lugar in fila:        
        if lugar == "O":
            Contador = Contador + 1

print (("Hay ") + (str(Contador)) + (" asientos vacios")) #esto dira cuantos elementos de un tipo hay en general, osea espacios vacios o ocupados
for fila in Asientos:
    for lugar in fila:
        print(lugar, end=" ")  #esto mostraria solo las letras de la matriz
    print ()

#Esta variable determinara si se apaga o sigue el programa
Fin = False

Clientes_info = [["O","O","O","O","O","O"], 
                ["O","O","O","O","O","O"], 
                ["O","O","O","O","O","O"], 
                ["O","O","O","O","O","O"], 
                ["O","O","O","O","O","O"], 
                ["O","O","O","O","O","O"], 
                ["O","O","O","O","O","O"]]



#Si fin es falso sigue prendido, si fin es verdadero, se termina
while Fin == False:
    print ("                        Bienvenido a la compra de boletos para el avion de Alan")
    Habran_mas_clientes = input ("Seguiremos vendiendo asientos? Si, No?     ")
    if Habran_mas_clientes == "Si" or Habran_mas_clientes == "SI" or Habran_mas_clientes == "si" or Habran_mas_clientes == "sI":

        Usuario = input("Ingrese su nombre:    ")
        Pasaporte = input("Ingrese su pasaporte:    ")

        print ("                             recordar que comienza desde el 0, restar 1 numero a lo que diras")
        print ()
        print ("Le ofrecemos los asientos marcados con O, los que tienen X ya estan ocupados")
        print ()
        #Mostrar disponibilidad de asientos
        for fila in Asientos:
            for lugar in fila:
                print(lugar, end=" ")  #esto mostraria solo las letras de la matriz, cuales son O y cuales X
            print ()

        #aqui preguntamos coordenadas x/y para guardar un asiento
        venta_de_lugarx = int(input("En que fila de asientos se quiere sentar?  "))
        venta_de_lugary = int(input("En que asiento se quiere sentar?  "))

        asiento_duplicado = False #esto se activara cuando se detecte que alguien pida un asiento que ya diga X, 
                                    #y no se desactivara hasta que agare un asiento vacio
        
        if Asientos[venta_de_lugarx][venta_de_lugary] == "O": #aqui dice, si las coordenadas son O
            Asientos[venta_de_lugarx][venta_de_lugary] = "X"  #si, si lo marcara con X de ocupado

            Clientes_info[venta_de_lugarx][venta_de_lugary] = (str(Usuario) + " con pasaporte: " + str(Pasaporte) + " tiene el lugar en fila " + str(venta_de_lugarx) + ", asiento " + str(venta_de_lugary))
            #esto registra la informacion de esta venta en la lista de informacion de clientes

        else:  #si no es O, osea sera X:
            print ("Ese asiento ya esta ocupado, solicite otro")
            asiento_duplicado = True #se activa el protocolo asiento ocupado, pida otro

        while asiento_duplicado == True:   #mientras no elija un asiento libre, seguire molestando con que pida otro
            venta_de_lugarx = int(input("En que fila de asientos se quiere sentar?  "))
            venta_de_lugary = int(input("En que asiento se quiere sentar?  "))

            if Asientos[venta_de_lugarx][venta_de_lugary] == "O":
                Asientos[venta_de_lugarx][venta_de_lugary] = "X"
                Clientes_info[venta_de_lugarx][venta_de_lugary] = (str(Usuario) + " con pasaporte: " + str(Pasaporte) + " tiene el lugar en fila " + str(venta_de_lugarx) + ", asiento " + str(venta_de_lugary))
            #esto registra la informacion de esta venta en la lista de informacion de clientes
                
                asiento_duplicado = False #si elige un espacio libre, se marcara con X y se desactivara el while
            else: #si vuelve a elegir un lugar ocupado volvere a pedirle que elija otro
                print ("Ese asiento ya esta ocupado, solicite otro")
                asiento_duplicado = True

#mostrar el tablero de como va la disponibilidad luego de la venta
    for fila in Asientos:
        for lugar in fila:
            print(lugar, end=" ")  #esto mostrara la disponibilidad actualizada
        print ()


    Contador = 0   #esto verifica cuantos espacios libres quedan
    for fila in Asientos:
        for lugar in fila:
            if lugar == "O":
                Contador = Contador + 1

    print (("Quedan ") + (str(Contador)) + (" asientos vacios"))
    if Contador == 0:  #cuando ya no se detecten O
        print ("Ya no hay lugares disponibles")
        print ("Se termina el programa de venta de la aerolinea :)")
        Fin = True

        #cuando digas si la cosa sigue o no:
    if Habran_mas_clientes == "No" or Habran_mas_clientes == "no" or Habran_mas_clientes == "NO" or Habran_mas_clientes == "nO":
        Fin = True

    if Fin == True: #al terminar se podra revisar informacion de los clientes
        print()
        mostrarrecibos = input("deseas revisar las ventas que hubo?")
        if mostrarrecibos == "Si" or mostrarrecibos == "SI" or mostrarrecibos == "si" or mostrarrecibos == "sI":
            print()
            for fila in Clientes_info:
                for lugar in fila:
                    if lugar != "O": #con esto solo se mostrara la informacion de los lugares ocupados
                        print(lugar)  #esto mostraria la informacion de cada lugar 1 por 1
            print()
            print("los otros " + str(Contador) + " lugares, estan vacios") #muestra que paso con los que no se mencionan
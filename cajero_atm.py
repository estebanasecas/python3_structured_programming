# - *- coding: utf- 8 - *-  
                                                                                                             

#------------------------------------------------------------------------------------------------------------------ ultimos movimientos

movimientos = 0
lista = []

def ultimos_mov():
    
    if movimientos > 0:
        
        print "--------------------------------------------------"
        print "                                    *Saldo Actual*\n"

        for i in range(0, movimientos):

            print '\t', i+1, '%s         %s%s         %s' % (lista[0], lista[1], lista[2], lista[3])            
   
            del lista[0:4]

        print '--------------------------------------------------'

        global movimientos
        movimientos = 0

    else:
     
        print "\n-----------------------------------------------"
        print "No registra ningún movimiento nuevo todavía."                                     
        print "-----------------------------------------------"
  
    menu()

#------------------------------------------------------------------------------------------------------------------ deposito

def deposito():

    while True:

        print "\nCuanto dinero desea depositar: ",
        deposito = raw_input()

        try:

            deposito = int(deposito)

            global saldo_actual
            saldo_actual = saldo_actual + deposito

            print "\n-----------------------------"
            print "Ha depositado $%d" % deposito
            print "Su saldo actual es $%d" % saldo_actual
            print "-----------------------------"

            lista[0:0] = ['Deposito', '+', deposito, saldo_actual]            
           
            global movimientos                                                
            movimientos += 1
            
            menu()
            
        except ValueError:

            print "\nEl comando ingresado no es válido. Intente nuevamente."


#------------------------------------------------------------------------------------------------------------------- retiro


def retiro():

    while True:

        print "\nCuanto dinero desea retirar: ", 
        retiro = raw_input()

        try:

            retiro = int(retiro)

            if retiro <= saldo_actual:

                global saldo_actual
                saldo_actual = saldo_actual - retiro
                print "\n-----------------------------"
                print "Ha retirado $%d" % retiro
                print "Su saldo actual es $%d" % saldo_actual
                print "-----------------------------"

                lista[0:0] = ['Retiro  ', '-', retiro, saldo_actual]

                global movimientos
                movimientos += 1               

                menu()

            else:

                print "\n-----------------------------"
                print "No dispone de esa cantidad"
                print "Su saldo actual es $%d" % saldo_actual
                print "-----------------------------"
                menu()

        except ValueError:

            print "\nEl comando ingresado no es válido. Intente nuevamente."
   

#------------------------------------------------------------------------------------------------------------------- consulta

saldo_actual = 500

def consulta():

    print "\n-----------------------------"
    print "Su saldo actual es: $%d" % saldo_actual
    print "-----------------------------"

    lista[0:0] = ['Consulta', '  ', '  ', saldo_actual]

    global movimientos
    movimientos += 1    

    menu()

#------------------------------------------------------------------------------------------------------------------- end

def end():

    print "\n-----------------------------------------------"
    print "Muchas gracias por utilizar nuestros servicios."
    print "-----------------------------------------------"
    exit(0)

#------------------------------------------------------------------------------------------------------------------- menu

def menu():
           
    print """\nPor favor seleccione una opción:

1. Consulta de saldo.
2. Retiro de efectivo
3. Depósito de efectivo.
4. Últimos movimientos.
5. Salir             
    """
   
    opcion = raw_input('> ')

    while True:           
        
        if opcion == "1":
            consulta()           
            
        elif opcion == "2":
            retiro()
                      
        elif opcion == "3":
            deposito()
                       
        elif opcion == "4":
            ultimos_mov()          
           
        elif opcion == "5":
            end()     

        else:
            print """\nEl comando ingresado no es válido. Intente nuevamente.
        
Por favor seleccione una opción:

1. Consulta de saldo.
2. Retiro de efectivo
3. Depósito de efectivo.
4. Últimos movimientos.
5. Salir             
            """

            opcion = raw_input('> ') 

#---------------------------------------------------------------------------------------------------------------- start    

def start():

    print """----------------------------------------------------------------\n
            **************************************** 
            *Bienvenido al sitema ATM Banco Galicia*
            ****************************************
            (Por favor presione enter para continuar)""", raw_input()

    menu()


           
start()

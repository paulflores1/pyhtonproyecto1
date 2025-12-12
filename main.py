import os
from time import sleep
"""
PROYECTO 01 : CRUD DE EMPRESA
NOMBRE: PAUL VIZCARRA FLORES

"""

dic_empresas = {
    '12345678':{
        'razon_social':'TECSUP',
        'direccion' : 'calle los alamos 123'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)

        while True:
         ruc= input("INGRESE RUC : ")
         if ruc.isdigit():    
            if len(ruc) == 11:                             
                break
            else:
                os.system("clear")
                print("=" * ANCHO)
                print(" " * 10 + "REGISTRAR EMPRESA")
                print("=" * ANCHO)    
                print("EL RUC DEBE TENER 11 DÍGITOS")
         else:
            os.system("clear")
            print("=" * ANCHO)
            print(" " * 10 + "REGISTRAR EMPRESA")
            print("=" * ANCHO) 
            print("EL RUC DEBE SER NÚMERICO")
          

        if ruc in dic_empresas:  
            print("EL RUC YA EXISTE EN EL SISTEMA")
        else:
            razon_social = input("INGRESE RAZÓN SOCIAL : ")
            direccion = input("INGRESE DIRECCIÓN : ")
            dic_empresas[ruc] = {
                'razon_social': razon_social,
                'direccion': direccion
            }
            os.system("clear")
            print("EMPRESA REGISTRADA CON ÉXITO")
     
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESA")
        print("=" * ANCHO)
        for ruc,datos in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"RAZÓN SOCIAL : {datos['razon_social']}")
            print(f"DIRECCIÓN : {datos['direccion']}")
            print("-" * ANCHO)
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  EMPRESA")
        print("=" * ANCHO)
        while True:
         ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR : ")
         if ruc.isdigit():    
            if len(ruc) == 11:                             
                break
            else:
                os.system("clear")
                print("=" * ANCHO)
                print(" " * 10 + "ACTUALIZAR EMPRESA")
                print("=" * ANCHO)    
                print("EL RUC DEBE TENER 11 DÍGITOS")
         else:
            os.system("clear")
            print("=" * ANCHO)
            print(" " * 10 + "ACTUALIZAR EMPRESA")
            print("=" * ANCHO) 
            print("EL RUC DEBE SER NÚMERICO")

        
        if ruc in dic_empresas:
            razon_social = input("INGRESE NUEVA RAZÓN SOCIAL : ")
            direccion = input("INGRESE NUEVA DIRECCIÓN : ")
            if razon_social:
                dic_empresas[ruc]['razon_social'] = razon_social
            if direccion:
                dic_empresas[ruc]['direccion'] = direccion
            
            os.system("clear")
            print("=" * ANCHO)
            print(" " * 10 + "ACTUALIZAR  EMPRESA")
            print("=" * ANCHO)
            print(f"EMPRESA {dic_empresas[ruc]["razon_social"]} ACTUALIZADA CON ÉXITO")

    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "BORRAR  EMPRESA")
        print("=" * ANCHO)

        while True:
         ruc = input("INGRESE RUC DE LA EMPRESA A ELIMINAR : ")
         if ruc.isdigit():    
            if len(ruc) == 11:                             
                break
            else:
                os.system("clear")
                print("=" * ANCHO)
                print(" " * 10 + "BORRAR EMPRESA")
                print("=" * ANCHO)    
                print("EL RUC DEBE TENER 11 DÍGITOS")
         else:
            os.system("clear")
            print("=" * ANCHO)
            print(" " * 10 + "BORRAR EMPRESA")
            print("=" * ANCHO) 
            print("EL RUC DEBE SER NÚMERICO")


        
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            os.system("clear")
            print("EMPRESA ELIMINADA CON ÉXITO")
        else:
            print("EL RUC NO EXISTE EN EL SISTEMA")
        
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")

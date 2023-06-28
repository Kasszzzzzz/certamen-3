import os
os.system("cls")
codigoProducto = [1000,1001,1002,1003,1004]
registrarProductos = []
buscarProducto = []
nombrarProductos = []
listarProductos = []
categoriaProducto = []
precioProducto = [0]
stockProducto = [0]
stock = []
productos = []
menu = '''
        MENU CARACOL EXPRESS
    1. Registrar producto
    2. Buscar producto
    3. Listar producto
    0. Salir
    Digite opcion: '''

def registroProductos():
    print("Registre datos del producto:")
    
    while True:
        try:
            registrarProductos = int(input("registro del producto:  "))
            if codigoProducto > 0:
                productos.append(registrarProductos)
                break
            else:
                print("error,codigo debe ser mayor que CERO")
        except:
                print("Excepcion de codigo")
        #end while del codigo
    while True:
        try:
           nombre = input("Nombre del producto:   ")
           if len (nombre) >=2:
               nombrarProductos.append(nombre)
               break
           else:
               print("Error, nombre debe tener al menos 2 caracteres")
        except:
         print("Excepcion del nombre")
            #end while nombre
    while True:
        try:
            categoria = input("Categoria:")
            if len(categoria)>=3:
                categoriaProducto.append(categoria)
                break
            else:
                print("Error, nombre categoria debe tener al menos 2 caracteres")
        except:
            print("Excepcion del nombre categoria")
            #end while nombre categoria
    while True:
        try:
            precio = int(input("Precio del producto:  "))
            if precio >0:
                precioProducto.append(precio)
                break
            else:
                print("error, numero debe ser mayor que cero")
        except:
            print("excepcion de numero")
            #end while numero-precio
    while True:
        try:
            stock = input("Stock: ")
            if len(stock)>=0:
                stockProducto.append(stock)
                break
            else:
                print("Error,numero de stock debe ser mayor que cero")
        except:
            print("Excepcion de stock")
            #end while de stock
def buscarProductos():
    print("Opcion 2")
    print("Lista de productos      \n")
    print("|N° |CODIGO |NOMBRE|         CATEGORIA  |PRECIO  |STOCK|")
    print("--+-----+---------------------------+---------+---------")
    precio = 0
    for i in range(len(codigoProducto)):
        if precio[i]>=  3:
            stock = "Si"
        stock +=1
    else:
            stock = "No"
    print(f"{i+1} | {codigoProducto[i]:6d} | {nombrarProductos[i]:20s} | {categoriaProducto[i]:10s} | {precioProducto[i]:5s} |{stockProducto[i]:5s})")
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Total de productos: {i+1}" )
    print(f"Cantidad de stock de los productos{stockProducto}")
def listadeProductos():
    print("Opcion 3")
    listarProductos = input ("Stocks de productos:   ")
    print(f"LISTADO DE PRODUCTOS Y STOCK:{stockProducto} \n")
    print("N°| CODiGO | NOMBRE| CATEGORIA      |PRECIO  | STOCK  ")
    print("--+--------+----------------------+------------+----+-")
    listarProductos = 0
    for i in range (len(listarProductos)):
        if listarProductos[i] <=3:
            stock = "Si"
        stock += 1
    else:
        stock = "No"
    if stock.lower() == listadeProductos[i].lower ():
            print(f"{i+1} |{codigoProducto[i]: 6d} {nombrarProductos[i]:20s} | {categoriaProducto[i]:10s} | {precioProducto[i]:5s} | {precioProducto[i]:5s}")
            print("--+--------+----------------------+------------+----+----------")
#programa principal

while True:
    try
        opc =int(input(menu))   
        if opc == 0:
            break
        elif opc ==1 :
            agregarproducto()                  
        elif opc == 2:
            buscadeproductos()
        elif opc == 3:
            ListaDeProductos()
            print("opcion 3")
            listadeProducto = input("ee:   ")
        else:
            print("opcion incorrecta")
    except:
        print("Excepcion de menu")
# endwhile


       



    

     





            

     
                  
        

        



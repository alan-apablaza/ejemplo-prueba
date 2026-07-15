#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]
 
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

#stock = {modelo: [precio, stock], ...] 
 
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1], 
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7], 
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}  

def mostrar_menu():
    print('''
*** MENU PRINCIPAL *** 
1.Stock marca. 
2.Búsqueda por precio. 
3.Actualizar precio. 
4.Salir. 
          ''')

def elegir_opcion():
    while True:
        try:
            opcion = int(input('Ingrese una opción: '))
            return opcion
        except ValueError:
            print('Debe ingresar un número entero positivo.')

def stock_marca(marca):
    suma_stock = 0
    for producto in productos:
        if productos[producto][0].strip().lower() == marca:
            suma_stock += stock[producto][1]
     
    return suma_stock

def programa_principal():
    while True:
        mostrar_menu()
        opcion = elegir_opcion()
        if opcion == 1:
            marca = input('Ingrese la marca: ').strip().lower()
            stock = stock_marca(marca)
            print(f'El stock es: {stock}')

        elif opcion == 2:
            print('opc 2')
        elif opcion == 3:
            print('opc 3')
        elif opcion == 4:
            print('Programa finalizado.')
            break
        else:
            print('Opción no válida.')

programa_principal()
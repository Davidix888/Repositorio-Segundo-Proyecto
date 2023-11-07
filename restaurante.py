bandera = 0
from time import sleep
from os import system
import queue

class Menus:
    def __init__(self):
        self.pila = []

    def ingresar_menu(self, nombre, complementos, precio):
        menu = {"Nombre: ": nombre, "Complementos: ": complementos, "Precio: ": precio}
        self.pila.append(menu)
        print("El menu ha sido ingresado correctamente!")

    def mostrar_menu(self):
        print("Estos son los menús para el dia de hoy: ")
        for menu in self.pila:
            print(f'- {menu["Nombre"]}: {menu["Complementos"]} - Q.{menu["Precio"]}')

    def eliminar_menu(self, indice):
        if 1 <= indice <= len(self.pila):
            eliminar = self.pila.pop(indice-1)
            print(f'El menu "{eliminar["Nombre"]}" ha sido eliminado.')
        else:
            print("Indice no válido. No se eliminó ningún menú.")
    
    def menus_iniciales(self):
        menu1 = {"Nombre": "Combo #1", "Complementos": "Hamburguesa, papas fritas, refresco", "Precio": 50}
        menu2 = {"Nombre": "Combo #2", "Complementos": "Pizza, ensalada, agua", "Precio": 40}
        menu3 = {"Nombre": "Combo #3", "Complementos": "Sándwich, aros de cebolla, batido", "Precio": 45}
        self.pila.extend([menu1, menu2, menu3])
        print("Se han añadido los menús predeterminados.")


    def inicializar(self):
        menu = Menus()
        menu.menus_iniciales()

        while True:
            print("1. Ingresar menu")
            print("2. Mostrar menu")
            print("3. Eliminar Menu")
            print("4. Salir")
            opcion = input("Seleccione una opcion: ")
            match opcion:
                case '1':
                    nombre = input("Ingrese el nombre del combo: ")
                    complementos = input("Ingrese el complemento del menu: ")
                    precio = int(input("Ingrese el precio del menu: "))
                    menu.ingresar_menu(nombre, complementos, precio)
                case '2':
                    menu.mostrar_menu()
                case '3':
                    indice = int(input("Ingrese el menu que desea eliminar: "))
                    menu.eliminar_menu(indice)
                case '4':
                    print("Saliendo de las opciones del menu")
                    break
            
class Pedidos:
    def __init__(self):
        self.pendiente = queue.Queue()
        self.preparacion = queue.Queue()
        self.entregado = queue.Queue()

    def ingreso_pedido(self, combo, nombre):
        pedido = {'Combo': combo, 'Nombre': nombre}
        self.pendiente.put(pedido)
        print(f'El pedido ha sido ingresado a la cola de pendientes')

    def en_preparacion(self):
        if not self.pendiente.empty():
            pedido = self.pendiente.get()
            self.preparacion.put(pedido)
            print(f'El pedido ha sido movido a la cola de preparación')

    def listo_servir(self):
        if not self.preparacion.empty():
            pedido = self.preparacion.get()
            self.entregado.put(pedido)
            print(f'El pedido ha sido entregado')

    def mostrar_pedidos(self):
        print('Pedidos Ingresados: ')
        for pedido in list(self.pendiente.queue):
            print(f'- Pedido: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')

        print('Pedidos en preparación: ')
        for pedido in list(self.preparacion.queue):
            print(f'- Pedido: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')

        print('Pedidos entregados: ')
        for pedido in list(self.entregado.queue):
            print(f'- Pedido: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')

    # funcion utilizada en con busqueda secuencial, lo que hace es buscar por el nombre de la persona el pedido que tiene, cambio realizado en clase
    def buscar_pedido(self, nombre):
        encontrado = False
        for pedido in list(self.pendiente.queue):
            if pedido['Nombre'] == nombre:
                print(f'Pedido encontrado en la cola de pendientes - Combo: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')
                encontrado = True
                break
        for pedido in list(self.preparacion.queue):
            if pedido['Nombre'] == nombre:
                print(f'Pedido encontrado en la cola de preparacion - Combo: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')
                encontrado = True
                break
        for pedido in list(self.entregado.queue):
            if pedido['Nombre'] == nombre:
                print(f'Pedido encontrado en la cola de entregados - Combo: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')
                encontrado = True
                break
        if not encontrado:
            print(f'Pedido no encontrado para el nombre: {nombre}')

    def inicializar_pedidos(self):
        
        objeto = Pedidos()

        while True:
            print('1. Ingreso de pedido')
            print('2. Orden en preparación')
            print('3. Orden a listos para entregar')
            print('4. Ver pedidos')
            print('5. Buscar pedido por nombre')
            print('6. Salir')

            opcion = input('Ingresa la opción que deseas: ')

            match opcion:
                case '1':
                    combo = input('Ingresa el combo que quieres: ')
                    nombre = input('Ingresa tu nombre para la entrega: ')
                    objeto.ingreso_pedido(combo, nombre)
                case '2':
                    objeto.en_preparacion()
                case '3':
                    objeto.listo_servir()
                case '4':
                    objeto.mostrar_pedidos()
                case '5':
                    nombre_buscar = input('Ingrese el nombre para buscar el pedido: ')
                    objeto.buscar_pedido(nombre_buscar)
                case '6':
                    print('saliendo...')
                    break
                case _:
                    print('No ingresaste una opción válida')

menu = Menus()
pedido1 = Pedidos()
while bandera == 0:
    print("BIENVENIDO AL RESTAURANTE")
    print("1. Ver menu")
    print("2. Ver Pedidos")
    print("3. Pagar")
    print("4. Inicio de Sesion")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    match opcion:
        case '1':
            menu.mostrar_menu()
        case '2':
            pedido1.mostrar_pedidos()
        case '4':
            usuario = input("Ingrese su usuario: ")
            contra = input("Ingrese su contraseña: ")
            if usuario == "admin" and contra == "admin":
                while True:
                    print("BIENVENIDO AL MENU DEL ADMINISTRADOR")
                    print("1. Ver todas las opciones del menu")
                    print("2. Ver todas las opciones de pedidos")
                    print("3. Salir")
                    opcion = input("Seleccione una opcion: ")
                    match opcion:
                        case '1':
                            menu.inicializar()
                        case '2':
                            pedido1.inicializar_pedidos()
                        case '3':
                            print("Saliendo del menu de administrador...")
                            break
                        case _:
                            print("No ingreso una opcion valida!")
            else:
                print("Usuario y/o contraseña incorrectos")
                sleep(2)
                system("cls")
        case '5':
            print("Gracias por usar el programa del restaurante!")
            print("Saliendo...")
            bandera = 1
        case _:
            print("No ingreso una opcion valida")
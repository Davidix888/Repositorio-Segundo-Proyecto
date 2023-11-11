import queue
from random import choice
from time import sleep
from os import system

class Menus:
    def __init__(self):
        self.pila = []

    def ingresar_menu(self, nombre, complementos, precio):
        menu = {"Nombre": nombre, "Complementos": complementos, "Precio": precio}
        self.pila.append(menu)
        print("El menú ha sido ingresado correctamente con oferta aplicada!")

    def mostrar_menu(self):
        print("Estos son los menús para el día de hoy: ")
        for menu in self.pila:
            print(f'- {menu["Nombre"]}: {menu["Complementos"]} - Q.{menu["Precio"]}')

        # funcion para ordenar los menus de menor a mayor
        self.ordenamiento_burbuja()
        print("\nMenús ordenados por precio con ordenamiento de burbuja:")
        for menu in self.pila:
            print(f'- {menu["Nombre"]}: {menu["Complementos"]} - Q.{menu["Precio"]}')    

    # Funcion que hace el proceso de el ordemiento de burbuja
    def ordenamiento_burbuja(self):
        n = len(self.pila)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.pila[j]['Precio'] > self.pila[j+1]['Precio']:
                    self.pila[j], self.pila[j+1] = self.pila[j+1], self.pila[j]

    def eliminar_menu(self, indice):
        if 1 <= indice <= len(self.pila):
            eliminar = self.pila.pop(indice-1)
            print(f'El menú "{eliminar["Nombre"]}" ha sido eliminado.')
        else:
            print("Índice no válido. No se eliminó ningún menú.")

    def menus_iniciales(self):
        menu1 = {"Nombre": "Combo #1", "Complementos": "Hamburguesa, papas fritas, refresco", "Precio": 50}
        menu2 = {"Nombre": "Combo #2", "Complementos": "Pizza, ensalada, agua", "Precio": 40}
        self.pila.extend([menu1, menu2])
        print("Se han añadido los menús predeterminados.")

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

    def buscar_pedido(self, nombre):
        encontrado = False
        for pedido in list(self.pendiente.queue):
            if pedido['Nombre'] == nombre:
                print(f'Pedido encontrado en la cola de pendientes - Combo: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')
                encontrado = True
                break
        for pedido in list(self.preparacion.queue):
            if pedido['Nombre'] == nombre:
                print(f'Pedido encontrado en la cola de preparación - Combo: {pedido["Combo"]}, Nombre: {pedido["Nombre"]}')
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
                    print('Saliendo...')
                    break
                case _:
                    print('No ingresaste una opción válida del menú.')

class Usuario:
    def __init__(self, nombre, nit, direccion, tarjeta_credito, fecha_tarjeta, cvv):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.tarjeta_credito = tarjeta_credito
        self.fecha_tarjeta = fecha_tarjeta
        self.cvv = cvv

class SistemaFacturacion:
    def __init__(self):
        self.usuarios = {}
        self.facturas = {}

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        nit = input("Ingrese su número de NIT: ")
        direccion = input("Ingrese su dirección de facturación: ")

        # Funcion para preguntar el metodo de pago a utilizar
        print("\nMétodo de Pago:")
        print("1. Tarjeta de Crédito")
        print("2. Efectivo")
        opcion_pago = input("Seleccione el método de pago (1 o 2): ")

        if opcion_pago == '1':
            tarjeta_credito = input("Ingrese su número de tarjeta de crédito | Formato (XXXX-XXXX-XXXX-XXXX): ")
            tarjeta_credito = tarjeta_credito.replace("-", "")
            fecha_tarjeta = input("Ingrese la fecha de vencimiento de su tarjeta (MM/YY): ")
            cvv = input("Ingrese el CVV de su tarjeta: ")
        else:
            tarjeta_credito = fecha_tarjeta = cvv = None

        usuario = Usuario(nombre, nit, direccion, tarjeta_credito, fecha_tarjeta, cvv)
        self.usuarios[nit] = usuario
        print(f"Usuario {nombre} registrado exitosamente.")

    # En esta funcion se cambio por el uso de nit en vez de correo y se agregó la funcion para generar un descuento que le puede tocar a cualquier usuario del 15% y se escribe en la factura
    def generar_factura(self, nit_usuario, total):
        if nit_usuario in self.usuarios:
            usuario = self.usuarios[nit_usuario]
            numero_factura = len(self.facturas) + 1

            tarjeta_oculta = "X" * (len(usuario.tarjeta_credito) - 4) + usuario.tarjeta_credito[-4:] if usuario.tarjeta_credito else None

            if usuario.tarjeta_credito:
                metodo_pago = 'Tarjeta de Crédito'
            else:
                metodo_pago = 'Efectivo'

            total_oferta = aplicar_oferta(total)

            self.facturas[numero_factura] = {
                'cliente': usuario.nombre,
                'total': total_oferta,
                'direccion': usuario.direccion,
                'nit': usuario.nit,
                'tarjeta_credito': tarjeta_oculta,
                'metodo_pago': metodo_pago
            }

            nombre_archivo = input("Ingrese el nombre para el archivo de texto (sin extensión): ")
            nombre_archivo_txt = f'{nombre_archivo}.txt'

            contenido = f"Restaurante: Fast Food - Proyecto\n"
            contenido += f"Cliente: {usuario.nombre}\n"
            contenido += f"NIT: {usuario.nit}\n"
            contenido += f"Dirección: {usuario.direccion}\n"
            contenido += f"Total (con oferta aplicada): Q{total_oferta}\n" 

            if usuario.tarjeta_credito:
                contenido += f"Tarjeta de Crédito: XXXX-XXXX-XXXX-{tarjeta_oculta[-4:]}\n"

            contenido += f"Método de Pago: {metodo_pago}\n"

            with open(nombre_archivo_txt, 'w') as archivo_txt:
                archivo_txt.write(contenido)

            print(f"\nFactura generada para el usuario {usuario.nombre}, número de factura: {numero_factura}")
            print(f"El archivo de texto '{nombre_archivo_txt}' ha sido guardado.")
        else:
            print("---- Usuario no encontrado ----")

    def inicializar_factura(self):
        sistema_facturacion = SistemaFacturacion()

        while True:
            print("\n---- Menú ----")
            print("1. Registrar Usuario")
            print("2. Generar Factura")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                sistema_facturacion.registrar_usuario()
            elif opcion == "2":
                nit_usuario = input("Ingrese el número de NIT del usuario: ")
                total = float(input("Ingrese el monto total de la factura: "))
                sistema_facturacion.generar_factura(nit_usuario, total)
            elif opcion == "3":
                print("------- FIN DE LA EJECUCIÓN --------")
                break
            else:
                print("Opción no válida, seleccione una opción válida del menú.")

def aplicar_oferta(total):
    # Funcion aleatoria para seleccionar a cualquier usuario y aplicarle el descuento
    if choice([True, False]):
        descuento = total * 0.15  # descuento del 15%
        total_oferta = total - descuento
        print(f"¡Haz ganado un descuento aleatorio del 15%! - Total con descuento: Q{total_oferta}")
        return total_oferta
    else:
        print("No hay oferta aplicada - Total sin descuento")
        return total

def menu_principal():
    menu = Menus()
    pedidos = Pedidos()
    sistema_facturacion = SistemaFacturacion()

    menu.menus_iniciales()

    while True:
        print("\n---- Menú Principal ----")
        print("1. Menús del Restaurante")
        print("2. Pedidos")
        print("3. Inicio de Sesión")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                menu.mostrar_menu()
            case '2':
                pedidos.mostrar_pedidos()
            case '3':
                usuario = input("Ingrese su usuario: ")
                contra = input("Ingrese su contraseña: ")
                while usuario == "admin" and contra == "admin":
                    print("BIENVENIDO AL MENÚ DE ADMINISTRADOR")
                    print("1. Ver opciones de Menús")
                    print("2. Ver opciones de Pedidos")
                    print("3. Ver opciones de Facturación")
                    print("4. Salir")
                    opcion = input("Seleccione una opción: ")

                    match opcion:
                        case '1':
                            while True:
                                print("\n---- Menús del Restaurante ----")
                                print("1. Ingresar menú")
                                print("2. Mostrar menús")
                                print("3. Eliminar menú")
                                print("4. Volver al menú principal")
                                opcion_menu = input("Seleccione una opción: ")

                                match opcion_menu:
                                    case '1':
                                        nombre = input("Ingrese el nombre del combo: ")
                                        complementos = input("Ingrese el complemento del menú: ")
                                        precio = float(input("Ingrese el precio del menú: "))
                                        precio_oferta = aplicar_oferta(precio)
                                        menu.ingresar_menu(nombre, complementos, precio_oferta)
                                    case '2':
                                        menu.mostrar_menu()
                                    case '3':
                                        indice = int(input("Ingrese el menú que desea eliminar: "))
                                        menu.eliminar_menu(indice)
                                    case '4':
                                        print("Regresando al menú principal...")
                                        sleep(2)
                                        break
                                    case _:
                                        print("No ingresó una opción válida!")
                                        sleep(1)
                                        system("cls")
                        case '2':
                            while True:
                                print("\n---- Pedidos ----")
                                print("1. Ingreso de pedido")
                                print("2. Orden en preparación")
                                print("3. Orden a listos para entregar")
                                print("4. Ver pedidos")
                                print("5. Buscar pedido por nombre")
                                print("6. Volver al menú principal")
                                opcion_pedidos = input("Seleccione una opción: ")

                                match opcion_pedidos:
                                    case '1':
                                        combo = input("Ingrese el combo que desea: ")
                                        nombre = input("Ingrese su nombre para la entrega: ")
                                        pedidos.ingreso_pedido(combo, nombre)
                                    case '2':
                                        pedidos.en_preparacion()
                                    case '3':
                                        pedidos.listo_servir()
                                    case '4':
                                        pedidos.mostrar_pedidos()
                                    case '5':
                                        nombre_buscar = input("Ingrese el nombre para buscar el pedido: ")
                                        pedidos.buscar_pedido(nombre_buscar)
                                    case '6':
                                        print("Regresando al menú principal...")
                                        sleep(2)
                                        break
                                    case _:
                                        print("No ingresó una opción válida!")
                                        sleep(1)
                                        system("cls")
                        case '3':
                            while True:
                                print("\n---- Facturación ----")
                                print("1. Registrar Usuario")
                                print("2. Generar Factura")
                                print("3. Volver al menú principal")
                                opcion_facturacion = input("Seleccione una opción: ")

                                match opcion_facturacion:
                                    case '1':
                                        sistema_facturacion.registrar_usuario()
                                    case '2':
                                        nit_usuario = input("Ingrese el número de NIT del usuario: ")
                                        total = float(input("Ingrese el monto total de la factura: "))
                                        sistema_facturacion.generar_factura(nit_usuario, total)
                                    case '3':
                                        print("Regresando al menú principal...")
                                        sleep(2)
                                        break
                                    case _:
                                        print("No ingresó una opción válida!")
                                        sleep(1)
                                        system("cls")
                else:
                    print("Usuario y/o contraseña incorrectos")
                    sleep(2)
            case '4':
                print("Gracias por usar el programa!")
                print("Saliendo...")
                sleep(2)
                break
            case _:
                print("No ingresó una opción válida!")

if __name__ == "__main__":
    menu_principal()

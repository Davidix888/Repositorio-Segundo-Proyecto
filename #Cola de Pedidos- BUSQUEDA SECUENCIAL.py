import queue

class pedidos:
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

objeto = pedidos()

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



        
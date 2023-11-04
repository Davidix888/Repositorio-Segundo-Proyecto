#Cola de Pedidos Fast Food
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
            print(f'El pedido ha sido movido a la cola de preparacion')

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

    
objeto = pedidos()

while True:
    print('1. Ingreso de pedido')
    print('2. Orden en preparacion')
    print('3. Orden a listos para entregar ')
    print('4. Ver pedidos')
    opcion = input('Ingresa la opcion que deseas: ')
    match opcion:
        case '1':
            combo = input('Ingresa el combo que quieres: ')
            nombre = input('Ingresa tu nombre para la entrega: ')
            objeto.ingreso_pedido(combo,nombre)
        case '2':
            objeto.en_preparacion()
        case '3':
            objeto.listo_servir()
        case '4':
            objeto.mostrar_pedidos()
        case '5':
            break
        case _:
            print('No ingresaste una opcion valida')    


        
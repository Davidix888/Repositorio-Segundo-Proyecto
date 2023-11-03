bandera = 0
inventario = {
    'Hamburguesa' : 10,
    'Pizza' : 5,
    'Papas Fritas' : 20,
    'Coca Cola' : 15
}

def menu():
    print("BIENVENIDO AL MENU")
    for item, cantidad in inventario.items():
        print(f'{item}: {cantidad} disponibles')

def hacer_pedido(item, cantidad):
    if item in inventario and inventario[item] >= cantidad:
        print(f'Pedido de {cantidad} {item} realizado.')
        inventario[item] -= cantidad
    else:
        print(f'Lo siento, {item} no está disponible en este momento')

while bandera == 0:
    print("BIENVENIDO AL RESTAURANTE")
    menu()
    opcion = input("¿Que le gustaria ordenar? (0 para salir): ")

    if opcion == '0':
        print("Gracias por utilizar el programa!")
        print("Saliendo...")
        bandera = 1

    item, cantidad = opcion.split()
    cantidad = int(cantidad)
    hacer_pedido(item, cantidad)

print("Gracias por utilizar el programa!")
print("Saliendo...")
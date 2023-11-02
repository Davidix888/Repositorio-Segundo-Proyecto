class Menus:
    def __init__(self):
        self.pila = []

    def ingresar_menu(self, nombre, complementos, precio):
        menu = {"Nombre": nombre, "Complementos": complementos, "Precio": precio}
        self.pila.append(menu)
        print("El menú ha sido ingresado correctamente")

    def mostrar_menu(self):
        print('Estos son los menús para el día de hoy:')
        for menu in self.pila:
            print(f'- {menu["Nombre"]}: {menu["Complementos"]} - Q{menu["Precio"]}')

    def eliminar_menu(self, indice):
        if 1 <= indice <= len(self.pila):
            eliminar = self.pila.pop(indice - 1)
            print(f'El menú "{eliminar["Nombre"]}" ha sido eliminado.')
        else:
            print('Índice no válido. No se eliminó ningún menú.')

    def menus_iniciales(self):
        menu1 = {"Nombre": "Combo #1", "Complementos": "Hamburguesa, papas fritas, refresco", "Precio": 50}
        menu2 = {"Nombre": "Combo #2", "Complementos": "Pizza, ensalada, agua", "Precio": 40}
        menu3 = {"Nombre": "Combo #3", "Complementos": "Sándwich, aros de cebolla, batido", "Precio": 45}
        self.pila.extend([menu1, menu2, menu3])
        print("Se han añadido los menús predeterminados.")

objeto = Menus()
objeto.menus_iniciales()

while True:
    print('1. Ingresar menu')
    print('2. Mostrar menu')
    print('3. Eliminar menu')
    print('4. Salir')
    opcion = input('Ingresa lo que deseas realizar: ')
    match opcion:
        case '1':
            nombre = input('Ingresa el nombre del combo: ')A
            complementos = input('Ingresa el contenido del menu: ')
            precio = int(input('Ingresa el precio del menu: '))
            objeto.ingresar_menu(nombre,complementos,precio)
        
        case '2':
            objeto.mostrar_menu()
        
        case '3':
            indice = int(input('Ingresa el menu que deseas eliminar:' ))
            objeto.eliminar_menu(indice)
        case '4':
            break
            

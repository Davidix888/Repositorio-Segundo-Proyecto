class Usuario:
    def __init__(self, nombre, correo, direccion, tarjeta_credito):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.tarjeta_credito = tarjeta_credito

class SistemaFacturacion:
    def __init__(self):
        self.usuarios = {}
        self.facturas = {}

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico: ")
        direccion = input("Ingrese su dirección de facturación: ")
        tarjeta_credito = input("Ingrese su número de tarjeta de crédito: ")

        usuario = Usuario(nombre, correo, direccion, tarjeta_credito)
        self.usuarios[correo] = usuario
        print(f"Usuario {nombre} registrado exitosamente.")

    def generar_factura(self, correo_usuario, total):
        if correo_usuario in self.usuarios:
            usuario = self.usuarios[correo_usuario]
            numero_factura = len(self.facturas) + 1
            self.facturas[numero_factura] = {
                'cliente': usuario.nombre,
                'total': total,
                'direccion': usuario.direccion,
                'correo': usuario.correo
            }

            nombre_archivo = input("Ingrese el nombre para el archivo de texto (sin extensión): ")
            nombre_archivo_txt = f'{nombre_archivo}.txt'

            contenido = f"Restaurante: Fast Food - Proyecto\n"
            contenido += f"Cliente: {usuario.nombre}\n"
            contenido += f"Correo: {usuario.correo}\n"
            contenido += f"Dirección: {usuario.direccion}\n"
            contenido += f"Total: {total}\n"

            with open(nombre_archivo_txt, 'w') as archivo_txt:
                archivo_txt.write(contenido)

            print(f"Factura generada para el usuario {usuario.nombre}, número de factura: {numero_factura}")
            print(f"El archivo de texto '{nombre_archivo_txt}' ha sido guardado.")
        else:
            print("Usuario no encontrado.")


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
        correo_usuario = input("Ingrese el correo electrónico del usuario: ")
        total = float(input("Ingrese el monto total de la factura: "))
        sistema_facturacion.generar_factura(correo_usuario, total)
    elif opcion == "3":
        print("------- FIN DE LA EJECUCION --------")
        break
    else:
        print("Opción no válida, seleccione una opción válida del menú.")

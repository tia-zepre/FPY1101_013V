import csv
import json
import os

ruta_csv = 'C:\\Users\\tiare\\OneDrive\\Desktop\\tiare\\duoc\\programacion\\experiencia 3\\3.3\\evaluacion formativa\\datos.csv'
ruta_json = 'C:\\Users\\tiare\\OneDrive\\Desktop\\tiare\\duoc\\programacion\\experiencia 3\\3.3\\evaluacion formativa\\planilla.json'
ruta_txt = 'C:\\Users\\tiare\\OneDrive\\Desktop\\tiare\\duoc\\programacion\\experiencia 3\\3.3\\evaluacion formativa\\archivo.txt'


menu_principal=[
    ["Registrar trabajador"],
    ["Listar los todos los trabajadores"], 
    ["Imprimir planilla de sueldos"], 
    ["Salir del Programa"]
]

#cargos
cargos=[
    ["Cargos           "],
    ["CEO              "], 
    ["Desarrollador    "], 
    ["Analista de datos"]
]

#datos
datos=[
    ["Trabajador","Cargo","Sueldo Bruto","Desc. Salud","Desc. AFP","Líquido a pagar "],
    ["ejemplo1","ceo","100000","10000","15000","75000"]
]

#funciones revisadas funcionales
def crear_menu():
    print("\nBienvenido al menú principal\n")
    for i, opcion in enumerate(menu_principal, start=1):
        print(f"{i}. {opcion[0]}")
        
def sueldo_liquido (sueldo_bruto,desc_salud,desc_afc):
    liquido=(sueldo_bruto)-(desc_afc+desc_salud)
    return liquido

def seleccionar_cargo():
    while True:
        try:
            print("\nSeleccione un cargo:")

            # Listar los cargos desde 1 en adelante, saltando el título
            for i, cargo in enumerate(cargos[1:], start=1):
                print(f"{i}. {cargo[0]}")

            opcion = int(input("Ingrese el número correspondiente al cargo: "))

            if 1 <= opcion  or opcion <= (len(cargos) - 1):
                cargo_elegido = cargos[opcion][0]
                print(f"Has elegido el cargo: {cargo_elegido}")
                return cargo_elegido
            else:
                print("Opción no válida. Debes ingresar un número de la lista.")

        except :
            print("Opción no válida. Debes ingresar un número de la lista.")

def mostrar_datos():
    print("\nListado de trabajadores registrados:")
    #encabezados
    encabezados=datos[0]
    print(f"{encabezados[0]}\t{encabezados[1]}\t\t\t{encabezados[2]}\t{encabezados[3]}\t{encabezados[4]}\t{encabezados[5]}\n")
    #datos 
    for i, trabajador in enumerate(datos[1:], start=1):
        print(f"{trabajador[0]}\t{trabajador[1]}\t\t{trabajador[2]}\t\t{trabajador[3]}\t\t{trabajador[4]}\t\t{trabajador[5]}\n")

def agregar_trabajador():
    while True:
        
        trabajador = input("Ingrese el nombre del trabajador o('x' para volver al menú principal): ")

        if trabajador.lower() == 'x':
            break

        cargo = seleccionar_cargo()
        sueldo_bruto = float(input("Sueldo Bruto: "))
        desc_salud = float(input("Descuento Salud: "))
        desc_afp = float(input("Descuento AFP: "))
        liquido_a_pagar = sueldo_liquido(sueldo_bruto, desc_salud, desc_afp)

        # Agregar datos del trabajador
        datos.append([trabajador, cargo, sueldo_bruto, desc_salud, desc_afp, liquido_a_pagar])
        print("Trabajador registrado exitosamente")
        op = input("\n¿Desea ingresar otro trabajador (si/no)?\n")
        if op.lower() == "no":
            return datos
            break



#funciones por revisar
#en estas funciones se corrigieron con ayuda de chat gpt
def guardar_planilla_txt(ruta_txt, datos_externo):
    try:
        #os.makedirs: Crea directorios recursivamente.
        #os.path.dirname: Obtiene el nombre del directorio de una ruta.
        #para luego verificar si el directorio existe o no 
        os.makedirs(os.path.dirname(ruta_txt), exist_ok=True)

        #crar archivo y escribir
        with open(ruta_txt, 'w') as archivo:
            for fila in datos_externo:
                #en vez de hacer 2 for utilizamos map para revisar las filas transformandolas a tipo str
                #y escribirlas en archivo tipo txt
                archivo.write("\t".join(map(str, fila)) + "\n")
        print(f"Planilla guardada en {ruta_txt}")
    except:
        print(f"Error: No se pudo guardar la planilla en {ruta_txt}")


def imprimir_planilla(ruta_txt):
    print("\nSelecciona una opción para imprimir la planilla:")
    print("1. Imprimir todos los trabajadores")
    print("2. Imprimir por cargo específico")
    print("3. Volver al menú principal")
    
    opcion = input()
    
    if opcion == '1':
        print("\nTodos los trabajadores:")
        with open(ruta_txt, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())
                
    elif opcion == '2':
        cargo_elegido = input("Ingrese el cargo específico para filtrar: ").lower()

        print(f"\nTrabajadores con cargo '{cargo_elegido}':")
        
        with open(ruta_txt, 'r') as archivo:
            for linea in archivo:
                
                if cargo_elegido in linea.lower():
                    print(linea.strip())
                    
    elif opcion == '3':
        return



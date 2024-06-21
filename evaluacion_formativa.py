"""
Una empresa necesita desarrollar una aplicación que permita registrar los sueldos brutos
de los trabajadores y calcular el líquido
a pagar. Para ello necesita que la aplicación cumpla con las siguientes funcionalidades

1. Registrar trabajador
Para registrar un trabajador se requiere los siguiente: Nombre y Apellido,
Cargo, Sueldo bruto. Debe validar que todos los datos sean ingresados.

2. Listar los todos los trabajadores

Una vez ingresado los datos, se deben calcular, los valores de acuerdo con la siguiente tabla

Trabajador        Cargo    Sueldo Bruto    Desc. Salud     Desc. AFP     Líquido a pagar 
Homero Simpson    CEO      1000000         70000           120000        810000
Listar los todos los trabajadores

Debe mostrar en la pantalla la lista de todos los trabajadores 
similar al ejemplo anterior de registrar un solo trabajador

3. Imprimir planilla de sueldos

Imprimir planilla de sueldos
Para imprimir la planilla, 
el usuario puede seleccionar imprimir todos o por algún cargo en específico. 
Estos cargos deben estar previamente definidos en algún tipo de colección de Python en el código 
y por lo menos deben ser tres, por ejemplo: CEO, Desarrollador, Analista de datos.
Al seleccionar uno de los cargos, se generará un archivo de texto (.txt)
Este debe tener la misma forma del registro 
completo de las opciones anteriores, pero en archivo de texto. 
con el detalle de los sueldos. 

4. Salir del Programa



Cada una de estas opciones de la aplicación debe estar desarrollada en 
una función que debe ser llamada desde el programa principal
El programa debe funcionar hasta que el usuario decida finalizar el programa
Al finalizar, 
debe subir el archivo de comprimido como evidencia del trabajo realizado. 
Luego, debe aplicar la pauta de evaluación formativa (Coevaluación).

"""
import csv
import json
import os
           
from funciones_evaf import menu_principal,cargos,datos,sueldo_liquido,seleccionar_cargo,agregar_trabajador,crear_menu,mostrar_datos,imprimir_planilla,guardar_planilla_txt

ruta_csv = 'C:\\Users\\tiare\\OneDrive\\Desktop\\tiare\\duoc\\programacion\\experiencia 3\\3.3\\evaluacion formativa\\datos.csv'
ruta_json = 'C:\\Users\\tiare\\OneDrive\\Desktop\\tiare\\duoc\\programacion\\experiencia 3\\3.3\\evaluacion formativa\\planilla.json'
ruta_txt = 'C:\\Users\\tiare\\OneDrive\\Desktop\\tiare\\duoc\\programacion\\experiencia 3\\3.3\\evaluacion formativa\\archivo.txt'

# Rutas a los archivos
ruta_datos = os.path.join('archivos', 'datos.csv')
ruta_json = os.path.join('archivos', 'planilla.json')
ruta_txt = os.path.join('archivos', 'archivo.txt')


# Main 
while True:
    try:
        crear_menu()
        op = int(input("Ingrese una opción: "))
        
        if op == 1:
            agregar_trabajador()
            
        
        elif op == 2:
            #aqui lista los datos
            mostrar_datos()
        
        elif op == 3:
            guardar_planilla_txt(ruta_txt, datos)
            imprimir_planilla(ruta_txt)
        
        elif op == 4:
            print("\nSaliendo del programa\n")
            break
    
    except ValueError:
        print("Opción no válida. Debes ingresar un número del menú.")
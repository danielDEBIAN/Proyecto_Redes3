# Importamos librerias
import PySimpleGUI as sg

# Definimos el tema de la ventana
sg.theme('Dark')

# Definimos el layout de la ventana
layout = [
    [sg.Text('Configuracion de Routers')],
    [sg.Text('¿Que deseas hacer?')],
    [sg.Button('Configurar routers'),sg.Button('Configurar enrutamiento')],
    [sg.Button('Configurar DHCP'), sg.Button('Configurar NAT')],
    [sg.Button('Salir')]
]

# Creamos la ventana
window = sg.Window('Proyecto Final', layout)

# Generamos el loop para que se procesen lso eventos y se obtengan valores

while True:
    event, values = window.read()
    if event == 'Salir' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
        break

window.close()
    

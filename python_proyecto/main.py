# Importamos librerias
import PySimpleGUI as sg
import sys

# Creamos una clase para obtener el output de la terminal
class OutputRedirector:
    def __init__(self, output_elem):
        self.output_elem = output_elem

    def write(self, message):
        # Modificamos el elemento output de la interfaz
        self.output_elem.update(value=message)

    def flush(self):
        pass

# Funcion para ventana de mostrar configuracion
def configuration():
    # Definimos el tema de la ventana
    sg.theme('DarkTanBlue')

    # Definimos el layout de la ventana
    layout_configuration = [
        [sg.Text('Mostrar configuracion', justification='center')],
        [sg.Output(size=(80,20), key='-OUTPUT-')],
        [sg.Button('Imprimir'), sg.Button('Regresar')]
    ]

    # Creamos la ventana
    window_configuration = sg.Window('Configuracion', layout_configuration)

    # Mandamos el output a la terminal
    output_redirector = OutputRedirector(window_configuration['-OUTPUT-'])
    sys.stdout = output_redirector

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_configuration.read()
        if event == 'Imprimir':
            print('Hola a todos')
        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_configuration.close()
            main()
            break
    # Restauramos el output
    sys.stdout = sys.__stdout__

    window_configuration.close()

# Funcion para ventana de mostrar enrutamiento
def routing():
    # Definimos el tema de la ventana
    sg.theme('DarkTanBlue')

    # Definimos el layout de la ventana
    layout_routing = [
        [sg.Text('Mostrar configuracion', justification='center')],
        [sg.Text('¿Que router quieres observar su enrutamiento?', justification='center')],
        [sg.Button('Router1'), sg.Button('Router2')],
        [sg.Button('Router3'), sg.Button('Router4')],
        [sg.Button('RouterPC'), sg.Button('Toda la red')],
        [sg.Button('Regresar')]
    ]

    # Creamos la ventana
    window_routing = sg.Window('Enrutamiento', layout_routing)

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_routing.read()
        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_routing.close()
            main()
            break
    window_routing.close()

# Funcion para conectarse a routers
def connect():
    # Definimos el tema de la ventana
    sg.theme('DarkTanBlue')

    # Definimos el layout de la ventana
    layout_connect = [
        [sg.Text('Conectarse a routers', justification='center')],
        [sg.Text('¿A que router quieres acceder?', justification='center')],
        [sg.Button('Router1'), sg.Button('Router2')],
        [sg.Button('Router3'), sg.Button('Router4')],
        [sg.Button('RouterPC')],
        [sg.Button('Regresar')]
    ]

    # Creamos la ventana
    window_connect = sg.Window('Conectarse', layout_connect)

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_connect.read()
        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_connect.close()
            main()
            break
    window_connect.close()

# Funcion para mostrar varios
def varios():
    # Definimos el tema de la ventana
    sg.theme('DarkTanBlue')

    # Definimos el layout de la ventana
    layout_varios = [
        [sg.Text('Varios', justification='center')],
        [sg.Text('¿Que configuracion quieres observar?', justification='center')],
        [sg.Button('ACL'), sg.Button('DHCP'), sg.Button('NAT')],
        [sg.Button('DNS'), sg.Button('VPN'), sg.Button('SNMP')],
        [sg.Button('Regresar')]
    ]

    # Creamos la ventana
    window_varios = sg.Window('Configuracion', layout_varios)

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_varios.read()
        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_varios.close()
            main()
            break
    window_varios.close()

# Funcion main
def main():
    # Definimos el tema de la ventana
    sg.theme('DarkTanBlue')

    # Definimos el layout de la ventana
    layout_main = [
        [sg.Text('Configuracion de Routers', justification='center')],
        [sg.Text('¿Que deseas hacer?', justification='center')],
        [sg.Button('Mostrar configuracion'), sg.Button('Mostrar enrutamiento')],
        [sg.Button('Conectarse a routers'), sg.Button('Varios')],
        [sg.Button('Salir')]
    ]

    # Creamos la ventana
    window_main = sg.Window('Proyecto Final', layout_main)

    # Definimos el bucle para que permanezca abierta la ventaan
    while True:
        event, values = window_main.read()
        if event == 'Salir' or event == sg.WIN_CLOSED:
            break
        if event == 'Mostrar configuracion':
            window_main.close()
            configuration()
        if event == 'Mostrar enrutamiento':
            window_main.close()
            routing()
        if event == 'Conectarse a routers':
            window_main.close()
            connect()
        if event == 'Varios':
            window_main.close()
            varios()
    window_main.close()

# Ejecutamos el codigo de main
if __name__ == '__main__':
    main()
    
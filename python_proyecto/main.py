# Importamos librerias
import PySimpleGUI as sg
import paramiko
import telnetlib
import time

# Funcion para ventana de mostrar configuracion
def show_configuration():
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_configuration = [
        [sg.Text('IP del router', font=('Arial', 15))],
        [sg.Input(key='-INPUT-IP-', font=('Arial', 12))],
        [sg.Text('Usuario', font=('Arial', 15))],
        [sg.Input(key='-INPUT-USER-', font=('Arial', 12))],
        [sg.Text('Password', font=('Arial', 15))],
        [sg.Input(key='-INPUT-PASS-', password_char='*', font=('Arial', 12))],
        [sg.Text('¿Que configuracion deseas ver?', font=('Arial', 15))],
        [sg.DropDown(["Resumen","Interfaces", "Ruteo", "ACL", "DHCP", "NAT", "DNS"], key='-DROPDOWN-', font=('Arial', 12))],
        [sg.Text("", size=(1, 1))],
        [sg.Button('Conectarse', font=('Arial', 12))],
        [sg.Output(size=(80,20), font=('Arial', 12), key="-OUTPUT-")],
        [sg.Button('Regresar', font=('Arial', 10))]
    ]

    # Creamos la ventana
    window_configuration = sg.Window('Mostrar configuraciones', layout_configuration, element_justification='center')

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_configuration.read()
        if event == 'Conectarse':
            if values['-DROPDOWN-'] == "Resumen":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_configuration(values['-INPUT-IP-'], values['-INPUT-USER-'], values['-INPUT-PASS-'])
                    print(output)
                except Exception as e:
                    print('Error:', str(e))
            elif values['-DROPDOWN-'] == "Interfaces":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_interfaces(values['-INPUT-IP-'], values['-INPUT-USER-'], values['-INPUT-PASS-'])
                    print(output)
                except Exception as e:
                    print('Error:', str(e))
            elif values['-DROPDOWN-'] == "Ruteo":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_route(values['-INPUT-IP-'], values['-INPUT-USER-'], values['-INPUT-PASS-'])
                    print(output)
                except Exception as e:
                    print('Error:', str(e))
            
        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_configuration.close()
            main()
            break

    window_configuration.close()

def get_configuration(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('enable\n')
        time.sleep(1)
        shell.send('enable_password\n')
        time.sleep(1)
        shell.send('show running-config brief\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

def get_route(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('enable\n')
        time.sleep(1)
        shell.send('enable_password\n')
        time.sleep(1)
        shell.send('show ip route\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)
    
def get_interfaces(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('enable\n')
        time.sleep(1)
        shell.send('enable_password\n')
        time.sleep(1)
        shell.send('show ip interface brief\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

# Funcion para ventana de mostrar enrutamiento
def routing():
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

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
    sg.theme('DarkTeal6')

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
    sg.theme('DarkTeal6')

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
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_main = [
        [sg.Text('Configuracion de Routers', justification='center', font=('Arial', 18))],
        [sg.Text('¿Que deseas hacer?', justification='center', font=('Arial', 15))],
        [sg.Button('Mostrar configuracion', font=('Arial', 12)), sg.Button('Mostrar enrutamiento', font=('Arial', 12))],
        [sg.Button('Conectarse a routers', font=('Arial', 12)), sg.Button('Varios', font=('Arial', 12))],
        [sg.Button('Salir', font=('Arial', 10))]
    ]

    # Creamos la ventana
    window_main = sg.Window('Proyecto Final', layout_main, element_justification='center')

    # Definimos el bucle para que permanezca abierta la ventaan
    while True:
        event, values = window_main.read()
        if event == 'Salir' or event == sg.WIN_CLOSED:
            break
        if event == 'Mostrar configuracion':
            window_main.close()
            show_configuration()
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
    
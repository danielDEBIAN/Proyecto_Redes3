# Importamos librerias
import PySimpleGUI as sg
import paramiko
import time

# Funcion para ventana de mostrar configuracion
def session(usuario, password):
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_configuration = [
        [sg.Text('¿Como deseas conectarte?', font=('Consolas', 13))],
        [sg.Text("", size=(1, 1))],
        [sg.Button('Conectarse por IP', font=('Consolas', 10))],
        [sg.Button('Conectarse por Router', font=('Consolas', 10))],
        [sg.Text("", size=(1, 1))],
        [sg.Button('Cerrar Sesion', font=('Consolas', 8))]
    ]

    # Creamos la ventana
    window_session = sg.Window('Mostrar configuraciones', layout_configuration, element_justification='center')

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_session.read()
        if event == 'Conectarse por IP':
            window_session.close()
            show_connection_ip(usuario, password)
            break
        if event == 'Conectarse por Router':
            window_session.close()
            show_connection_router(usuario, password)
            break
        if event == 'Cerrar Sesion' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_session.close()
            main()
            break

    window_session.close()

def show_connection_ip(usuario, password):
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_configuration = [
        [sg.Text('IP del router', font=('Consolas', 13))],
        [sg.Input(key='-INPUT-IP-', font=('Consolas', 10))],
        [sg.Text('¿Que configuracion deseas ver?', font=('Consolas', 13))],
        [sg.DropDown(["Interfaces", "Ruteo", "ACL", "DHCP", "NAT", "DNS"], key='-DROPDOWN-', font=('Consolas', 10))],
        [sg.Text("", size=(1, 1))],
        [sg.Button('Conectarse', font=('Consolas', 10))],
        [sg.Output(size=(80,10), font=('Consolas', 10), key="-OUTPUT-")],
        [sg.Button('Regresar', font=('Consolas', 8))]
    ]

    # Creamos la ventana
    window_configuration = sg.Window('Mostrar configuraciones', layout_configuration, element_justification='center')

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_configuration.read()
        if event == 'Conectarse':
            if values['-INPUT-IP-'] == "":
                sg.popup('Error', 'Digite una IP')
            if values['-DROPDOWN-'] == "Interfaces":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_interfaces(values['-INPUT-IP-'], usuario, password)
                    print(output)
                except Exception as e:
                    print('Error:', str(e))
            elif values['-DROPDOWN-'] == "Ruteo":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_route(values['-INPUT-IP-'], usuario, password)
                    print(output)
                except Exception as e:
                    print('Error:', str(e))
            elif values['-DROPDOWN-'] == '':
                sg.popup('Error', 'Seleccione una opcion')
            
        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_configuration.close()
            session(usuario, password)
            break

    window_configuration.close()

def show_connection_router(usuario, password):
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_configuration = [
        [sg.Text('Selecciona el router', font=('Consolas', 13))],
        [sg.DropDown(["R1","R2", "R3", "R4", "R5"], key='-DROPDOWN-', font=('Consolas', 10))],
        [sg.Text("", size=(1, 1))],
        [sg.Button('Conectarse', font=('Consolas', 10))],
        [sg.Button('Regresar', font=('Consolas', 8))]
    ]

    # Creamos la ventana
    window_configuration = sg.Window('Mostrar configuraciones', layout_configuration, element_justification='center')

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_configuration.read()
        if event == 'Conectarse':
            if values['-DROPDOWN-'] == "R1":
                window_configuration.close()
                connection_router('10.1.1.1', usuario, password)
                break
            if values['-DROPDOWN-'] == "R2":
                window_configuration.close()
                connection_router('10.1.4.1', usuario, password)
                break
            if values['-DROPDOWN-'] == "R3":
                window_configuration.close()
                connection_router('10.1.3.1', usuario, password)
                break
            if values['-DROPDOWN-'] == "R4":
                window_configuration.close()
                connection_router('10.1.3.2', usuario, password)
                break
            if values['-DROPDOWN-'] == "R5":
                window_configuration.close()
                connection_router('192.172.10.1', usuario, password)
                break
            elif values['-DROPDOWN-'] == "":
                sg.popup('Error', 'Seleccione una opcion')

        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_configuration.close()
            session(usuario, password)
            break

    window_configuration.close()

def connection_router(ip, usuario, password):
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_configuration = [
        [sg.Text('¿Que configuracion deseas ver?', font=('Consolas', 13))],
        [sg.DropDown(["Interfaces", "Ruteo", "ACL", "DHCP", "NAT", "DNS"], key='-DROPDOWN-', font=('Consolas', 10))],
        [sg.Text("", size=(1, 1))],
        [sg.Button('Mostrar', font=('Consolas', 10))],
        [sg.Output(size=(80,10), font=('Consolas', 10), key="-OUTPUT-")],
        [sg.Button('Regresar', font=('Consolas', 8))]
    ]

    # Creamos la ventana
    window_configuration = sg.Window('Mostrar configuraciones', layout_configuration, element_justification='center')

    # Generamos el loop para que se procesen los eventos y se obtengan valores
    while True:
        event, values = window_configuration.read()
        if event == 'Mostrar':
            if values['-DROPDOWN-'] == "Interfaces":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_interfaces(ip, usuario, password)
                    print(output)
                except Exception as e:
                    print('Error: ', str(e))
            elif values['-DROPDOWN-'] == "Ruteo":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_route(ip, usuario, password)
                    print(output)
                except Exception as e:
                    print('Error: ', str(e))
            elif values['-DROPDOWN-'] == "ACL":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_lists(ip, usuario, password)
                    print(output)
                except Exception as e:
                    print('Error: ', str(e))
            elif values['-DROPDOWN-'] == "DHCP":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_dhcp(ip, usuario, password)
                    print(output)
                except Exception as e:
                    print('Error: ', str(e))
            elif values['-DROPDOWN-'] == "NAT":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_nat(ip, usuario, password)
                    print(output)
                except Exception as e:
                    print('Error: ', str(e))
            elif values['-DROPDOWN-'] == "DNS":
                try:
                    window_configuration['-OUTPUT-'].update("")
                    print('Conectando ...')
                    output = get_dns(ip, usuario, password)
                    print(output)
                except Exception as e:
                    print('Error: ', str(e))
            elif values['-DROPDOWN-'] == "":
                sg.popup('Error', 'Seleccione una opcion')

        if event == 'Regresar' or event == sg.WIN_CLOSED: # Definimos si se cierra la ventana se termina el evento o si se selecciona salir
            window_configuration.close()
            session(usuario, password)
            break

    window_configuration.close()

# Funcion para obtener la informacion de ruteo
def get_route(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show ip route\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

# Funcion para obtener el resumen de las interfaces
def get_interfaces(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show ip interface brief\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

# Funcion para obtener las listas de acceso
def get_lists(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show access-lists\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)
    
# Funcion para obtener la informacion de DHCP
def get_dhcp(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show running-config | include dhcp pool\n')
        time.sleep(1)
        shell.send('show ip dhcp binding\n')
        time.sleep(1)
        shell.send('show ip dhcp server statistics\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

# Funcion para obtener la informacion de NAT
def get_nat(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show running-config | include nat\n')
        time.sleep(1)
        shell.send('show ip nat translations\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)
    
# Funcion para obtener la informacion de DNS
def get_dns(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show running-config | include dns\n')
        time.sleep(1)
        shell.send('show run | section name-server\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

# Funcion para obtener la informacion de VPN
def get_vpn(ip, user, password):
    try:
        # Realizamos la configuracion de SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, port='22', username=user, password=password)

        # Mandamos los comandos que queremos
        shell = ssh_client.invoke_shell()
        time.sleep(1)
        shell.send('show interfaces tunnel 0\n')
        time.sleep(1)
        shell.send('show crypto session\n')
        time.sleep(1)
        shell.send('show crypto isakmp policy\n')
        time.sleep(5) 
        output = shell.recv(65535).decode('ascii')
        return "Conexion exitosa!\n"+output
    except Exception as e:
        return "Error en la conexion:\n"+str(e)

# Funcion main
def main():
    # Definimos el tema de la ventana
    sg.theme('DarkTeal6')

    # Definimos el layout de la ventana
    layout_main = [
        [sg.Text('Usuario', font=('Consolas', 15))],
        [sg.Input(key='-INPUT-USER-', font=('Consolas', 10))],
        [sg.Text('Contraseña', font=('Consolas', 15))],
        [sg.Input(key='-INPUT-PASS-', password_char='*', font=('Consolas', 10))],
        [sg.Button('Iniciar sesion', font=('Consolas', 10)), sg.Button('Salir', font=('Consolas', 10))]
    ]

    # Creamos la ventana
    window_main = sg.Window('Proyecto Final', layout_main, element_justification='center')

    # Definimos el bucle para que permanezca abierta la ventaan
    while True:
        event, values = window_main.read()
        if event == 'Salir' or event == sg.WIN_CLOSED:
            window_main.close()
            break
        if event == 'Iniciar sesion' and values['-INPUT-USER-'] == 'cisco' and values['-INPUT-PASS-'] == 'cisco':
            window_main.close()
            session(values['-INPUT-USER-'], values['-INPUT-PASS-'])
            break
        else:
            sg.popup('Error', 'Revisa tus credenciales')
    window_main.close()

# Ejecutamos el codigo de main
if __name__ == '__main__':
    main()
    
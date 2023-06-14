# Proyecto Redes 3
> Este proyecto se realizo con la finalidad de recopilar los conocimientos obtenidos durante el curso

## Documentacion de SimpleGUI
1. Como instalar:
* https://www.pysimplegui.org/en/latest/
2. GitHub del proyecto:
* https://github.com/PySimpleGUI/PySimpleGUI

## Tutorial de SimpleGUI
https://realpython.com/pysimplegui-python/

## Se debe instalar tkinter con este comando:
```bash
sudo apt-get install python3-tk 
```
### Si no funciona checar esta pagina:
https://www.tutorialspoint.com/how-to-install-tkinter-in-python

## Requerimentos:
Mediante un programa de Python ​que corra en mi maquina Virtual  en GNS3​
Deberá de mostrarme:​
1. La configuración de toda mi red(cada router) incluyendo las vpc​
2. Protocolos de enrutamiento configurados en cada router.​
3. Tener conectividad con ssh y telnet (conectarme a cualquier router solo con correr el prohrama)​
4. Mostrarme  ​
    * ACL​
    * DHCP​
    * NAT​
    * DNS​
    * VPN​
5. ALGUNA APLICACIÓN DE SNMP (EJEMPLO SI DESCONECTO UNA INTERFAZ O LA BORRO, ESTARE SIMULANDO QUE SE ROMPIO UN 
ENLACE ENTONCES QUE EN LA CONSOLA O INTERFAZ GRAFICA SE MUESTRE LA CAIDA DEL ENLACE). con interfaz grafica esto puede ser mas sencillo.​

## Enlace de la presentacion de codigos de Python del profe
https://correoipn.sharepoint.com/:p:/r/sites/ASR4CM15232/_layouts/15/Doc.aspx?action=edit&sourcedoc=%7Ba139ab32-a9f9-456c-a25c-5dd8ea85aa35%7D&wdOrigin=TEAMS-WEB.teamsSdk.openFilePreview&wdExp=TEAMS-CONTROL&web=1

## Conexion a routers
Para que las librerias que se usan para la conexion de routers funcionen, debemos instalar "Paramiko" con el siguiente comando:
```bash
pip install paramiko
```

## IP para PC
La IP para la maquina virtual debe ser:
```bash
192.172.10.2
```
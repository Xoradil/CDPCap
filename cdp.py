#Based on code from https://allones.de/2018/10/31/python-scapy-capturing-cisco-discovery-protocol-cdp/
#Modified by Cameron Cunningham
#This is a Cisco Discovery Protocol(CDP) tool designed to tell you what port on which switch you' re connected to

import PySimpleGUI as sg
from scapy.all import *

sg.theme('LightGray1') 
 


adapters = []

for i in ifaces.data.keys():
    iface = ifaces.data[i]
    adapters.append(str(iface.name))


interface = 'Ethernet'
capfilter = 'ether dst 01:00:0c:cc:cc:cc'

#packet = sniff(iface = interface, count=2 , filter=capfilter)
#packet
#packet.display()

layout = [  [sg.Text('Welcome to port checker')], 
            [sg.Text('Your connections: ')], [sg.Radio(text, 1) for text in adapters],  
            [sg.Button('Find port'), sg.Button('Cancel')] 
] 

window = sg.Window('CDP Port Checker', layout)

while True: 
    event,values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break 
 
window.close() 
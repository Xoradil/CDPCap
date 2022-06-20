#Based on code from https://allones.de/2018/10/31/python-scapy-capturing-cisco-discovery-protocol-cdp/
#Modified by Cameron Cunningham
#This is a Cisco Discovery Protocol(CDP) tool designed to tell you what port on which switch you' re connected to

import PySimpleGUI as sg
from scapy.all import *

sg.theme('LightGray1') 
 

adapters = []
port = ""
deviceName = ""


for i in ifaces.data.keys():
    iface = ifaces.data[i]
    adapters.append(str(iface.name))

   

capfilter = 'ether dst 01:00:0c:cc:cc:cc'



layout = [  [sg.Text('Welcome to port checker')], 
            [sg.Text('Your connections: ')], [sg.Combo(adapters,key='interface')],  
            [sg.Button('Find port'), sg.Button('Cancel')] 
] 
layout3 = [ [sg.Text('Capturing Packets')],
           ]


window = sg.Window('CDP Port Checker', layout)

while True: 
    event,values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break 
    elif event == 'Find port':
        interface = values['interface']
        load_contrib('cdp')
        packet = sniff(iface = interface, count=3 , filter=capfilter)
        for i in packet:
            if len(i) > 60:
                usablePacket = i
        window.close()
        
        #usablePacket.show()
        port=usablePacket["CDPMsgPortID"].iface.decode()
        deviceName = usablePacket["CDPMsgDeviceID"].val.decode()
        layout2 = [
            [sg.Text("Port connected to: " + port)],
            [sg.Text("Device name: " + deviceName)],
            [sg.Button('Close')],
        ]
        window2 = sg.Window('Results',layout2)
        e,v = window2.read()
        if event == sg.WIN_CLOSED or event == 'Close': 
            break 

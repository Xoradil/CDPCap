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



capfilter = 'ether dst 01:00:0c:cc:cc:cc'



layout = [  [sg.Text('Welcome to port checker')], 
            [sg.Text('Your connections: ')], [sg.Combo(adapters,key='interface')],  
            [sg.Button('Find port'), sg.Button('Cancel')] 
] 
layout2 = [
    [sg.Text("\n Capturing Packet\n")]
]


window = sg.Window('CDP Port Checker', layout)

while True: 
    event,values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break 
    elif event == 'Find port':
       #window2 = sg.Window('Capturing',layout2)
        #e,v=window2.read()
        interface = values['interface']
        load_contrib('cdp')
        packet = sniff(iface = interface, count=5 , filter=capfilter)
        #window2.close()
        for i in packet:
            if len(i) > 60:
                print(len(i))
                useablePacket = i
        useablePacket.show()
        port=useablePacket["CDPMsgPortID"].iface.decode()
        print(port)

window.close() 
#Based on code from github user chrisbog https://github.com/CiscoSE/cdp_discover/blob/master/cdp.py
#Modified by Cameron Cunningham
#This is a Cisco Discovery Protocol(CDP) tool designed to tell you what port on which switch you' re connected to

import PySimpleGUI as sg
import pcapy
from dpkt import ethernet


def onPacket(header,data):
    frame = ethernet.Ethernet(data)

    #CDP packets start at byte position 22 and the data needed starts at byte 26
    #Find the length of the entire frame
    etherLen = len (frame)

    CDPStart = 22
    CDPData = 26

    #loop through the packet until we get the data we need
    count = CDPData

    while count < etherLen:
        #First two bytes contain the typeID of the CDP packet
        typeid = 256 * ord(data[count]) + ord(data[count+1])
        #The next two bytes give the length of the CDP packet
        length = 256 * ord(data[count+2]) + ord(data[count+3])
        #Find and grab the data fields
        cdpField = data[count+4:count+length]

        if typeid == 1:
            deviceName = cdpField
        elif typeid == 3:
            portNum = cdpField
        elif typeid == 6:
            deviceType == cdpField

        count = count + length


devices = pcapy.findalldevs()

sg.theme('LightGray1')

layout = [  [sg.Text('Welcome to port checker')],
            [sg.Text('Your connections: ')], 
            [sg.Button('Find port'), sg.Button('Cancel')]
]

window = sg.Window('CDP Port Checker', layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()

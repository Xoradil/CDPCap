#Based on code from github user chrisbog https://github.com/CiscoSE/cdp_discover/blob/master/cdp.py
#Modified by Cameron Cunningham
#This is a Cisco Discovery Protocol(CDP) tool designed to tell you what port on which switch you' re connected to

import PySimpleGUI as sg
from scapy.all import *



adapters = []

for i in ifaces.data.keys():
    iface = ifaces.data[i]
    adapters.append(str(iface.name))

print (adapters)
interface = 'Ethernet'

packet = sniff(iface = interface, count=2 , filter='ether dst 01:00:0c:cc:cc:cc')
packet
packet.display()
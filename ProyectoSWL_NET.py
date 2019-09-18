#!/usr/bin/python 

""" Se emplea una topologia que consiste en un controlador local,
7 switch y 6 hosts, trabajando con Mininet"""

"""Inicia Mininet"""
from mininet.net import Mininet
from mininet.node import Controller
from mininet.node import CPULimitedHost
from mininet.link import TCLink 
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

def myTreeNet():
    
    ListaSwitch = []
    ListaHost = []

    """ Crea una red de arbol con un controlador local y links restringidos"""
    net = Mininet( controller=Controller, link=TCLink )
    
    """ Add controlador local """
    net.addController ('c0')

    """ Add swtiches """
    for x in range(0, 7):
	    ListaSwitch.append(net.addSwitch('s'+str(x)))

    """ Add hosts """
    for x in range (0, 6):
	    ListaHost.append(net.addHost('h'+str(x+1), ip = '200.31.1.'+str(x+1)))

    """Crea los enlaces"""
       #Switch
    for x in range(0,3):
	    if x ==  0:
	        net.addLink(ListaSwitch[x], ListaSwitch[x+1], bw=100, delay='100ms')
		net.addLink(ListaSwitch[x], ListaSwitch[x+2], bw=100, delay='100ms')
	    if x == 1:
		net.addLink(ListaSwitch[x], ListaSwitch[x+2], bw=100, delay='100ms')
		net.addLink(ListaSwitch[x], ListaSwitch[x+4], bw=100, delay='100ms')
	    if x == 2:
		net.addLink(ListaSwitch[x], ListaSwitch[x+2], bw=100, delay='100ms')
		net.addLink(ListaSwitch[x], ListaSwitch[x+4], bw=100, delay='100ms')
	
	#Host      
    for x in range(0,6):
	    if x == 0 or x == 1 :
	        net.addLink(ListaHost[x], ListaSwitch[3], bw=1000, delay='1ms')
	    if x == 2:
		net.addLink(ListaHost[x], ListaSwitch[5], bw=1000, delay='1ms')
	    if x == 3:
		net.addLink(ListaHost[x], ListaSwitch[2], bw=1000, delay='1ms')
	    if x == 4 or x == 5:
		net.addLink(ListaHost[x], ListaSwitch[6], bw=1000, delay='1ms')
    
    net.start()
    
    dumpNodeConnections(net.hosts)
    
    net.pingAll()
    

    """ Prueba entre hosts """
    for x in range (0, 5):
       net.iperf((ListaHost[x], ListaHost[x+1]))
       net.iperf((ListaHost[x+1], ListaHost[x]))
    
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myTreeNet()










#!/usr/bin/python 

""" Se emplea una topologia que consiste en un controlador local,
7 switch y 6 hosts, trabajando con Mininet"""

"""Inicia Mininet"""
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink 
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

def myTreeNet():

    """ Crea una red de arbol con un controlador local y enlaces """
    net = Mininet( controller=Controller, link=TCLink )
    
    """ Add controlador local """
    net.addController ('c0')

    """ Add swtiches """
    s0 = net.addSwitch('s0')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    """ Add hosts """
    h1a = net.addHost ('h1a', ip='200.31.1.1')
    h2a = net.addHost ('h2a', ip='200.31.1.2')
    h3b = net.addHost ('h3b', ip='200.31.1.3')
    h4c = net.addHost ('h4c', ip='200.31.1.4')
    h5d = net.addHost ('h5d', ip='200.31.1.5')
    h6d = net.addHost ('h6d', ip='200.31.1.6')

    """Crea los enlaces"""
    net.addLink(s1, s0, bw=100, delay='10ms')
    net.addLink(s2, s0, bw=100, delay='10ms')
    net.addLink(s3, s1, bw=100, delay='10ms')
    net.addLink(s4, s1, bw=100, delay='10ms')
    net.addLink(s5, s2, bw=100, delay='10ms')
    net.addLink(s6, s2, bw=100, delay='10ms')

    net.addLink(h1a, s3, bw=1000, delay='10ms')
    net.addLink(h2a, s3, bw=1000, delay='10ms')

    net.addLink(h3b, s4, bw=1000, delay='10ms')

    net.addLink(h4c, s5, bw=1000, delay='10ms')

    net.addLink(h5d, s6, bw=1000, delay='10ms')
    net.addLink(h6d, s6, bw=1000, delay='10ms')

    net.start()

    dumpNodeConnections(net.hosts)

    net.pingAll()
    
    """ Prueba entre hosts """
    h1a, h2a = net.get ('h1a', 'h2a')
    net.iperf((h1a, h2a))

    h2a, h1a = net.get('h2a', 'h1a')
    net.iperf((h2a, h1a))

    h2a, h3b = net.get ('h2a', 'h3b') 
    net.iperf((h2a, h3b))

    h3b, h4c = net.get ('h3b', 'h4c')
    net.iperf((h3b, h4c))

    h4c, h5d = net.get ('h4c', 'h5d')
    net.iperf((h4c,h5d))

    h5d, h6d = net.get ('h5d', 'h6d')
    net.iperf((h5d, h6d))

    h6d, h5d = net.get ('h6d', 'h5d')
    net.iperf((h6d, h5d))


    CLI(net)
    
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myTreeNet()










# Proyecto Integrador de la materias de Fundamentos de Networking y Software Libre

Implementar la emulación de una red Lan y parámetros de medición en el software MININET de acuerdo a las siguientes indicaciones:

 1. Inicie mininet.
 2. Implemente la topología.
 3. Haga ping entre todos los hosts.
 4. Salga del programa.


# Topología
![](https://lh3.googleusercontent.com/FSmt4e7aCQ9CdwV9FzJmhlCCTOv6YW6dX_c_2uuVnqpuzppYh25KDioQxr2_cu6KzHi1RxMCeVYg "TopologiaProyecto")

> Topología tipo árbol que tiene una dirección ip 200.31.1.0

# Code

 

> Todas las librerías a utilizar

```py
from mininet.net import Mininet
from mininet.node import Controller
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info 
```
```py
def  myTreeNet():

ListaSwitch = []

ListaHost = []
```

> Crea una red tipo árbol con un controlador local y links restringidos.
```py
net = Mininet( controller=Controller, link=TCLink )
``` 
> Añade el controlador
```py
net.addController ('c0')
```
> Añadiendo switches
```py
for x in  range(0, 7):

ListaSwitch.append(net.addSwitch('s'+str(x)))
```

> Añadiendo Hosts 

```py 
for x in  range (0, 6):

ListaHost.append(net.addHost('h'+str(x+1), ip  =  '200.31.1.'+str(x+1)))
```

> Creando los enlaces entre switches

```py
for x in  range(0,3):

if x ==  0:

net.addLink(ListaSwitch[x], ListaSwitch[x+1], bw=100, delay='100ms')

net.addLink(ListaSwitch[x], ListaSwitch[x+2], bw=100, delay='100ms')

if x ==  1:

net.addLink(ListaSwitch[x], ListaSwitch[x+2], bw=100, delay='100ms')

net.addLink(ListaSwitch[x], ListaSwitch[x+4], bw=100, delay='100ms')

if x ==  2:

net.addLink(ListaSwitch[x], ListaSwitch[x+2], bw=100, delay='100ms')

net.addLink(ListaSwitch[x], ListaSwitch[x+4], bw=100, delay='100ms')
```

> Creando enlaces entre switches y hosts
```py
for x in  range(0,6):

if x ==  0  or x ==  1 :

net.addLink(ListaHost[x], ListaSwitch[3], bw=1000, delay='1ms')

if x ==  2:

net.addLink(ListaHost[x], ListaSwitch[5], bw=1000, delay='1ms')

if x ==  3:

net.addLink(ListaHost[x], ListaSwitch[2], bw=1000, delay='1ms')

if x ==  4  or x ==  5:

net.addLink(ListaHost[x], ListaSwitch[6], bw=1000, delay='1ms')
```

> Inicia la red
```py
net.start()
```
```py
dumpNodeConnections(net.hosts)
```
> Realiza ping entre todos los hosts 
```py
net.pingAll()
```
> Prueba el rendimiento de ancho de banda entre los hosts
```py
for x in  range (0, 5):

net.iperf((ListaHost[x], ListaHost[x+1]))

net.iperf((ListaHost[x+1], ListaHost[x]))
```

> Detiene la ejecución de la red 
```py
net.stop()
```
```py
if  __name__  ==  '__main__':

setLogLevel( 'info' )

myTreeNet()
```

# Integrantes

 1. Steven Silva
 2. Ronny Guevara
 3. Andrea Cárdenas




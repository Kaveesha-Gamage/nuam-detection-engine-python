import os
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.link import TCLink

def create_lab_network():
    net = Mininet(
        controller=Controller,
        switch=OVSSwitch,
        link=TCLink,
        autoSetMacs=True
    )

    print("*** Adding controller")
    net.addController('c0')

    print("*** Adding switch")
    s1 = net.addSwitch('s1')

    print("*** Adding LAN hosts")
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    h4 = net.addHost('h4', ip='10.0.0.4/24')

    print("*** Adding IDS host")
    hIDS = net.addHost('hIDS', ip='10.0.0.100/24')

    print("*** Creating links")
    for h in (h1, h2, h3, h4, hIDS):
        net.addLink(h, s1)

    print("*** Adding real NAT")
    nat = net.addNAT()
    nat.configDefault()

    print("*** Starting network")
    net.start()
    
    nat_ip = nat.IP()
    
    print("*** Setting default routes")
    for h in (h1, h2, h3, h4, hIDS):
        h.cmd(f'ip route add default via {nat_ip}')

    print("*** Configuring port mirroring")

    ids_port = None
    for intf in s1.intfList():
        if intf.link and hIDS in (intf.link.intf1.node, intf.link.intf2.node):
            ids_port = intf.name
            break

    if not ids_port:
        raise RuntimeError("IDS interface not found")

    os.system(f"""
    ovs-vsctl \
    -- --id=@p get port {ids_port} \
    -- --id=@m create mirror name=ids-mirror select-all=true output-port=@p \
    -- set bridge s1 mirrors=@m
    """)

    return net

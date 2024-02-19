import random
import threading
import os
import socket
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch, OVSSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink, Link

class Network:

    def run(self):

        # defining net
        net = Mininet(controller=RemoteController, link=TCLink)

        # adding hosts
        h1 = net.addHost("h1", ip="192.168.1.2", mac="00:00:00:00:00:01")
        h2 = net.addHost("h2", ip="192.168.1.3", mac="00:00:00:00:00:02")
        h3 = net.addHost("h3", ip="192.168.1.4", mac="00:00:00:00:00:03")
        h4 = net.addHost("h4", ip="192.168.1.5", mac="00:00:00:00:00:04")
        h5 = net.addHost("h5", ip="192.168.1.6", mac="00:00:00:00:00:05")
        h6 = net.addHost("h6", ip="192.168.1.7", mac="00:00:00:00:00:06")
        h7 = net.addHost("h7", ip="192.168.1.8", mac="00:00:00:00:00:07")
        h8 = net.addHost("h8", ip="192.168.1.9", mac="00:00:00:00:00:08")

        # adding switches
        s1 = net.addSwitch("s1")
        s2 = net.addSwitch("s2")
        s3 = net.addSwitch("s3")
        s4 = net.addSwitch("s4")
        s5 = net.addSwitch("s5")
        s6 = net.addSwitch("s6")
        s7 = net.addSwitch("s7")
        s8 = net.addSwitch("s8")
        

        # adding controller with IP address and port
        net.addController("C0", controller=RemoteController, ip="127.0.0.1", port=6633)

        # defining link options (used for delay and bandwidth detection on the links)
        hostlink = dict (bw = 1000, delay='0ms', cls=TCLink) 
        base_link = dict(bw = 1000, delay='4ms', cls=TCLink) 
        mid_link = dict(bw = 570, delay='7ms', cls=TCLink) 
        busy_link = dict(bw = 400, delay='10ms', cls=TCLink) 

        net.addLink(h1, s1, **hostlink)
        net.addLink(s1, s2, **base_link)
        net.addLink(s1, s3, **base_link)

        net.addLink(h2, s2, **hostlink)
        net.addLink(s2, s3, **mid_link)
        net.addLink(s2, s4, **mid_link)
        net.addLink(s2, s5, **busy_link)

        net.addLink(h3, s3, **hostlink)
        net.addLink(s3, s5, **mid_link)

        net.addLink(h4, s4, **hostlink)
        net.addLink(s4, s5, **mid_link)
        net.addLink(s4, s6, **base_link)

        net.addLink(h5, s5, **hostlink)
        net.addLink(s5, s6, **busy_link)
        net.addLink(s5, s7, **mid_link)

        net.addLink(h6, s6, **hostlink)
        net.addLink(s6, s7, **mid_link)
        net.addLink(s6, s8, **base_link)

        net.addLink(h7, s7, **hostlink)
        net.addLink(s7, s8, **base_link)

        net.addLink(h8, s8, **hostlink)

        # running network
        net.start()

        CLI(net)

        # stopping network
        net.stop()

if __name__ == "__main__":
    network = Network()
    network.run()


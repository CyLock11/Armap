#!/usr/bin/env python3

from scapy.all import *
from mac_vendor_lookup import MacLookup
import ipaddress
import netifaces

class InterfaceError(ValueError):

    def __init__(self, msg):

        super().__init__(msg)

def parse_iface(iface):

    # get the interfaces
    interfaces = netifaces.interfaces()

    # check if the interface exists
    if iface not in interfaces:

        raise InterfaceError(f"The interface {iface} does not exist")

def get_utils(iface):

    addr_ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    addr_mac = netifaces.ifaddresses(iface)[netifaces.AF_LINK][0]['addr']
    netmask = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['netmask']

    network = ipaddress.ip_network(f"{addr_ip}/{netmask}", strict=False)

    count_hosts = network.num_addresses

    return addr_ip, addr_mac, network, count_hosts

def get_vendor(addr_mac):

    try:

        vendor = MacLookup().lookup(addr_mac)

    except:

        vendor = "Not found"

    return vendor

def scan_network(iface, network):

    # discovered hosts
    active_hosts = []

    pkts = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=str(network))

    ans, _ = srp(pkts, timeout=1, iface=iface, verbose=0)

    for snd, rcv in ans:

        active_hosts.append((rcv.psrc, rcv.hwsrc))

    return sorted(active_hosts, key=lambda x: ipaddress.IPv4Address(x[0]))

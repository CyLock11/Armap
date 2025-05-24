#!/usr/bin/env python3

from termcolor import colored
from utils import get_utils, scan_network, parse_iface, get_vendor, InterfaceError
import argparse
import signal
import time
import sys

def def_handler(sig, frame):

    print(colored("\n\n[!] Saliendo...\n", 'red'))
    sys.exit(0)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

def get_arguments():

    parser = argparse.ArgumentParser(description="Tool to discover active hosts using the ARP protocol")

    parser.add_argument('-i', required=True, dest="iface", help="Interface containing the network to be scanned")

    return parser.parse_args().iface

def main():

    iface = get_arguments()

    parse_iface(iface)

    try:

        ip, mac, network, count_hosts = get_utils(iface)

    except KeyError as e: 

        missing_key = e.args[0]

        if missing_key == 2:

            key_error = "IPv4"

        elif missing_key == 17:

            key_error = "MAC"

        else:

            key_error = "Not found"

        raise(InterfaceError(f"Missing interface data: {key_error}"))

    # Header
    print(colored("Interface:", 'cyan'),
          colored(iface, 'green') + ",",
          colored("MAC:", 'cyan'),
          colored(mac, 'magenta') + ",",
          colored("IPv4:", 'cyan'),
          colored(ip, 'blue'))

    # Main message
    print(colored(f"Starting armap 1.0 with {count_hosts} hosts", 'yellow'),
          colored(f"(https://github.com/CyLock11/Armap)", 'grey'), "\n")

    start_time = time.time()

    active_hosts = scan_network(iface, network)

    end_time = time.time()

    final_time = end_time - start_time

    for host, mac in active_hosts:

        vendor = get_vendor(mac)

        print(colored(host, 'blue'), "\t",
              colored(mac, 'magenta'), "\t",
              colored(vendor, 'yellow'))

    print(colored("\nEnding armap 1.0:", 'yellow'),
          colored(f"{count_hosts} hosts scanned", 'blue'),
          colored("in %.2f seconds" % (final_time), 'cyan'))

if __name__ == '__main__':

    main()

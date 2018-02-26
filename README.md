# Illumio-Firewall
This project contains 2 files: a code file and a test file containing sample rules. 

In order to run this file, I've used 'ipaddress' module which is one of the standard library in python to deal with IP addresses (both IPv4 and IPv6)

In case this module is not found on the system it can be installed via following command: sudo pip install ipaddress

In order to run this code, an instance of 'Firewall' class needs to be created and then path of csv file containing rules must be passed as argument. The file name is firewall.py which must be in the same directory from where execution is performed. 

The following steps needs to be performed to execute this code:
from firewall import Firewall
fw = Firewall("<path_to_csv_file>")
fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")     (will return true when executed from python shell)
...

One assumption which I made in this is that rules are correctly defined, ports are in the range of 1-65535, IPv4 addresses are in the range of 0.0.0.0-255.255.255.255.

This code works fine for IPv6 addresses as well.  

As of now this firewall is stateless in nature (it doesn't remember any state). If given more time I would like to turn it into a stateful firewall which is more efficient and lookup is much faster since it "remembers" states.  

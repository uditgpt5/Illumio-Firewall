from ipaddress import ip_address

class Firewall(object):
	def __init__(self, path_to_rules_file):
		self.rules_file = path_to_rules_file

	def accept_packet(self, direction_pkt, protocol_pkt, port_pkt, ip_address_pkt):
		match = False
		file_handler = open(self.rules_file, 'r')
		for line in file_handler:
		    row = line.rstrip('\n')
		    direction, proto, ports, ipaddresses = row.split(',')

		    port_range = ports.split('-')
		    port_range_list = []
		    if len(port_range) > 1:
            		port_range_list = range(int(port_range[0]), int(port_range[1])+1)
        	    else:
            		port_range_list.append(int(port_range[0]))			
		    
		    ipaddress_range = ipaddresses.split('-')
		    ipaddress_range_list = []
		    if len(ipaddress_range) > 1:
			start_ip = ip_address(unicode(ipaddress_range[0], "utf-8"))
			end_ip = ip_address(unicode(ipaddress_range[1], "utf-8"))
			for ip_range in range(int(start_ip), int(end_ip)+1):
			    ipaddress_range_list.append(ip_address(ip_range))
		    else:
			start_ip = ip_address(unicode(ipaddress_range[0], "utf-8"))
			for ip_range in range(int(start_ip), int(start_ip)+1):
			    ipaddress_range_list.append(ip_address(ip_range))

		    ip_address_pkt_IP_format = ip_address(unicode(ip_address_pkt, "utf-8"))

		    if direction_pkt == direction and protocol_pkt == proto and int(port_pkt) in port_range_list and ip_address_pkt_IP_format in ipaddress_range_list:
			match = True
			break
		return match 

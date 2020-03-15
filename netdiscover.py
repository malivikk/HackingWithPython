import ipaddress
import subprocess
import argparse
import time

def PortScan(subnet, verbose=False, silent=False):
	t1 = time.time()
	hostl = []
	ip_net = ipaddress.ip_network(subnet)
	if verbose and not silent:
		print("Starting Scan in subnet %s" % subnet)
	all_hosts  = list(ip_net.hosts())
	
	for i in range(len(all_hosts)):
		output = subprocess.Popen(["ping", "-c", "1", "-w", "500", str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0]
		
		if "100% packet loss" in output.decode("utf-8"):
			if verbose and not silent:
				print(str(all_hosts[i]), "is Offline")
		else:
			if silent: print(str(all_hosts[i]), "is Online")
			hostl.append(all_hosts[i]
	t2 = time.time()
	if silent: print("Scan lasts for %s s" % str(t2-t1))
	return hostl

if __name__ == "__main__":
	v = False
	subn = ""
	description = "This is a little tool to discover all devices within a subnet"
	
	parser = argparse.ArgumentParser(description=description)

	parser.add_argument("-v", "--verbose", help="run program with more comments", action="store_true")
	parser.add_argument("-s", "--subnet", help="subnet to scan")
	
	args = parser.parse_args()
	
	if args.verbose:
		v = True
	
	if args.subnet:
		subn = args.subnet
	else:
		raise Error("You need to specify a subnet to scan on")
	
	_ = PortScan(subn, verbose=v)

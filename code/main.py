import math
import sys
import time
import json


SERVER_LOAD_PATH = "test1/server_load"
SERVER_CAP_PATH = "test1/server_capabilities"

server_loads = {}

def get_servers():
	content = open(SERVER_CAP_PATH, "r").read().split("\n")
	servers = content[0].split()
	caps = content[1].split()
	server_caps = {}
	for server, capability in zip(servers, caps):
		server_caps[server] = int(capability)
	return server_caps

def read_loads():
	global server_loads
	content = open(SERVER_LOAD_PATH, "r").read().split("\n")
	servers = content[0].split()
	for server in servers:
		server_loads[server] = []
	for loads in content[1:]:
		for server,load in zip(servers, loads.split()):
			server_loads[server].insert(0, int(load))

#Simulating read from server port because the script dint work
#Just have to send the message to the server received in this function
# and return the load value the server returns
def get_load(server_name):
	return server_loads[server_name].pop()

def get_load_snapshot():
	snapshot = {}
	for server in server_loads:
		snapshot[server] = get_load(server)
	return snapshot

def find_best_server(servers, loads):
	best_server = None
	min_time = sys.maxint
	for server in servers.keys():
		if loads[server] < 0:
			continue
		free_moment = math.ceil(float(loads[server])/float(servers[server]))
		if free_moment<min_time:
			min_time = free_moment
			best_server = server
		elif free_moment == min_time:
			if servers[server] > servers[best_server]:
				best_server = server
	return best_server

def print_result(packet, current_load, best_server):
	print str(packet) + "\t" + json.dumps(current_load) + "\t\t" + best_server

def update_loads(servers, loads, best_server):
	loads[best_server] += 5
	for key in servers.keys():
		if loads[key] < 0:
			continue
		loads[key]-= servers[key]
		if loads[key] < 0:
			loads[key] = 0
	return loads

def main():
	read_loads()
	servers = get_servers()
	print "SERVERS:"
	print servers
	print
	print "RESULTS:"
	count = 0
	loads = None
	while True:
		if count%5 == 0:
			loads = get_load_snapshot()
		count += 1
		best_server = find_best_server(servers, loads)
		print_result(count, loads, best_server)
		loads = update_loads(servers, loads, best_server)



if __name__ == "__main__":
	try:
		main()
	except IndexError:
		print "DONE"
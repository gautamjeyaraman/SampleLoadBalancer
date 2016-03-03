====================================
Instructions to run
====================================
- Download the code
- Update the paths of the server load and capability files in the firs two lines of the script
- Run using "python main.py"
- The output will be printed in the console

====================================
Sample test files
====================================
- Sample test files are given at test1,test2,test3 folders
- The corresponding results are in output_test*.txt files

====================================
A minor gotcha
====================================
- Since the server code was not running in mac, I have simulated the server in the function get_load in line number 34
- The code now reads the loads directly from the file
- To make it work with the server, onlyl change is to call the server in this function call and return the value returned by the server

====================================
How it works
====================================
- For every 5 packets, the code gets the current load from the servers
- For every packet, the algorithm returns the best server and the packet goes to that server
- Best server is calculated as follow:
	- The server is the first one to be free after all its load is processed
	- The server is available (its load is not -1)
	- If two servers get free at the same time, return the server which has the better processing power
- Though the loads are fetched only once per 5 packets, the loads are updated for every packet based in the processing power and the current packet added to it

====================================
PS
====================================
- The file main_nsfw.py has the code to read from the servers as well
- Not sure if it will work because its not tested
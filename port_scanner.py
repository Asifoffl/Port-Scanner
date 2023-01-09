import socket
from datetime import datetime as dt
import sys

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of args")
    print("Syntax: python3 port_scanner.py [ip/hostname]")

print("Scanning target: "+target)
print("Time started: "+str(dt.now()))
print("-"*50)

try:
    for port in range(1, 1000):
        s = socket.socket()
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            s.close()
except KeyboardInterrupt:
    print("\nExiting.....")
    sys.exit()
except socket.gaierror:
    print("Hostname could'nt be resolved")
    sys.exit()
except socket.error:
    print("Could'nt connect to server")
    sys.exit()
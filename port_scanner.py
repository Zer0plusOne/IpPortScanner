# IP port scanner

import socket
import threading
import time
import os
import sys

def final():
    print("Thanks for using this tool, restarting to the main page...")
    time.sleep(5)
    os.system("python3 port_scanner.py")
#ASCII ART 

logo = """\033[33m

██╗██████╗       ██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██║██╔══██╗      ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║██████╔╝█████╗██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║██╔═══╝ ╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║██║           ██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝╚═╝           ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                                    \033[37m[✔]    https://github.com/Zer0plusOne/     [✔]
                                    \033[37m[✔]            Version 1.0.0               [✔]
                                    \033[91m[X] Please Don't Use For illegal Activity  [X]

\033[30mTo exit write on the IP addres "00.00.00.00"                                                                                                               
\033[97m"""
print (logo)
#enter the ip address of the target
ip = input("Enter the IP address of the target: ")
if ip == "00.00.00.00":
    print("Exiting...")
    time.sleep(5)
    sys.exit()
# Enter the port range to scan

start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# Scan the ports between start_port and end_port

for port in range(start_port, end_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"\033[32mPort {port} is open\033[97m")
        s.close()
    else:
        print(f"\033[31mPort {port} is closed\033[97m")
        s.close()
# execute the final function
final()


import socket
import termcolor

def scan(target, ports):
    for port in range(1,ports):
        scan_port(target, ports)


def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress,port))
        print("[+] Port Opened" + str(port))
        sock.close()
    except:
        print("[-] Port Colse"  + str(port))



target = input("[*] Enter Target To Scan: ")
ports = input("[*] Enter How Many Ports You Want To Scan: ")




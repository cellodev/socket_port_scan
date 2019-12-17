from multiprocessing import Pool
import socket

ports = range(1024) #set range ports Eg: 0-1024

def scane(port):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(0.1) #set timeout reponse (seconds)
    code = scan.connect_ex(('127.0.0.1', port)) #set address for portscan
    if code == 0:
        print(port, "- Open")

if __name__ == "__main__":
    p = Pool()
    print("Running... Please Wait")
    p.map(scane,ports)
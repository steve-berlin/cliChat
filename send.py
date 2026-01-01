import subprocess as sp

IP = "192.168.1.50"
PORT = "8080"
sp.call(f"nc {IP} {PORT} < msg.txt", shell=True)
print("Message sent!")

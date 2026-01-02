import subprocess as sp

PORT = "8080"
# Redirection works here because shell=True is used
sp.call(f"cd incoming;nc -l -p {PORT} > msg.txt", shell=True)

from pydub import AudioSegment as audio
from pydub.playback import play
from time import sleep
from os import system

sfx = audio.from_mp3("sfx.mp3")
try:
    with open("incoming/msg.py.txt", "w") as f:
        f.write("")
except FileNotFoundError:
    with open("incoming/msg.py", "x") as f:
        f.write("")
incoming = open("incoming/msg.py", "r").read()
while incoming == "":
    sleep(0.5)
play(sfx)
system(f'notify-send "You have recieved a message" "{incoming}"')

from pydub import AudioSegment as audio
from pydub.playback import play
from time import sleep
from os import system

incoming = open("incoming.txt", "r").read()
sfx = audio.from_mp3("sfx.mp3")
try:
    with open("incoming.txt", "w") as f:
        f.write("")
except FileNotFoundError:
    with open("incoming.txt", "x") as f:
        f.write("")
while incoming == "":
    sleep(0.5)
play(sfx)
system(f'notify-send "You have recieved a message" "{incoming}"')

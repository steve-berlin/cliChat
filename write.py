txt = 'Write your message here.\n When finished write "END"'
line = ""
print(txt)
while line != "END":
    line = input("\nnext line>> ")
    with open("msg.txt", "a") as f:
        f.write(line)

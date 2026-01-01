# Startup
txt = 'Write your message here.\n When finished write "END"'
line = ""
print(txt)
# Clear msg.txt
open("msg.txt", "w").write("")
# Main texting logic
while line != "END":
    line = input("\nnext line>> ")
    if line != "END":
        with open("msg.txt", "a") as f:
            f.write(f"{line}\n")

from time import sleep

frames = ["Listening   ", "Listening.  ", "Listening.. ", "Listening..."]
while True:
    for frame in frames:
        # \r at start resets cursor; end="" prevents newline
        print(f"\r{frame}", end="", flush=True)
        sleep(0.25)

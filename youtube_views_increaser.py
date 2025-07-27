import webbrowser
import os
import time



url =  input("https://youtu.be/nf7h7dpMavs")

refreshrate = input("10")

browserr = input("Chrome")


def letsdoit():
    os.system("TASKKILL /F /IM "+browserr+".exe")
    webbrowser.open(url)
    time.sleep(int(refreshrate))

views = input("200)
for i in range(int(views)+1):
    letsdoit()

#!/usr/bin/env python3
from datetime import datetime
from gpiozero import Button
from time import sleep
import json

# Define Buttons
buttonRight = Button(16)
buttonLeft = Button(21)

def main():
    if buttonLeft.is_pressed:
        writeFile("Left")
        sleep(.2)
    if buttonRight.is_pressed:
        writeFile("Right")
        sleep(.2)

def writeFile(side):
    x = datetime.now()
    y = {'date':str(x.year) + "-" + str(x.month) + "-" + str(x.day), 'time':str(x.hour) + ":" + str(x.minute) + ":" + str(x.second), 'button':side}
    with open("log.txt", "a") as f:
        f.write(json.dumps(y) + "\n")

if __name__ == "__main__":
    while True:
        main()

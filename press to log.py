#!/usr/bin/env python3
from datetime import datetime
from gpiozero import Button
from time import sleep

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
    concat = str(x.year) + "-" + str(x.month) + "-" + str(x.day) + " " + str(x.hour) + ":" + str(x.minute) + "\t" + side + "\n"
    with open("log.txt", "a") as f:
        f.write(concat)

if __name__ == "__main__":
    while True:
        main()

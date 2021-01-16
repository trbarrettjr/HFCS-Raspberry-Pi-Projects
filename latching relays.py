#!/usr/bin/env python3

# Get the libraries
from gpiozero import Button, LED

# Establish our variables
left = Button(21) # On physical pin of GPIO board
right = Button(16) # Button on physical pin of GPIO Board
relay1 = LED(19, active_high=False) # Relay board is a little weird, needs to have active_high=False to turn off relay
relay2 = LED(6, active_high=False)

def main():
    while True:
        left.when_pressed = relay2.toggle
        right.when_pressed = relay1.toggle

if __name__ == '__main__':
    main()

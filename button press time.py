#!/usr/bin/env python3

# Get the libraries
from gpiozero import Button, LED
import time

# Establish our variables
left = Button(21) # On physical pin of GPIO board
right = Button(16) # Button on physical pin of GPIO Board

def main():
    while True:
        if left.is_pressed: # First, Analyze if the left button is pressed
            print("You pressed the left button for", left.pressed_time, "seconds")  # Printed Statement of event
            time.sleep(.2) # Sleep to prevent message runaway
        if right.is_pressed: # Second, New analysis, if the right button is pressed
            print("You pressed the right button for", right.pressed_time, "seconds") # Printed statement of event
            time.sleep(.2) # Sleep to prevent message runaway

# Always good to put this on the bottom of your python code to load your code first then start it.
if __name__ == "__main__":
    main()

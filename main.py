
# SPDX-FileCopyrightText: 2018 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board
import neopixel
from analogio import AnalogIn


pot = AnalogIn(board.A1)  # what pin the pot is on
pixpin = board.D0  # what pin the LEDs are on
numpix = 16  # number of LEDs in ring!
BPP = 4  # required for RGBW ring
ORDER = neopixel.RGB

num_ring = 0

ring = neopixel.NeoPixel(pixpin, numpix, bpp=BPP, brightness=0.01)
# colors = [(255, 0, 0), (255, 150, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (180, 0, 255)]


def val(pin):
    # divides voltage (65535) to get a value between 0 and 255
    return pin.value / 257


def cycleCW(wait):
    # for color in colors:
     for j in range(100,255):
         for i in range(16):
            time.sleep(wait)
            ring[i] = (255, 0, 0)
            time.sleep(0.01)
            
            ring[i-1] = (0, 0, 0)
        # Fill the pixels with the current color and wait for 0.5 seconds
        # fill_color(color)


def cycleCCW(wait):
    # for color in colors:
        for j in range(100, 255):
            for i in range(16):
                time.sleep(wait)
                k = 15-i
                ring[k] = (255, 0, 0)
                time.sleep(0.1)
                ring[k] = (0, 0, 0)
        # Fill the pixels with the current color and wait for 0.5 seconds
        # fill_color(color)

while True:
    print("1 = CW ; 2 = CCW")
    x = int(input("Enter a number: "))
    if x == 1:
        cycleCW(0.1)
    else:
        cycleCCW(0.1)
    # cycleKY(0.1) colorwhee
    i = 0

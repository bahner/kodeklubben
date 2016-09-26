"""Write my name with a turtle

The task was to write my name with a turtle, but I haven't learned how to "jump"
yet. So I just make the program write funny triangles.
"""
#coding: utf-8

from time import sleep
from turtle import * #pylint: disable=W0401,W0614

PENSIZE = 60

speed(11)
pensize(PENSIZE)

def draw_line(length, colour='black'):
    """Draws a turtle line of given length and color"""
    pencolor(colour)
    forward(length)

def draw_triangle(sidelength=10, colour='black'):
    """Draws a triangle with given sidelength and colour"""
    for i in range(3): #pylint: disable=W0612
        draw_line(sidelength, colour)
        right(120)
        draw_line(sidelength, colour)
        right(120)
        draw_line(sidelength, colour)

COLOURS = ['green', 'red', 'blue', 'purple', 'yellow']

if __name__ == '__main__':
    # Increase the length of the triangle sides,
    # from 100 to 250 increasing it by 50 each time around.
    for _l in range(100, 250, 50):
        # For each triangle size (set by _l) draw it in one of the colours,
        # put make the pensize smaller each time around, so we can
        # see the colours.
        for _c in COLOURS:
            draw_triangle(_l, _c)
            PENSIZE -= 4
            pensize(PENSIZE)
sleep(10)

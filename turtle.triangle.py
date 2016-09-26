"""Write my name with a turtle"""
#coding: utf-8

from time import sleep
from turtle import * #pylint: disable=W0401,W0614

PENSIZE=60

speed(11)
pensize(PENSIZE)

def draw_line(length, colour='black'):
    """Draws a turtle line of given length and color"""
    pencolor(colour)
    forward(length)

def draw_triangle(sidelength=10, colour='black'):
    """Draws a triangle with gicen sidelength and colour"""
    for i in range(3): #pylint: disable=W0612
        draw_line(sidelength, colour)
        right(120)
        draw_line(sidelength, colour)
        right(120)
        draw_line(sidelength, colour)

COLOURS = ['green', 'red', 'blue', 'purple', 'yellow']

if __name__ == '__main__':
    for _l in range(100, 250, 50):
        for _c in COLOURS:
            draw_triangle(_l, _c)
            PENSIZE -= 4
            pensize(PENSIZE)
sleep(10)

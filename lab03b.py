"""
Program: CS 115 Lab 3b
Author: Soumana Sylla
Description: Using the graphics package, this program will draw a circle.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    for i in range(1, 100, 20):
        center = Point(400, 500)         # create a point to serve as the center of the circle
        radius = 40 + i
        circle = Circle(center, radius)  # create a circle centered at "center" with radius "radius"
        circle.setOutline('green')
        circle.draw(window)              # draw the circle in the window that we created earlier

    window.getMouse()                # wait for the mouse to be clicked in the window
    window.close()                   # close the window after the mouse is clicked in the window


main()

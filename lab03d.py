"""
Program: CS 115 Lab 3 Part D
Author: Soumana Sylla
Description: Using the graphics package, this program will draw a number of
             circles using a for-loop.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    x = 100
    y = 100
    user_circle_amount = int(input("Enter the amount of circles you want: "))
    user_radius = int(input("Enter the size of the radius: "))
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('red')
        circle.draw(window)

        y = y + 2 * user_radius

    window.getMouse()
    window.close()


main()

"""
Program: CS 115 Lab 3 Part E
Author: Soumana Sylla
Description: Using the graphics package, this program will prompt the user for an amount of circles
and radius, then draw a square of circles with diagonal circles inside.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    user_circle_amount = int(input("Enter the amount of circles you want: "))
    user_radius = int(input("Enter the size of the radius: "))


    x = user_radius + 5
    y = user_radius + 5
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('red')
        circle.draw(window)

        y = y + 2 * user_radius


    x = user_radius + 5
    y = user_radius + 5
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('red')
        circle.draw(window)

        x = x + 2 * user_radius


    x = user_radius + 5
    y = user_circle_amount * (user_radius * 2) - user_radius + 5
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('red')
        circle.draw(window)

        x = x + 2 * user_radius


    x = user_circle_amount * (user_radius * 2) - user_radius + 5
    y = user_radius + 5
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('red')
        circle.draw(window)

        y = y + 2 * user_radius


    x = user_radius + 5
    y = user_radius + 5
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('blue')
        circle.draw(window)

        y = y + 2 * user_radius
        x = x + 2 * user_radius


    x = user_circle_amount * (user_radius * 2) - user_radius + 5
    y = user_radius + 5
    for i in range(user_circle_amount):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, user_radius)
        circle.setOutline('blue')
        circle.draw(window)

        y = y + 2 * user_radius
        x = x - 2 * user_radius

    window.getMouse()
    window.close()


main()
"""
    Program: CS 115 Lab 4b_1
    Author: Soumana Sylla
    Description: This program draws a few rectangles and fills them.
"""
from graphics import *
from random import seed, randint
from time import clock


def random_color():
    # Don't worry about the internal details of this function.
    colors = ['blue', 'blue2', 'blue3',
              'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3',
              'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3',
              'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3',
              'pink', 'pink1', 'pink2', 'pink3']

    return colors[randint(0, len(colors)-1)]


def main():
    seed()  # Initialize random number generator

    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 60
    num_rows = int(input('Number of rows: '))  # commented out for now
    num_columns = int(input('Number of columns: '))

    window = GraphWin('Lab 4B', 800, 800)



    for r in range(num_rows):
        y = top_left_y + r * height



        for c in range(num_columns):
            x = top_left_x + c * width

            top_left_point = Point(x, y)
            bottom_right_point = Point(x + width, y + height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
            enclosing_rectangle.setFill(random_color())
            enclosing_rectangle.draw(window)


    window.getMouse()
    window.close()

main()

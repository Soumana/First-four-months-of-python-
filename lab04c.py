"""
    Program: CS 115 Lab04c.py
    Author: Soumana Sylla
    Description: This program prompts the user for an amount of rows and columns and
    draws rectangles and fills them. Then, accepts the user's mouse clicks and determines where they occur.
"""
from graphics import *
from random import seed, randint
from time import clock


def random_color():

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
    num_rows = int(input('Number of rows: '))
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



    for i in range(10):
        c_point = window.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
        row =  y_c_point - top_left_y
        column = x_c_point - top_left_x
        final_row = row // height
        final_column = column // height



        if final_row >= 0 and final_row <= (num_rows - 1) and final_column >= 0 and final_column <= (num_columns - 1):
            print("The click at", (x_c_point, y_c_point), "is in row", str(int(final_row + 1)) + ",", "column", str(int(final_column + 1)) + '.')

        else:
            print("The click at", (x_c_point, y_c_point), "is outside of the grid.")






    window.getMouse()
    window.close()

main()


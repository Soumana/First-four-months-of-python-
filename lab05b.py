"""
Program: CS 115 Lab 5b
Author: Your name
Description: This program draws a line graph.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("points-test.txt", "r")
    num_points = int(pointsfile.readline())

    # ---- Draw a line between the first and second points
    x = 20  # see note above
    first_y = int(pointsfile.readline())   # get the first y-coordinate
    first_point = Point(x, window_height - first_y)  # see note above

    second_y = int(pointsfile.readline())  # get the second y-coordinate
    x = x + 10
    second_point = Point(x, window_height - second_y)

    # Draw a line between the first two points
    line = Line(first_point, second_point)
    line.setOutline('orange')
    line.draw(window)

    # Draw a circle centered at the first point
    circle = Circle(first_point, 1)
    circle.draw(window)

    #### Line A (for writeup)

    # ---- Draw a line between the second and third points
    first_point = second_point    # the first point of the second line
    second_y = int(pointsfile.readline())  # read the third point
    x = x + 10
    second_point = Point(x, window_height - second_y)

    # Draw the next line
    line = Line(first_point, second_point)
    line.setOutline('orange')
    line.draw(window)

    # Draw the second point
    circle = Circle(first_point, 1)
    circle.draw(window)

    #### Line B (for writeup)

    # ---- Draw a line between the third and fourth points
    first_point = second_point
    second_y = int(pointsfile.readline())  # read the third point
    x = x + 10
    second_point = Point(x, window_height - second_y)

    line = Line(first_point, second_point)
    line.setOutline('orange')
    line.draw(window)

    # Draw the third point
    circle = Circle(first_point, 1)
    circle.draw(window)

    # Draw the fourth point
    circle = Circle(second_point, 1)
    circle.draw(window)

    #### Line C (for writeup)

    window.getMouse()
    window.close()

main()
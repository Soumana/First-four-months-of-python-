"""
Program: CS 115 Lab 2
Author: Soumana Sylla
Description: This program will compute the area of a square, the area of a circle,
the volume of a cube, the volume of a sphere, and the area of an equilateral traingle, given a length.
"""

import math

def main():
    # Get the side length
    length = float(input('Enter a numeric value: '))

    # Compute the area of the square
    square_area = length * length
    circle_area = math.pi * length**2
    volume_cube = length**3
    volume_sphere = 4/3 * math.pi * length**3
    area_equilateral_traingle = length**2 * (math.sqrt(3)) / 4

    print("The area of a square with side length ", length,
          " is ", square_area, ".", sep="")

    print("The area of a circle with radius length ", length,
          " is ", circle_area, ".", sep="")

    print("The volume of a cube with edge length ", length,
          " is ", volume_cube, ".", sep="")

    print("The volume of a sphere with radius length ", length,
          " is ", volume_sphere, ".", sep="")

    print("The area of an equilateral triangle with side ", length,
          " is ", area_equilateral_traingle, ".", sep="")






main()


"""
Program: CS 115 Lab 8c
Author: Soumana Sylla
Description: This program computes geometric quantities.
"""
import sys
import math


def get_numeric_val():
    """
    Ask the user for a number
    Exit if the user does not supply a positive value.
    Otherwise, return the value they entered
    """

    num = float(input('Enter a positive numeric value: '))
    if num <= 0:
        sys.exit('Error: that number was not positive.')
    return num


def get_menu_choice():
    """ Print the menu and return the user's selection """
    print('would you like to')
    print('a. Calculate the area of a square?')
    print('b. Calculate the area of a circle?')
    print('c. Calculate the volume of a cube?')
    print('d. Calculate the volume of a sphere?')
    print('e. Calculate the area of an equilateral triangle?')
    print('q. Quit?')
    print()

    user_letter = input('Enter a letter: ')
    user_choice = user_letter.lower()

    return user_choice





def compute_square_area(side):
    """
    Compute and return the area of a square.
    Parameter: side length of the square
    """
    square_area = side * side
    return square_area



def compute_circle_area(radius):
    """
    Compute and return the area of a circle.
    Parameter: radius of the circle
    """
    area = math.pi * radius**2
    return area



def compute_cube_volume(edge):
    """
    Compute and return the volume of a cube.
    Parameter: edge length of the cube
    """
    volume = edge**3
    return volume

def compute_sphere_volume(radius):
    '''
    Compute and return the volume of a sphere.
    Parameter: radius
    '''

    volume = 4 / 3 * math.pi * radius**3
    return volume

def compute_tri_are(side):
    '''
    Compute and return the area of an equilateral triangle
    Parameter side:
    '''
    area = side**2 * (math.sqrt(3)) / 4
    return area


def main():

    menu_choice = get_menu_choice()  # Get the user's first choice

    while menu_choice != 'q':
        user_num = get_numeric_val()  # Get the side length (etc.)

        if menu_choice == 'a':
            print('The area of a square with side length ',
                  user_num, ' is ', round(compute_square_area(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'b':
            print('The area of a circle with radius length ',
                  user_num, ' is ', round(compute_circle_area(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'c':
            print('The volume of a cube with edge length ',
                  user_num, ' is ', round(compute_cube_volume(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'd':
            print('The volume of a sphere with radius length ',
                  user_num, ' is ', round(compute_sphere_volume(user_num), 5),
                  '.', sep="")
        else:
            menu_choice == 'e'
            print('The area of an equilateral triangle with side length ',
                  user_num, ' is ', round(compute_tri_are(user_num), 5),
                  '.', sep="")

        menu_choice = get_menu_choice()  # Get user's next choice


main()
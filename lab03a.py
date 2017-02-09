"""
Program: CS 115 Lab 3a
Author: Soumana Sylla
Description: This program prompts the user to enter five integers then prints the sum and mean.
"""


def main():
    sum = 0

    for i in range(1, 6):
        user_integer = int(input("Enter an integer: "))
        sum = sum + user_integer

    print('The total is:', sum)
    print('The mean is:', sum / 5)


main()


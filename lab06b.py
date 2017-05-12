"""
Program: CS 115 Lab 6b
Author: Your name
Description: This program will read a positive integer and
 find the largest power of two that is less than or equal to it.
"""


def main():
    i_num = eval(input("Enter a number: "))
    n = 1
    two_to_n = 2 ** n


    while two_to_n < i_num:
        n = n + 1
        two_to_n = two_to_n * 2

    if two_to_n > i_num:
        n = n - 1
        two_to_n = two_to_n / 2

    print('2**' + str(n))


main()

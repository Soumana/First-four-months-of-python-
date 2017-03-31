"""
Program: CS 115 Lab 6c
Author: Soumana Sylla
Description: This program will read a positive integer and
 express it as the sum of powers of 2.
"""


def main():

    i_num = int(input("Enter a number: "))



    while i_num > 0:
        n = 0
        two_to_n = 2**n
        while two_to_n < i_num:
            n = n + 1
            two_to_n = 2**n

        if two_to_n > i_num:
            n = n - 1
            two_to_n = 2**n


        i_num = i_num - two_to_n
        if i_num > 0:
            print("2**" + str(n), "+", end=" ")
        else:
            print("2**" + str(n))






main()
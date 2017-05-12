"""
Program: CS 115 Lab 7a
Author: Soumana Sylla
Description: This program finds $1.00 words.
"""


def main():

    user_word = input("Enter a word: ")
    user_word = user_word.lower()

    while user_word != 'quit':
        total = 0
        for i in user_word:
            numbers = ord(i) - 96
            total += numbers
        total = total * .01
        print("Your word is worth ${0:.2f}".format(total) + ".")
        if total == 1.0:
            print("Congratulations!")






        new_user_word = input("Enter a word: ")
        new_user_word = new_user_word.lower()
        user_word = new_user_word




main()

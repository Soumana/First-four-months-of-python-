"""
Program: CS 115 Lab 7b
Author: Soumana Sylla
Description: This program Computes the average word length of the user's text.
"""


def main():
    user_text = input("Enter some text: ")
    total_words = 0
    total_characters = 0


    while user_text != "":
        user_text_list = user_text.split()
        total_words += len(user_text_list)
        for i in user_text_list:
            total_characters += len(i)
        user_text = input("Enter some text: ")

    try:
        average_word_length = total_characters / total_words
        print("The average word length is:", round(average_word_length, 5))

    except ZeroDivisionError:
        print("You did not enter any words.")




main()


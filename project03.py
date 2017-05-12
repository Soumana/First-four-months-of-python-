"""
Author: Soumana Sylla
Description: This program creates a game called Ghost Word, modeled after Hangman using the graphics package.
A random word is selected from a file and hidden. The player tries to fill in the letters of the word.
The game is won when the word is entirely guessed, or when the player reaches 6 incorrect guesses.
The player's current number of incorrect guesses is illustrated by drawing a figure
that slowly disappears with each incorrect guess;
when the figure has entirely disappeared, the player loses.
"""

from ghost_support import *
import sys
import string


def readfile(filename):
    """
        Reads the entire contents of a file into a single string using
        the read() method.

        Parameter: the name of the file to read (as a string)
        Returns: the text in the file as a large, possibly multi-line, string
        """

    infile = open(filename, "r")  # open file for reading

    # Use Python's file read function to read the file contents
    filetext = infile.read().splitlines()

    infile.close()  # close the file

    return filetext  # the text of the file, as a single string


def create_board():
    """
    Generates the game window.

    :param: None
    :return: a graphics window with a stick_man drawing
    """

    win = GraphWin('Ghost Game', WINSIZE, WINSIZE)
    win.setBackground('red')

    head = Circle(Point(300, 120), 60)
    head.setFill('black')
    head.draw(win)

    body = Line(Point(300, 181), Point(300, 450))
    body.setFill('black')
    body.setWidth(8)
    body.draw(win)

    left_arm = Line(Point(300, 300), Point(200, 145))
    left_arm.setFill('black')
    left_arm.setWidth(8)
    left_arm.draw(win)

    right_arm = Line(Point(300, 300), Point(400, 145))
    right_arm.setFill('black')
    right_arm.setWidth(8)
    right_arm.draw(win)

    left_leg = Line(Point(300, 447), Point(200, 550))
    left_leg.setFill('black')
    left_leg.setWidth(8)
    left_leg.draw(win)

    right_leg = Line(Point(300, 447), Point(400, 550))
    right_leg.setFill('black')
    right_leg.setWidth(8)
    right_leg.draw(win)

    parts = [left_leg, right_leg, left_arm, right_arm, body, head]

    return win, parts


def play(updated_dictionary, win, parts):
    """
    Allows the game to be played, generates a secret word,
    checks if the user's guess is in the secret word.

    :param updated_dictionary:
    :param win:
    :param parts:
    :return: None
    """
    secret_word = []
    incorrect_guesses = []
    correct_guesses = []
    match = 0
    remaining_guesses = 6

    word = choose_word(updated_dictionary)

    for char in word:
        secret_word.append('_')
    print('\tHint: ', end='')
    for i in secret_word:
        print(i, end=' ')

    print()
    print('\tThe following letter(s) are not in the secret word...', incorrect_guesses)
    print()

    while True:
        print('Remaining guesses left:', remaining_guesses)
        print()
        user_guess = input('Guess: ')

        while True:
            if len(user_guess) > 1 or user_guess.isalpha() == False: # Guess must be one character and alphabetical
                print('You entered', "'" + user_guess.upper() + "'", 'That is not a valid guess.')
                print()
                user_guess = input('Guess again: ')

            elif user_guess.upper() in incorrect_guesses or user_guess.upper() in correct_guesses:
                    print('You already guessed', user_guess.upper())
                    print()
                    user_guess = input('Guess: ')
            else:
                break

        if user_guess.lower() not in word.lower(): # Inform the user if the guess was incorrect.
            print('Sorry,', user_guess.upper(), 'is not in the secret word.')
            remaining_guesses += -1

        if user_guess.lower() in word.lower():
            print('Good job,', user_guess.upper(), 'is in the secret word.')  # Inform the user if the guess was correct
        print()

        for i in range(len(word)):
            if user_guess.lower() == word[i].lower():  # Checks if user's guess is in the secret word.
                secret_word[i] = user_guess.upper()
                match += 1

        if len(secret_word) == match:  # If the user has guessed the secret word, they won
            print('Congrats, You Won!')
            print()
            print('\tWord:', word.upper())
            print()
            user_answer = input('Would you like to play a game of Ghost Word? (Enter Yes or No) ')
            print()
            while user_answer.lower() != 'yes' and user_answer.lower() != 'no':
                print('Sorry, that is not a valid input')
                user_answer = input('Would you like to play a game of Ghost Word? (Enter Yes or No) ')
                print()
            if user_answer.lower() == 'yes':
                win.close()
                win, parts = create_board()
                play(updated_dictionary, win, parts)

            if user_answer.lower() == 'no':
                print('Goodbye, have a nice day.')
                sys.exit()
            return

        if user_guess.upper() not in word.upper():  # If incorrect guess, a body part from the stick_man gets removed
            incorrect_guesses.append(user_guess.upper())
            parts[0].undraw()
            parts = parts[1:]
        else:
            correct_guesses.append(user_guess.upper())

        print('\tHint: ', end='')

        for i in secret_word:
            print(i, end=' ')
        print()

        print('\tThe following letter(s) are not in the secret word...', incorrect_guesses)
        print()

        while len(incorrect_guesses) == 6:  # With six incorrect guesses, the game is over
            print('Game Over! You used up all of your six guesses.')
            print()
            print('\tThe secret word was:', word.upper())
            print()

            user_answer = input('Would you like to play a game of Ghost Word? (Enter Yes or No) ')
            print()
            while user_answer.lower() != 'yes' and user_answer.lower() != 'no':
                print('Sorry, that is not a valid input')
                user_answer = input('Would you like to play a game of Ghost Word? (Enter Yes or No) ')
                print()
            if user_answer.lower() == 'yes':
                win.close()
                win, parts = create_board()
                play(updated_dictionary, win, parts)

            if user_answer.lower() == 'no':
                print('Goodbye, have a good day.')
                sys.exit()
            return


def main():
    """
    Prompts the user for a file that contains a list of words,
    if any words have duplicates or contain non-alphabetical letters,
    they are removed. Then information is provided about the file.
    :parameter: None
    :return: None
    """
    filename = input('Enter a dictionary filename: ')
    dictionary = readfile(filename)

    updated_dictionary = []
    for word in dictionary:
        if word.lower().isalpha() == True:
            updated_dictionary.append(word.lower())
        if len(updated_dictionary) == 0:
            print('Error: There are no usable alphabetical words.')
            sys.exit(-1)

    updated_dictionary = list(set(updated_dictionary))

    print()
    print('Here is some info about the file.')

    print('\tSize of dictionary:', len(updated_dictionary))
    print('\tFrequency of each letter:')

    for letter in string.ascii_uppercase:
        total = 0
        for word in updated_dictionary:
            word = word.upper()
            total += word.count(letter)
        print('\t\t', letter + ':', total)

    print()
    user_answer = input('Would you like to play a game of Ghost Word? (Enter Yes or No) ')
    print()
    while user_answer.lower() != 'yes' and user_answer.lower() != 'no':
        print('Sorry, that is not a valid input')
        user_answer = input('Would you like to play a game of Ghost Word? (Enter Yes or No) ')
        print()

    if user_answer.lower() == 'yes':
        win, parts = create_board()
        play(updated_dictionary, win, parts)

    if user_answer.lower() == 'no':
        print('Goodbye, have a nice day.')
        sys.exit()

main()

"""
Program: CS 115 Lab 10
Author: Soumana Sylla
Description: This program will open a file and then search its contents
             using linear and binary search.
"""


def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """

    infile = open(filename, "r")  # open file for reading

    # Use Python's file read function to read the file contents
    filetext = infile.read()

    infile.close()  # close the file

    return filetext  # the text of the file, as a single string


def print_list(list_to_print):
    """
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    """

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")


def linear_search(search_list, value_to_find):
    """
    Uses a hand-coded linear search to find the position of an item in a list

    Parameters: the list; the item to search for
    Returns: the position of the item in the list
        (or None if it is not in the list)
    """
    for i in range(len(search_list)):
        if search_list[i] == value_to_find:
            return i







def main():
    """ Read and print a file's contents. """
    filename = input('Name of input file: ')
    opened_file = open(filename)
    file_contents = opened_file.read().splitlines()
    #print('Number of lines in file:', len(file_contents))
    print_list(file_contents)

    user_city = input('Enter the name of a city: ')
    while user_city.lower() != 'quit':
        position = linear_search(file_contents, user_city)
        print('The position of', user_city, 'is:')
        print('Linear search:', position)
        user_city = input('Enter the name of a city: ')




main()

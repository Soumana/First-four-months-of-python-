"""
Program: CS 115 Lab 14
Author: Soumana Sylla
Description: This program will open a file and then returns the index where the value to find lies using recursion
binary search.
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
    filetext = infile.read().splitlines()

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



def binary_search_recursive(search_list, value_to_find, first, last):
    '''Uses recursion to return the index from where the value to find lies'''
    print('Binary searching between', first, 'and', last)
    if first > last:
        return None
    middle = (first + last) // 2
    if value_to_find == search_list[middle]:
        return middle
    elif value_to_find > search_list[middle]:
        first = middle + 1

    else:
        last = middle - 1
    return binary_search_recursive(search_list, value_to_find, first, last)


def binary_search(search_list, value_to_find):
    """
    Uses a binary search function to find the position of an item in a list
    Parameters: the list; the item to search for
    Returns: the position of the item in the list
             (or None if it is not in the list)
    """
    counter = 0
    first = 0
    last = len(search_list) - 1
    return binary_search_recursive(search_list, value_to_find, first, last)
    # while first <= last:
    #     middle = (first + last) // 2
    #     counter += 1
    #     if value_to_find == search_list[middle]:
    #         print('**Binary search iterations:', counter)
    #         return middle
    #
    #     elif value_to_find > search_list[middle]:
    #         first = middle + 1
    #
    #     else:
    #         last = middle - 1
    #
    # print('**Binary search iterations:', counter)
    # return None








def main():
    """ Read and print a file's contents. """
    filename = input('Name of input file: ')
    file_contents = readfile(filename)
    print()
    print('The original list of cities is:')
    print_list(file_contents)
    print()
    print('After sorting, the new list is:')
    file_contents.sort()
    print_list(file_contents)
    print()

    user_city = input('Enter the name of a city: ')
    while user_city.lower() != 'quit':
        #print('Linear search:', linear_search(file_contents, user_city))
        #print('Binary search:', binary_search(file_contents, user_city))
        print('The position of', user_city, 'is:', binary_search(file_contents, user_city))
        print()
        user_city = input('Enter the name of a city: ')




main()

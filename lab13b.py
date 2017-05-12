"""
Program: Lab 13
Author: Soumana Sylla
This program defines and test a basic City class. It also defines a __str__ and __lt__ method.
Then, a list of cities with their populations are accepted as input, which then gets sorted from least to greatest
 based on the population.
"""
import sys


class City:
    def __init__(self, city, population):
        self.city = city
        self.population = population


    def __str__(self):
        return str(self.city + ' ' + '(' + 'pop. ' + str(self.population) + ')')

    def __lt__(self, other):
        # Return True if the population of self is less than
        # the population of other and return False otherwise
        if self.population < other.population:
            return True
        else:
            return False

def print_list(list_to_print):
    '''
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    '''

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")


def selection_sort(L):
    '''
    Use the selection sort algorithm to sort a list.
    Parameter: unsorted list
    Sorts the original list that was passed to it -- doesn't return anything.
    '''
    for i in range(len(L) - 1):
        min_index = find_index_of_min(L, i)
        #print('Swapped elements', i, 'and', min_index, '--', L[i], 'and', L[min_index])
        L[i], L[min_index] = L[min_index], L[i]


def find_index_of_min(L, start_index):
    """
    Parameter: a list L
    Returns: finds the index of the minimum element starting at an index specified.
        (returns None if the list is empty or
        if the list does not have enough elements to start at start_index)
    """

    if len(L) <= start_index:
        return None
    if len(L) - 1 == start_index:
        return start_index
    min_index = start_index
    for i in range(min_index + 1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def readfile(filename):

    infile = open(filename, "r")  # open file for reading

    # Use Python's file read function to read the file contents
    filetext = infile.read().splitlines()

    infile.close()  # close the file

    return filetext  # the text of the file, as a single string



def main():

    user_file = input('Enter the name of a file: ')
    file_list = readfile(user_file)

    list_of_cities = []
    for i in range(0, len(file_list) , 2):
        object = City(file_list[i], int(file_list[i+1]))
        list_of_cities.append(object)



    print('The original list of cities is:')
    print_list(list_of_cities)
    print()

    print('The new list of cities is:')
    selection_sort(list_of_cities)
    print_list(list_of_cities)





main()

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


def main():
    filename = input('Enter a file name: ')
    print()
    list_to_print = readfile(filename)
    print('The original list of cities is: ')
    print_list(list_to_print)

    print(find_index_of_min([]))
    print(find_index_of_min([3, 2, 1, 0]))
    print(find_index_of_min(['A', 'Z', 'Y', 'B']))
    print(find_index_of_min(['B', 'A', 'Z', 'Y']))

main()
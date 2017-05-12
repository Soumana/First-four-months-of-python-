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


def selection_sort(L):
    '''
    Use the selection sort algorithm to sort a list.
    Parameter: unsorted list
    Sorts the original list that was passed to it -- doesn't return anything.
    '''
    for i in range(len(L) - 1):
        min_index = find_index_of_min(L, i)
        print('Swapped elements', i, 'and', min_index, '--', L[i], 'and', L[min_index])
        L[i], L[min_index] = L[min_index], L[i]


def merge(L, start_index, sublist_size):
    """
    Merge two sublists of a list L

    Parameters:
    L - the list
    start_index - the index of the first element to be merged
    sublist_size - the size of the chunks to be merged

    Left chunk: L[start_index] to L[start_index + sublist_size - 1]
    Right chunk: L[start_index + sublist_size] to L[start_index + 2 * sublist_size - 1]
    """

    index_left = start_index
    left_stop_index = start_index + sublist_size
    index_right = start_index + sublist_size
    right_stop_index = min(start_index + 2 * sublist_size,
                           len(L))

    print('Merging sublists:', L[index_left:left_stop_index], 'and',
          L[index_right:right_stop_index]);

    L_tmp = []

    while (index_left < left_stop_index and
           index_right < right_stop_index):
        if L[index_left] < L[index_right]:
           L_tmp.append(L[index_left])
           index_left += 1
        else:
           L_tmp.append(L[index_right])
           index_right += 1

    if index_left < left_stop_index:
           L_tmp.extend(L[index_left : left_stop_index])
    if index_right < right_stop_index:
           L_tmp.extend(L[index_right : right_stop_index])

    L[start_index : right_stop_index] = L_tmp
    print('Merged sublist:', L_tmp, '\n')



def merge_sort(L):
    """
    Sort a list L using the merge sort algorithm.

    (Starter code doesn't fully sort the list.)
    """

    chunksize = 1  # Start by dividing the list into N sub-lists of 1 element each

    while chunksize < len(L):
        print("\n*** Sorting sublists of size", chunksize)

    # Divide the list into pairs of chunks
        left_start_index = 0  # Start of left chunk in each pair

    # While we still have chunks to merge
        while left_start_index + chunksize < len(L):
            merge(L, left_start_index, chunksize)

        # Move to next pair of chunks
            left_start_index += 2 * chunksize
        chunksize = chunksize * 2

        print('List is now', L)





def main():
    filename = input('Enter a file name: ')
    user_selection = input('Type S for selection sort and M for merge sort: ')
    print()
    list_to_print = readfile(filename)
    print('The original list of cities is: ')
    print_list(list_to_print)
    #user_selection = input('Type S for selection sort and M for merge sort: ')
    print()
    if user_selection.lower() == 's':
        selection_sort(list_to_print)
        print()
        print('The new list of cities is: ')
        print_list(list_to_print)


    if user_selection.lower() == 'm':
        merge_sort(list_to_print)
        print('The new list of cities is: ')
        print_list(list_to_print)
    #print()

    # print('The new list of cities is: ')
    # print_list(list_to_print)





main()

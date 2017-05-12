"""
Program: CS 115 Lab 9a
Author: Soumana Sylla
Description: This program will create a magic square
   whose size is specified by the user, then prompt the user for a text file
   and determines if the text file is or is not a magic square.


"""
import sys

def create_list(rows, cols):
    """
    Creates a two-dimensional array.

    Parameters: the numbers of rows and columns

    Returns: a 2D array with all values set to zero
    """

    two_d = []  # create an empty list
    for i in range(rows):
        two_d.append([])  # append an empty list to two_d
        for j in range(cols):
            two_d[i].append(0)   # two_d[i] is the empty list that we just created.
                                 # here, we are adding elements to it.
    return two_d


def rjust_by_n(number, n):
    """
    Return a string of length "n" with number right-justified in it.

    Parameters:
    number: an value with n or fewer digits
    n: a positive integer value

    Returns: a string of length n with a number right-justified in it.
    """
    return str(number).rjust(n)


def print_list(numbers):
    """
    Print a 1D list of numbers, where each number is right-justified
    """
    for i in range(len(numbers)):
        print( rjust_by_n(numbers[i], 4), end='')
    print()


def print_2d_list(two_d_list):
    """
    Print a 2-dimensional list
    """
    for i in range(len(two_d_list)):
        print_list(two_d_list[i])


def build_magic_square(square):
    """
    Create a magic square in "square"

    Parameter:
    square: a two dimensional array whose number of rows and columns are equal
            and len(square) is an odd number.

    Modifies "square" but doesn't return anything.
    """
    magic_value = 1
    square_size = len(square)
    row = 0
    col = square_size // 2
    square_size_squared = square_size * square_size
    while magic_value <= square_size_squared:
        square[row][col] = magic_value
        row -= 1
        col += 1
        if row < 0 and col > square_size - 1:
            row += 2
            col -= 1
        elif row < 0:
            row = square_size - 1
        elif col > square_size - 1:
            col = 0
        elif square[row][col] != 0:
            row += 2
            col -= 1

        magic_value += 1


def sum_row_values(matrix, row_number):
    """
    Sums the values of all entries in the row given by "row_number"

    Parameters:
    matrix: a two dimensional (square) list
    row_number: an integer value in the range 0 and len(matrix)-1

    Returns: the sum of all values of the row indicated by "row_number"
    """

    full_row = matrix[row_number]
    return sum(full_row)


def sum_col_values(matrix, col_number):
    """
    Sums the values of all entries in the column given by "col_number"

    matrix: a two dimensional (square) array
    col_number: an integer value in the range 0 and len(matrix)-1

    Returns the sum of all values in the column indicated by "col_number"
    """
    total = []
    for i in range(len(matrix)):
        number = matrix[i][col_number]
        total.append(number)
    return sum(total)




def sum_top_left_bottom_right_diagonal(matrix):
    """
    Calculates the sum of the values at matrix[0][0], matrix[1][1], etc.

    matrix: a two dimensional (square) matrix
    return value: the sum of values of the top-left to bottom-right
                  diagonal
    """
    total = []
    for i in range(len(matrix)):
        number = matrix[i][i]
        total.append(number)
    return sum(total)



def sum_top_right_bottom_left_diagonal(matrix):
    """
    Calculates the sum of the values at matrix[0][len(matrix)-1], matrix[1][len(matrix)-2], etc.

    matrix: a two dimensional (square) matrix
    return value: the sum of values of the top-right to bottom-left
                  diagonal
    """

    total = []
    for i in range(len(matrix)):
        number = matrix[i][len(matrix) - 1 - i]
        total.append(number)
    return sum(total)


def is_magic_square(matrix):
    """
    returns True if the two dimensional array that "matrix" points to is a
    magic square. Otherwise, it returns False.

    matrix: a two dimensional (square) array.
    return value: True or False.
    """

    # calculate the sum of the values of the top-left to
    # bottom-right diagonal. Call it tlbr_sum.
    tlbr_sum = sum_top_left_bottom_right_diagonal(matrix)

    # calculate the sum of the values of the top-right to
    # bottom-left diagonal. Call it trbl_sum.
    trbl_sum = sum_top_right_bottom_left_diagonal(matrix)

    # if tlbr_sum is not equal to trbl_sum, return False. Otherwise,
    # proceed.
    if tlbr_sum != trbl_sum:
        print('The above square is NOT a magic square.')
        return False

    # calculate the sum of each row of the matrix and compare it
    # with tlbr_sum. If the two sums are not equal, return False.
    # Otherwise, proceed.

    for row_number in range(len(matrix)):
        sum_of_row_0 = sum_row_values(matrix, row_number)
        if sum_of_row_0 != tlbr_sum:
            print('The above square is NOT a magic square.')
            return False




    # calculate the sum of each column of the matrix and compare it
    # with tlbr_sum. If the two sums are not equal, return False.
    # Otherwise, proceed.

    for col_number in range(len(matrix)):
        number = sum_col_values(matrix, col_number)
        if tlbr_sum != number:
            print('The above square is NOT a magic square.')
            return False

    else:
        print('The above square is a magic square.')
        return True


def read_magic_square(filename):
            """
            Read values from a file into a 2D list

            Parameter:
            filename: the name of the file

            Returns a 2D list of integer values read.
            """

            infile = open(filename, "rt")
            square = []  # start with an empty list

            for line in infile:  # read text from file
                row = []
                numbers = line.split()

                # Loop through the list of numbers.
                # Append each number to the row.
                for num in numbers:
                    row.append(int(num))

                if len(row) > 0:  # Don't count blank lines
                    square.append(row)  # Append the row to the 2D list

            return square


def main():
    square_size = int(input('Enter an odd integer to build a magic square: '))
    if square_size % 2 == 0:
        sys.exit(print(square_size, 'is not an odd integer. Terminating...'))
    else:
        print()
        two_D_list = create_list(square_size, square_size)
        build_magic_square(two_D_list)
        print_2d_list(two_D_list)
        print()
        is_magic_square(two_D_list)
        print()
        user_file = input('Enter the name of a file containing a matrix of numbers: ')
        print()
        user_magic_square = read_magic_square(user_file)
        create_list(len(user_magic_square), len(user_magic_square))
        print_2d_list(user_magic_square)
        print()
        is_magic_square(user_magic_square)



main()



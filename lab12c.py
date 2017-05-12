"""
Program: Lab 12
Author: Soumana
This program will read in a list of students and grades from a text
 file, calculate the students' averages, and print the list of students.
"""


def file(filename):
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


class Student:
    """ A class that holds the data for an individual student """
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def get_average(self):
        """ Return the average grade """

        if self.scores == []:
            return None
        else:
            all_scores = []
            for score in self.scores:
                all_scores.append(score)
            average = sum(all_scores) / len(self.scores)
            return round(average, 5)





    def print(self):
        """ Print the student info in the following format:
           Name (12 characters), grades(separated by tabs), average (formatted
           to 5 decimals """

        # Right now, just prints the student name padded out to 12 characters
        string_to_print = self.name.ljust(12)

        # Convert list of integers to strings for printing purposes
        # There are shorter ways to do this, but this is the clearest.
        for score in self.scores:
            string_to_print += '\t' + str(score)

        string_to_print += '\t' + str(self.get_average())

        print(string_to_print)



# A tester program
def main():
    total_average = []
    studentlines = file("students.txt")
    for line in studentlines:
        seperate_lines = line.split()
        if len(seperate_lines) == 0:
            break
        else:
            name = []
            scores = []
            name.append(seperate_lines[0])
            for i in seperate_lines[1:]:
                number = int(i)
                scores.append(number)
        Individuals = Student(name[0], scores)
        Individuals.print()

        avg = Individuals.get_average()
        total_average.append(avg)
    print()
    overall_average = (sum(total_average) / len(total_average))
    print('Overall Average:',round(overall_average, 5))



main()

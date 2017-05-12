"""
Program: Lab 13
Author: Soumana Sylla
Define and test a basic City class.
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



def main():
    tokyo = City('Tokyo', 13189000)
    mexico_city = City('Mexico City', 8857188)



    print(tokyo)
    print(mexico_city)

    print()
    # Print whichever city is larger
    print('The larger city is:')
    if mexico_city < tokyo:
        print(tokyo)
    else:
        print(mexico_city)
main()

#usr/bin/env python3

#!/usr/bin/env python3

"""This script loads in data and searches for oaks in it, while being robust to typos"""

__appname__ = '[OAKS DEBUGME]'
__author__ = 'Booming bonobos'
__version__ = '0.0.1'

import csv
import sys


# Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus'
    >>> is_an_oak('Quercus cirrus')
    True
    >>> is_an_oak('quercus cirrus')
    True
    >>> is_an_oak('Quercuss cirrus')
    False
    >>> is_an_oak(' Quercus cirrus')
    True
    >>> is_an_oak('Fagus sylvatica')
    False
    """

    return name.lower().strip().startswith('quercus ')


def main(argv):
    """Writes only the oak species to a new csv, from a file of tree species."""
    f = open('../data/TestOaksData.csv', 'r')
    f_lines = f.readlines()[1:]  # start reading from the second line - need to add an if statement to only do this if there is a header in the first place
    g = open('../data/JustOaksData.csv', 'w')
    taxa = csv.reader(f_lines)
    csvwrite = csv.writer(g)
    for row in taxa:
        print(row)
        print("The genus is: ")
        print(row[0] + '\n')
        if is_an_oak(" ".join(row)):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])

    return 0


if (__name__ == "__main__"):
    import doctest

    doctest.testmod()
    status = main(sys.argv)
    sys.exit(status)
~                       

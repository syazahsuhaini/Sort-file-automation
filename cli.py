# parse;
# to separate a sentence into grammatical parts, such as subject, verb, etc.
# to examine computer data and change it into a form that can be easily read or understood

import argparse

from sort import *

"""
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Sort and move files based on its extensions.')

    parser.add_argument('input', help='Input file to process.')

    sort_files()
"""

parser = argparse.ArgumentParser(description ='Process some integers.')
parser.add_argument('integers', metavar ='N', 
                    type = int, nargs ='+',
                    help ='an integer for the accumulator')

parser.add_argument(dest ='accumulate', 
                    action ='store_const',
                    const = sum, 
                    help ='sum the integers')

args = parser.parse_args()
print(args.accumulate(args.integers))
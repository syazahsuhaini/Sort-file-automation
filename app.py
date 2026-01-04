# parse;
# to separate a sentence into grammatical parts, such as subject, verb, etc.
# to examine computer data and change it into a form that can be easily read or understood

import argparse

from sort import *
from rename import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='File automation tool',
        description='Sort files and rename timesheets.',
        epilog='by Syaza')

    parser.add_argument('--sort',   # -- indicate as flag
                        action='store_true',    # if flag is in the argument, return TRUE for args.sort
                        help='Sort files into folders based on their extensions and timesheet.')
    
    parser.add_argument('--rename',   # -- indicate as flag
                        action='store_true',    # if flag is in the argument, return TRUE for args.sort
                        help='Rename timesheets.')
    
    parser.add_argument('month_year',   # -- indicate as flag
                        nargs='*',    # neeed 2 arguments
                        default=None,
                        help='Month and year to rename the timesheets.')
    
    args = parser.parse_args() # a container that collects the value of the flag

    if args.sort:
        sort_files()

    if args.rename:
        if args.month_year is None or len(args.month_year) != 2:
            print("Error: you must provide month and year for renaming, e.g., 'January 2025'")
        else:
            month, year = args.month_year
            rename_files(month, year)
    
    if not (args.sort or args.rename):
        print("No flags provided. Nothing will run.")
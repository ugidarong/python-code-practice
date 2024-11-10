#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""
import random
import argparse
import csv
from pprint import pprint
from tabulate import tabulate
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args() 
    random.seed(args.seed)
    exercises = read_csv(args.file)
    wod = []
    for name , low, high in random.smaple(exercises, k=args.num):
        reps = random.randint(low,high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((name, reps))
    print(tabulate(wod, headers = ('Exercise', 'Reps')))
# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    exercises = []
    for row in csv.DictReader(fh, delimiter = ','):
        low, high = map(int, row['reps'].split('-'))
        exercises.append((row['exercise'], low, high))

    return exercises
# --------------------------------------------------

# --------------------------------------------------
if __name__ == '__main__':
    main()
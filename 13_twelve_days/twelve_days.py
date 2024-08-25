#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-08-03
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='int',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    
    args =  parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    days = args.num

    #1 서수 모음, 선물 모음
    ordinary = ['first','second','third','fourth','fifth','sixth','seventh',
                'eighth','ninth','tenth','eleventh','twelfth']
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]

    for i in range(0,days):
        print("On the %s day of christmas,"%(ordinary[i]))
        print("My true love gave to me")
        for n in (range(i, -1, -1)):
            print(gifts[n])
      

# --------------------------------------------------
if __name__ == '__main__':
    main()

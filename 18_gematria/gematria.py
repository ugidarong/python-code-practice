#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    list_text=text.split(' ')
    vals = []
    for i in list_text:
        vals.append(list(i))
    
    for x in range(len(vals)):
        for y in range(len(vals[x])):
            vals[x][y] = ord(vals[x][y])
     
    answer = []
    for num in vals:
        answer.append(sum(num))
    
    print(' '.join(map(str,answer)))
            
    
# --------------------------------------------------
if __name__ == '__main__':
    main()

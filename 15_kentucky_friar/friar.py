#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-08-11
Purpose: Rock the Casbah
"""

import argparse
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    text = re.split(r'(\W)', args.text)
    #yYou = re.match(r'([yY])ou', 'you')
    #print(text[0])
    fry(text[0])


def fry(word):
    yYou = re.match(r'([yY])ou', word)
    if yYou:
        print(yYou.group(1) + "'all")
    



def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
if __name__ == '__main__':
    main()

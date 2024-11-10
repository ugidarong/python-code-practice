#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""
import sys
import re
import argparse
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    matches = re.findall('(<([^<>]+)>)', text)
    
    if not matches:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    for placeholder, name in matches:
        article = 'an' if name.lower()[0] in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(f'Give me {article} {name} : ')
        text = re.sub(placeholder, answer, text, count = 1)
    print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()

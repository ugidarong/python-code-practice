#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-07-20
Purpose: Rock the Casbah
"""
import string
import argparse
import random
import os
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)



    args = parser.parse_args()

    if not 0 <=args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    mutations = args.mutations
    text = args.text
    change_text_num = round(len(text) * mutations)
    random_choice = random.sample(range(len(text)),change_text_num)
    
    #체크리스트
    alpah_list = ''.join(sorted(list(string.ascii_letters + string.punctuation)))
    text_list = list(text)
    
    for i in random_choice:
        text_list[i] = random.choice(alpah_list.replace(text_list[i], ''))
    
    print("You said: "+'"'+text+'"')    
    print("I heard : " +'"'+''.join(text_list)+'"')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()

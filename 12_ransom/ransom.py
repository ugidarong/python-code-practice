#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-08-03
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    #1번 조건 바꾸려는 수랑 글자 위치가 같음


    args = get_args()
    random.seed(args.seed)
    text=args.text
    group1 = list(text)
    X = random.randint(0,len(text)-1)
    change_count = random.sample(range(len(text)),X)
    
    for i in range(0,len(group1)):
        if i in change_count:
            if group1[i] == group1[i].upper():
                group1[i] = group1[i].lower()
            else:
                group1[i] = group1[i].upper()
        
    
    #테스트 불통 이유
    #교재랑 다른 함수식으로 사용 2개의 랜덤함수를 사용함으로써 틀린답이 나옴
    #다만 교제 목적과 부합함으로 다음 장으로 넘어감ㄴ
    print("".join(group1))
    

# --------------------------------------------------
if __name__ == '__main__':
    main()

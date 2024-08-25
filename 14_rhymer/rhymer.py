#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-08-03
Purpose: Rock the Casbah
"""

import argparse
import re
import string
import string as s
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word.lower()#받은 단어

    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()#자음그룹
    
   
    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])#자음 규칙

    try:
        split = re.match(f'([{consonants}]+)?([aeiou])(.*)', word).groups()#제일 앞글자 따오기  
        my_split = list(split)    
        if split[0] in prefixes:#앞글자가 자음일 경우
            last = []
            for i in prefixes:
                if i == split[0]:#같은 글자는 생략
                    pass


                else:#다른 글자를 정렬리스트로 모으고 출력
                    my_split[0] = i
                    last.append(''.join(my_split))
            last = sorted(last)
            for k in last:
                print(k)    


        else:#모음으로 시작될 경우
            lastlast = []
            for first in prefixes:
                lastlast.append(str(first + word))
            last_group=sorted(lastlast)
            for t in last_group:
                print(t)


    except:#자음으로만 됬을 경우 출력
        print(f'Cannot rhyme "{args.word}"')






def stemmer():
    pass

def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('','')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('','apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')
# --------------------------------------------------
if __name__ == '__main__':
    main()

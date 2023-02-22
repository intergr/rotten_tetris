from os import system
from random import shuffle
from itertools import zip_longest
from time import time

li = ['.']*200
shapes = ['4', '1n3', 'ss1n3', '2n2', 's2n2', 's1n3', '2ns2']*5
shuffle(shapes)

clear = lambda: system('cls')
show = lambda li:  print('''
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                |{}{}{}{}{}{}{}{}{}{}|
                ﹋﹋﹋﹋﹋﹋
                '''.format(*li))

def main():
    global li, shapes
    lines = 0
    background = li[:]
    prev = []
    start = time()
    retry = 0
    for inf in shapes:
        show(li)
        row, column, down, left, right = (0,)*5
        flag = 0
        while True:
            char = input()
            clear()
            match char:
                case 'w': inf = turn(inf)
                case 'a': left += 1
                case 's': down += 1
                case 'd': right += 1
                case 'r': retry = 1
            if retry: break
            down *= 10
            for shape in inf:
                if shape.isdigit():
                    shape = int(shape)
                    direction = row+column+down+right-left
                    if '▉' not in li[direction:shape+direction]:
                        li[direction:shape+direction] = '▉'*shape
                    else: li = prev[:]; flag = 1; break
                    if len(li) > 200: li = prev[:]; flag = 1; break
                elif shape == 'n':
                    row += 10
                    column = 0
                else:
                    column += 1
            prev = li[:]
            if flag: break
            print(f'Lines: {lines}')
            show(li)
            row, column = (0,)*2
            down //= 10
            li = background[:]
        if retry: break
        if prev == background: break
        prev, temp = remove_lines(prev)
        lines += temp
        background = prev[:]
    end = time()
    return lines, end-start

def turn(shape:str):
    temp = 'n'.join(''.join(i)[::-1].rstrip('s') for i in zip_longest(*\
            ''.join('1'*int(i) if i.isdigit() else i for i in shape).split('n'), fillvalue='\0'))
    res = ''
    count = 0
    for i in temp+'\0':
        if i == '1': count += 1
        elif count: res += str(count) + i; count = 0
        else: res += i
    return res

def remove_lines(li:list):
    li = li[:]
    count = 0
    for i in range(0, 199, 10):
        if li[i:i+10] == ['▉']*10:
            del li[i:i+10]
            li = ['.']*10 + li
            count += 1
    return li, count

if __name__ == '__main__':
    while True:
        lines, time_ = main()
        print(f'{lines} lines cleared, {int(time_//60)}m {time_-(time_//60)*60:.2f}s passed.\nRetry? (y/n)')
        s = input()
        if s in ['n', 'N']: break
        li = ['.']*200
        shuffle(shapes)
#! python3.py
# _*_ coding: UTF-8 _*_

__author__ = 'Michael Liao'

import  sys

def test():
    args = sys.argv
    print('argv___%s',sys.argv)

    if len(args) == 1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello, %s!'%args[1])
    else:
        print('Too many arguments!')


def pow_three():
    fs = []
    for i in range(1, 4):
        def f(i=i):
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = pow_three()
print("f1 = ", f1(), " f2 = ", f2(), " f3 = ", f3())

if __name__ == '__main__':
    test()
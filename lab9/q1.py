#!/usr/bin/env python3

class MyPoint(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

def main():
    r1 = MyPoint(3, 4)
    r2 = MyPoint()
    r3 = MyPoint(1)
    r4 = MyPoint(y = 10)
    print(r1)
    print()
    print(r2)
    print()
    print(r3)
    print()
    print(r4)

main()

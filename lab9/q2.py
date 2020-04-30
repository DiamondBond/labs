#!/usr/bin/env python3

class MyPoint(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

    def get_x(self):
        try:
            return int(self.__x)
        except:
            return int(0)

    def get_y(self):
        try:
            return int(self.__y)
        except:
            return int(0)

    def set_x(self, x):
        try:
            if x >= 0:
                self.__x = x
        except:
            pass

    def set_y(self, y):
        try:
            if y >= 0:
                self.__y = y
        except:
            pass

def main():
    print("test case 1:")
    r = MyPoint(3, 4)
    print(r)
    print(r.get_x(), r.get_y())

    print("\ntest case 2:")
    r = MyPoint()
    print(r.get_x(), r.get_y())

    print("\ntest case 3:")
    r = MyPoint()
    r.set_x(100)
    r.set_y(200)
    print(r)

    print("\ntest case 4:")
    r = MyPoint(10, 20)
    r.set_x(-100)
    r.set_y(-50)
    print(r)

main()

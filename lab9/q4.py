#!/usr/bin/env python3
import math

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

    def get_distance(self, other_point):
        diff_x = other_point.__x - self.__x
        diff_y = other_point.__y - self.__y
        x_sq = diff_x * diff_x
        y_sq = diff_y * diff_y
        distance = math.sqrt(x_sq + y_sq)
        return distance
    
    def is_near_by(self, other_point):
        distance = self.get_distance(other_point)
        if distance < 5.0:
            return True
        else:
            return False

class MyLine(MyPoint):
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__start_point = []
        self.__end_point = []

    def __str__(self):
        return "(" + str(self.__x1) + ", " + str(self.__y1) + ") to (" + str(self.__x2) + ", " + str(self.__y2) + ")"

def main():
    line1 = MyLine(10, 20, 20, 30)
    print(line1)

main()

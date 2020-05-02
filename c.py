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
        self.__start_point = MyPoint(x1, y1)
        self.__end_point = MyPoint(x2, y2)

    def __str__(self):
        return "(" + str(self.__x1) + ", " + str(self.__y1) + ") to (" + str(self.__x2) + ", " + str(self.__y2) + ")"

    def set_end_point(self, x2, y2):
        try:
            if x2 < 0:
                self.__x2 = 0
            else:
                self.__x2 = x2
            if y2 < 0:
                self.__y2 = 0
            else:
                self.__y2 = y2
        except:
            pass
        self.__end_point = (x2, y2)

    def set_start_point(self, x1, y1):
        try:
            if x1 < 0: self.__x1 = 0
            else:
                self.__x1 = x1
            if y1 < 0:
                self.__y1 = 0
            else:
                self.__y1 = y1
        except:
            pass
        self.__start_point = (x1, y1)

    def get_end_point(self):
        return self.__end_point
    
    def get_start_point(self):
        return self.__start_point

    def get_length(self):
        diff_x = self.__x1 - self.__x2
        diff_y = self.__y1 - self.__y2
        x_sq = diff_x * diff_x
        y_sq = diff_y * diff_y
        distance = math.sqrt(x_sq + y_sq)
        return distance

class MyCircle(MyPoint):
    def __init__(self, x = 0, y = 0 , radius = 1):
        self.__x = x
        self.__y = y
        self.__centre_point = MyPoint(self.__x, self.__y)
        self.__radius = radius

    def __str__(self):
        return "Circle at " + str(self.__centre_point) + ", radius = " + str(self.__radius)

    def set_radius(self, radius):
        if radius < 0:
            pass
        else:
            self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_centre_point(self, x, y):
        try:
            if x >= 0:
                self.__x = x
            else:
                pass
            
            if y >= 0:
                self.__y = y
            else:
                pass

        except:
            pass
        self.__centre_point = MyPoint(self.__x, self.__y)

    def get_centre_point(self):
        return self.__centre_point

    def get_distance(self, another_circle):
        diff_x = another_circle.__x - self.__x
        diff_y = another_circle.__y - self.__y
        x_sq = diff_x * diff_x
        y_sq = diff_y * diff_y
        distance = math.sqrt(x_sq + y_sq)
        return distance

class MyMultiLine(MyPoint):
    def __init__(self, points):
        self.__points = points

    def __str__(self):
        out_string = ""
        for i in range(0, len(self.__points)):
            out_string += str(self.__points[i])
        return out_string

    def get_distance(self, other_point):
        diff_x = other_point.__x - self.__x
        diff_y = other_point.__y - self.__y
        x_sq = diff_x * diff_x
        y_sq = diff_y * diff_y
        distance = math.sqrt(x_sq + y_sq)
        return distance
 
    def get_length(self):
        dist = 0
        for i in range(1, len(self.__points)):
            temp = self.__points[i-1].get_distance(self.__points[i])
            dist += temp
        return dist

def main():
    p1 = MyPoint()
    p2 = MyPoint(10, 20)
    p3 = MyPoint(20, 30)
    p4 = MyPoint(30, 40)
    line1 = MyMultiLine([p1, p2, p3, p4])
    print('The total length is {:.2f}.'.format(line1.get_length()))

main()

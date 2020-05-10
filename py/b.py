#!/usr/bin/env python3

class SimplePolynomial(object):
    def __init__(self, c0=1, c1=1, c2=1):
        self.__coefficients = [c0, c1, c2]

    def __str__(self):
        if self.__coefficients[0] != 0 and self.__coefficients[1] != 0 and self.__coefficients[2] != 0:
            return str(self.__coefficients[2]) + "x^2 + " + str(self.__coefficients[1]) + "x + " + str(self.__coefficients[0])
        elif self.__coefficients[0] != 0 and self.__coefficients[1] != 0 and self.__coefficients[2] == 0:
            return str(self.__coefficients[1]) + "x + " + str(self.__coefficients[0])
        elif self.__coefficients[0] == 0 and self.__coefficients[1] != 0 and self.__coefficients[2] != 0:
            return str(self.__coefficients[2]) + "x^2 + " + str(self.__coefficients[1]) + "x"
        elif self.__coefficients[0] != 0 and self.__coefficients[1] == 0 and self.__coefficients[2] != 0:
            return str(self.__coefficients[2]) + "x^2 + " + str(self.__coefficients[0])

    def evaluate(self, x):
        return self.__coefficients[2] * x ** 2 + self.__coefficients[1] * x + self.__coefficients[0]

    def __add__(self, x):
        temp_list = []
        for i in range(0, 3):
            temp_list.append(self.__coefficients[i] + x.__coefficients[i])
        out_list = SimplePolynomial(temp_list[0], temp_list[1], temp_list[2])
        return out_list
    
def main():
    p1 = SimplePolynomial(3, 2, 0)
    p2 = SimplePolynomial(1, 2, 3)
    p3 = p1 + p2
    print(type(p3))
    print(type(p2))
    print(p3.evaluate(2))

main()

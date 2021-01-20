import math
import matplotlib

def sigma(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const * i
    return sum

def main():
    print("please provide the point in room")
    print("x? ")
    x = int(input())

    print("y? ")
    y = int(input())

    # problem provides that 3.5 is the height to be used
    #print("z? ")
    #z = input()
    z = 3.5

    print(x, y, z)
    for i in range(0, 25):
        x_k = i
        y_k = i
        
        SUPER = sigma(1, 2, 1)

        BASED_SECT_1 = (x - x_k)^2
        BASED_SECT_2 = (y - y_k)^2
        #BASED_SECT_3 = (z - 6.0)^2.0 
        # ^ => (z = 3.5) ==> -2.5*2 = -5

        BASE = BASED_SECT_1 + BASED_SECT_2 - 1

        ANSWER = SUPER * 1/BASE
    print(ANSWER)

main()
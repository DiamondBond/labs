def pi(iteration):
    pi = 0.0
    sign = 1
    b = 1.0

    for i in range(iteration):
        pi += 4.0*sign/b

        b += 2
        sign *= -1

    print(pi)

pi(1000000)



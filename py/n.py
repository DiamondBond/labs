import random

print('tmp')
a=20
b=30
print(a+b)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
fact(5)

for i in range(10):
    a = a + random.randrange(10)

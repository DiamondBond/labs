#!/usr/bin/env python3
# y = n / 2 * (2 * a + (n - 1) * x)
# a = ((2 * y) / n - (n - 1) * x) / 2

ans = []
x = 13
y = 1000

# main
for n in range(1,10000):
    a = ((2 * y) / n - (n - 1) * x) / 2
    if a%1==0:
        a = int(a)
        ans.append((a, n))
        #print(ans)
print(ans)

#!/usr/bin/env python3


def printMan(offset):
    print(offset + "***** o")
    print(offset + "    */|\\")
    print(offset + "    */ \\")


offset = "*"
n = 6

for i in range(n):
    printMan(offset)
    offset += "    "
print("*" * ((n + 1) * 4 + 2))

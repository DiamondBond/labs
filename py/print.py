#!/usr/bin/env python3


def printOut(offset):
    print(offset + "***** o")
    print(offset + "    */|\\")
    print(offset + "    */ \\")


offset = "*"
n = 6

print("Generating", n, "stickmen...")
for i in range(n):
    printOut(offset)
    offset += "    "
print("*" * ((n + 1) * 4 + 2))

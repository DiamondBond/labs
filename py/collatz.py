import sys
input = sys.argv[1]

def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(x)    
    return num_seq

output = collatz_sequence(int(input))
print(output)
print(len(output))

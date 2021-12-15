import numpy as np

# read data
with open('input.txt') as f:
    data = [list(line.rstrip()) for line in f]

transposed = np.array(data).T.tolist()

# convert to numeric
numeric = [[ int(digit) for digit in l] for l in transposed ]

# find most common bits
common = [round(sum(x)/len(x)) for x in numeric]

gamma_string = "".join([str(digit) for digit in common])

def flip(d):
    if d == 0:
        return(1)
    elif d == 1:
        return(0)

epsilon_list = [flip(digit) for digit in common]

epsilon_string = "".join([str(digit) for digit in epsilon_list])

# convert from binary to decimal
gamma = int(gamma_string, 2)
epsilon = int(epsilon_string, 2)

print("product = %d" % (gamma * epsilon))
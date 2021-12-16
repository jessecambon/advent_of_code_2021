import numpy as np

def round_properly(d):
    if d == 0.5:
        return(1)
    else:
        return(round(d))

def flip(d):
    if d == 0:
        return(1)
    elif d == 1:
        return(0)

# read data
with open('sample.txt') as f:
    data =  [list(line.rstrip()) for line in f]

# convert input data to numeric list of lists
data_numeric = [[ int(digit) for digit in l] for l in data ]

#transposed = np.array(data_numeric).T.tolist()

# data_numeric indices
#indices_to_keep = list(range(len(data_numeric)))
remaining_numbers = data_numeric

# iterate through data and remove items that don't match criteria
for i in range(len(data_numeric[0])):
    # extract ith column from remaining numbers
    number_column = [x[i] for x in remaining_numbers]

    # find most common digit
    d_common = round_properly(sum(number_column)/len(number_column))
    print('d_common:')
    print(d_common)

    for l in remaining_numbers:
        # if only one value left then stop
        if l[i] != d_common:
            remaining_numbers.remove(l)
        
        if len(remaining_numbers) == 1:
            break

# use indices to keep to extract relevant number and convert from 
# decimal to binary
binary_oxygen = ''.join([str(d) for d in remaining_numbers[0]])

oxygen = int(binary_oxygen, 2)

print('oxygen: %d' % oxygen)





# gamma_string = "".join([str(digit) for digit in common])



# epsilon_list = [flip(digit) for digit in common]

# epsilon_string = "".join([str(digit) for digit in epsilon_list])

# # convert from binary to decimal
# gamma = int(gamma_string, 2)
# epsilon = int(epsilon_string, 2)

# print("product = %d" % (gamma * epsilon))
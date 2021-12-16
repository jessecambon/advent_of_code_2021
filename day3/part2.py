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


def find_value(val_type):

    remaining_numbers = data_numeric

# iterate through data and remove items that don't match criteria
    for i in range(len(data_numeric[0])):
        if len(remaining_numbers) == 1:
            break
        # extract ith column from remaining numbers
        number_column = [x[i] for x in remaining_numbers]

        # find most or least common digit

        d_select = round_properly(sum(number_column)/len(number_column))
        
        if val_type == 'scrubber':
            d_select = flip(d_select)
        print('d_select:')
        print(d_select)

        for l in remaining_numbers:
            # if only one value left then stop
            if len(remaining_numbers) == 1:
                break
            if l[i] != d_select:
                remaining_numbers.remove(l)

        print('remaining numbers:')
        print(remaining_numbers)

    # use indices to keep to extract relevant number and convert from 
    # decimal to binary
    binary_value = ''.join([str(d) for d in remaining_numbers[0]])

    print("binary_value: " + binary_value)

    final_value = int(binary_value, 2)

    return(final_value)

#oxygen = find_value('oxygen')
scrubber = find_value('scrubber')
#print('oxygen: %d' % oxygen)
print('scrubber: %d' % scrubber)




# gamma_string = "".join([str(digit) for digit in common])



# epsilon_list = [flip(digit) for digit in common]

# epsilon_string = "".join([str(digit) for digit in epsilon_list])

# # convert from binary to decimal
# gamma = int(gamma_string, 2)
# epsilon = int(epsilon_string, 2)

# print("product = %d" % (gamma * epsilon))
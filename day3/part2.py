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
with open('input.txt') as f:
    data =  [list(line.rstrip()) for line in f]

# convert input data to numeric list of lists
data_numeric = [[ int(digit) for digit in l] for l in data ]

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
            
        # print('d_select:')
        # print(d_select)

        # only keep numbers that match criteria
        remaining_numbers = [ l for l in remaining_numbers if l[i] == d_select]

    # use indices to keep to extract relevant number and convert from 
    # decimal to binary
    binary_value = ''.join([str(d) for d in remaining_numbers[0]])

    # print("binary_value: " + binary_value)

    final_value = int(binary_value, 2)

    return(final_value)

oxygen = find_value('oxygen')
scrubber = find_value('scrubber')
print('oxygen: %d' % oxygen)
print('scrubber: %d' % scrubber)
print('product: %d' % (oxygen * scrubber))
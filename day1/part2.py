# read data
with open('input.txt') as f:
    init_seq = [int(line.rstrip()) for line in f]

# Make list of lists spanning 3 numbers at a time

seq_lists = []
for j in range(len(init_seq)-2):
    seq_lists.append(init_seq[j:j+3])

# sum up the 3 numbers in each element

seq = [ sum(x) for x in seq_lists ]

# rest of the problem is same as part 1

i = 0

# how many increases and decreases were there
increases = 0 
decreases = 0

while i < len(seq):
    if i == 0:
        print(seq[0])
    else:
        if seq[i] == seq[i-1]:
            pass
        elif seq[i] < seq[i-1]:
            decreases += 1
            print('%d (decreased)' % seq[i])
        else:
            increases += 1
            print('%d (increased)' % seq[i])
    i +=1

print('\ntotal increases: %d' % increases)
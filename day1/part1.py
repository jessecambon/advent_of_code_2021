# read data
with open('input.txt') as f:
    seq = [int(line.rstrip()) for line in f]

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
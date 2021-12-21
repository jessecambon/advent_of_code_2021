from collections import Counter

part = 2 # part 1 or 2 ?

# read data
with open('input.txt') as f:
    vents_str = [line.strip().replace(' -> ', ',').split(',') for line in f]


straight = []
diagonal = []

# read in coordinates
vents_int = [[int(d) for d in line] for line in vents_str]

# given x1,x2 or y1,y2 return a list of increments to use to
# draw a diagonal from x1,y1 to x2,y2
def get_increments(a1, a2):
    a_range = list(range(abs(a2-a1) + 1))
    if a2 < a1:
        a_range = [ -1 * x for x in a_range]
    return(a_range)

for i, (x1, y1, x2, y2) in enumerate(vents_int):
    # if i == 3:
    #     break
    #print("(%d, %d) -> (%d, %d)" % (x1, y1, x2, y2))
    if x1 == x2 or y1 == y2:
    #    print('straight!')
        straight += [(x,y) for x in range(min(x1, x2), max(x1, x2)+1) for y in range(min(y1, y2), max(y1, y2)+1)]
    elif abs(x2-x1) == abs(y2-y1):
        #print('diagonal!')
        new_diagonal_pts = [(x1 + x_inc, y1 + y_inc) for (x_inc, y_inc) in zip(get_increments(x1,x2), get_increments(y1,y2)) ]
        #print(new_diagonal_pts)
        diagonal += new_diagonal_pts
    else:
    #    print('ignore!')
        pass

if part == 1:
    counts = Counter(straight)
else:
    counts = Counter(straight + diagonal)
count_pts = len([x for x in counts.values() if x >= 2])

print('number of points: %d' % count_pts)
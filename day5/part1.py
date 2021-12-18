from collections import Counter

# read data
with open('input.txt') as f:
    vents_str = [line.strip().replace(' -> ', ',').split(',') for line in f]


straight = []

# read in coordinates
vents_int = [[int(d) for d in line] for line in vents_str]

for i, (x1,y1,x2,y2) in enumerate(vents_int):
    # if i == 3:
    #     break
    #print("(%d, %d) -> (%d, %d)" % (x1, y1, x2, y2))
    if x1 == x2 or y1 == y2:
    #    print('straight!')
        straight += [(x,y) for x in range(min(x1,x2), max(x1,x2)+1) for y in range(min(y1,y2), max(y1,y2)+1)]
    else:
    #    print('ignore!')
        pass

counts = Counter(straight)
count_pts = len([x for x in counts.values() if x >= 2])

print('number of points: %d' % count_pts)
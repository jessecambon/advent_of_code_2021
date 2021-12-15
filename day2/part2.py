# read data
with open('input.txt') as f:
    moves = [line.rstrip().split(' ') for line in f]


horizontal = 0
depth = 0
aim = 0

for direction, distance in moves:
    distance = int(distance)
    if direction == 'forward':
        horizontal += distance
        depth += aim * distance
    elif direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance

print('horizontal: %d' % horizontal)
print('depth: %d' % depth)
print('product: %d' % (depth * horizontal))
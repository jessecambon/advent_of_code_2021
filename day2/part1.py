# read data
with open('input.txt') as f:
    moves = [line.rstrip().split(' ') for line in f]


horizontal = 0
depth = 0

for direction, distance in moves:
    distance = int(distance)
    if direction == 'forward':
        horizontal += distance
    elif direction == 'up':
        depth -= distance
    elif direction == 'down':
        depth += distance

print('horizontal: %d' % horizontal)
print('depth: %d' % depth)
print('product: %d' % (depth * horizontal))
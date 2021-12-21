
# A solution from reddit --------

with open('sample.txt') as f:
    fish_init_str =  [ line.strip().split(',') for line in f]

fish_init = [int(x) for x in fish_init_str[0]]


def solve(data, days):
    tracker = [data.count(i) for i in range(9)]
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)


print(f"Part 1: {solve(fish_init, 80)}")
print(f"Part 2: {solve(fish_init, 256)}")
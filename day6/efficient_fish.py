n_iterations = 256

with open('input.txt') as f:
    fish_init_str =  [ line.strip().split(',') for line in f]

fish_init = [int(x) for x in fish_init_str[0]]

timers = [0]*9 # values of 0 to 8 days

# insert initial fish
for i in fish_init:
    timers[i] += 1

for _ in range(n_iterations):
    new_timers = timers[1:] # shift counts down 1
    new_timers.append(timers[0]) # '0' fish produce new '8' fish
    new_timers[6] += timers[0] # '0' fish get reset to '6' fish
    timers = new_timers

print(sum(timers))
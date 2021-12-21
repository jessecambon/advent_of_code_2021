n_iterations = 256

with open('sample.txt') as f:
    fish_init_str =  [ line.strip().split(',') for line in f]

fish_init = [int(x) for x in fish_init_str[0]]


class Fish:
    def __init__(self, n_iterations):
        self.current_fish = fish_init
        self.new_fish = []
        self.n_iterations = n_iterations

    def age_fish(self, d):
        if d == 0:
            self.new_fish.append(8) # create new fish
            return(6)
        else:
            return(d-1)
    
    # iterate through lifecycles
    def main(self):
        for i in range(1, n_iterations + 1):
            self.new_fish = [] # reset new fish object

            # age the fish we have
            aged_fish = [self.age_fish(fish) for fish in self.current_fish]

            # print('new fish:')
            # print(self.new_fish)

            # add the new fish and the aged fish together
            self.current_fish = aged_fish + self.new_fish 


# i is 1 indexed

the_fish = Fish(n_iterations)

the_fish.main()

#print(the_fish.current_fish)

print('number of fish:')
print(len(the_fish.current_fish))
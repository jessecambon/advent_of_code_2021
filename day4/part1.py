import numpy as np

bingo_boards = []
bingo_square_txt = []

# Read in bingo squares as 2d numpy arrays in a list
# and bingo numbers as a single 1d numpy array
with open('input.txt') as f:
    line_index = 0
    for line in f:
        if line_index == 0:
            bingo_numbers = np.fromstring(line.strip(), sep=',')
            line_index += 1
        elif line.rstrip() != '':
            bingo_square_txt.append(line.strip())
            # store bingo square as numpy array
            if len(bingo_square_txt) == 5:
                bingo_boards.append(np.fromstring(' '.join(bingo_square_txt), sep=' ').reshape(5, 5))
                bingo_square_txt = [] # reset bingo square


# Play bingo - reveal one bingo number at a time
# use one board for now

bingo_numbers_in_play = np.empty(0)

bingo = False # has a board won yet?

for i in range(len(bingo_numbers)):
    if bingo == True:
            print('Bingo!')
            print('Winning board number: %d' % (board_number+1))
            print('Numbers in play:')
            print(bingo_numbers_in_play)

            unscored_numbers = selected_board.flatten()[np.isin(selected_board.flatten(), bingo_numbers_in_play, invert = True)]
            print("unscored sum: %d" % sum(unscored_numbers))
            print("last bingo number: %d" % bingo_numbers_in_play[-1])
            print('product: %d' % (sum(unscored_numbers) * bingo_numbers_in_play[-1]))
            break

    # select bingo numbers in play for the given round
    bingo_numbers_in_play = np.append(bingo_numbers_in_play, bingo_numbers[i])

    for board_number, selected_board in enumerate(bingo_boards):
        # check rows for bingo
        for k in range(5):
            row = selected_board[k]
            if sum(np.isin(row, bingo_numbers_in_play)) == 5:
                print('row:')
                print(row)
                bingo = True
                break
        
        # check columns for bingo
        for k in range(5):
            column = selected_board[:,k]
            if sum(np.isin(column, bingo_numbers_in_play)) == 5:
                print('column:')
                print(column)
                bingo = True
                break
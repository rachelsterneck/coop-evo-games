import random

# 0 --> empty
# 1 --> cooperator
# 2 --> defector
EMPTY = 0
COOPERATOR = 1
DEFECTOR = 2

UNDERPOPULATION_THRESHOLD = 2
OVERPOPULATION_THRESHOLD = 3
BIRTH_THRESHOLD = 3

def create_board(N, p, b):
    board = [[EMPTY]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            r1 = random.uniform(0, 1)
            if r1 > b:
                r2 = random.uniform(0, 1)
                if r2 > p:
                    board[i][j] = DEFECTOR
                else:
                    board[i][j] = COOPERATOR

    return board


def get_neighbor_count(board, neighbors):
    neighbor_count = 0
    for r, c in neighbors:
        if board[r][c] == 0:
            neighbor_count += 1
    
    return neighbor_count

def update_board(N, board):
    for i in range(N):
        for j in range(N):
            current_cell = board[i][j]
            neighbors = get_neighbor_coords(N, i, j)
            neighbor_count = get_neighbor_count(board, neighbors)

            # cell is dead, check if will come to life
            if current_cell == 0:
                if neighbor_count == BIRTH_THRESHOLD:
                    # to do: implement birth logic
                    board[i][j] = 5
            else:
                # if cell underpopulated or overpopulated, it dies
                # otherwise it survives (no change) 
                if neighbor_count < UNDERPOPULATION_THRESHOLD or neighbor_count > OVERPOPULATION_THRESHOLD:
                    board[i][j] = EMPTY

def get_neighbor_coords(N, cell_x, cell_y):
    neighbor_coords = []
    
    # top_left
    if cell_x-1 >= 0 and cell_y-1 >= 0:
        neighbor_coords.append((cell_x-1, cell_y-1))

    # left
    if cell_y-1 >= 0:
        neighbor_coords.append((cell_x, cell_y-1))

    # bottom left
    if cell_x+1 < N and cell_y-1 >= 0:
        neighbor_coords.append((cell_x+1, cell_y-1))

    # top right
    if cell_x-1 >= 0 and cell_y+1 < N:
        neighbor_coords.append((cell_x-1, cell_y+1))

    # right
    if cell_y+1 < N:
        neighbor_coords.append((cell_x, cell_y+1))

    # bottom right
    if cell_x+1 < N and cell_y+1 < N:
        neighbor_coords.append((cell_x+1, cell_y+1))

    # top 
    if cell_x-1 >= 0:
        neighbor_coords.append((cell_x-1, cell_y))

    # bottom
    if cell_x+1 < N:
        neighbor_coords.append((cell_x+1, cell_y))

    # if cell_x != 0:
    #     neighbor_coords.append(top_left)
    #     neighbor_coords.append(top)
    #     neighbor_coords.append(top_right)

    # if cell_x != N-1:
    #     neighbor_coords.append(bottom_left)
    #     neighbor_coords.append(bottom)
    #     neighbor_coords.append(bottom_right)

    # if cell_y != 0:
    #     #neighbor_coords.append(top_left)
    #     neighbor_coords.append(left)
    #     #neighbor_coords.append(bottom_left)

    # if cell_y != N-1:
    #     #neighbor_coords.append(top_right)
    #     neighbor_coords.append(right)
    #     #neighbor_coords.append(bottom_right)
    
    return neighbor_coords


def print_board(N, board):
    for i in range(N):
        board_str = [str(e) for e in board[i]]
        print(' '.join(board_str))


if __name__ == "__main__":
    # size of game board
    N = 10
    # proportion of cooperators
    p = 0.2
    # initial proportion of board filled
    b = 0.5
    # number of iterations
    iterations = 5

    board = create_board(N, p, b)
    print_board(N, board)

    generation = 0
    while generation < iterations:
        update_board(N, board)
        print('\n\n')
        print_board(N, board)
        generation += 1
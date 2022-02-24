import random
# Evaluation logic taken from Yupan Huang
# at the following link
# https://github.com/HYPJUDY/EightQueensAndPuzzle/blob/master/EightQueensAndPuzzle/EightQueensProblem/SteepestHillClimbing.py

# heuristic function to evaluate a board given a list
# of length 8 with values of 1 thru 8


def evaluate(board):

    num = 0
    for col in range(len(board)):
        for anotherCol in range(col+1, len(board)):
            if board[col] == board[anotherCol]:
                num += 1  # collied in the same row
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                num += 1  # collied diagonally
    return num


# function to find the next best state given a board state

def generate_next_state(board):

    # track best state
    best_state = board.copy()
    best_state_h = evaluate(best_state)

    # if current state is a goal state return True
    if best_state_h == 0:
        return best_state

    # iterate through columns and finding the h cost
    # of each change, assign best_state accordingly
    for col, value in enumerate(board):
        for row in range(1, len(board)+1):
            if value == row:
                continue
            test_board = board.copy()
            test_board[col] = row
            test_board_h = evaluate(test_board)

            if test_board_h < best_state_h:
                best_state = test_board
                best_state_h = test_board_h
    return best_state


def hill_climbing_solution(board):

    max_iterations = 250

    iterations = 0

    solve_board = board.copy()
    attacks = evaluate(solve_board)

    if attacks == 0:
        return (solve_board, iterations, attacks)

    while attacks != 0:

        next_board = generate_next_state(solve_board)
        if next_board == solve_board:
            return (solve_board, iterations, attacks)
        solve_board = next_board.copy()
        attacks = evaluate(solve_board)
        iterations += 1
        if iterations >= max_iterations:
            return (solve_board, iterations, attacks)

    return (solve_board, iterations, attacks)


def random_restart_solution(board):

    max_iterations = 250

    iterations = 0

    # copy initial board to avoid pointers
    solve_board = board.copy()
    attacks = evaluate(solve_board)

    # if initial state is a goal state
    if attacks == 0:
        return (solve_board, iterations, attacks)

    while attacks != 0:

        next_board = generate_next_state(solve_board)

        # if local minimum is reached randomize the board
        if next_board == solve_board:
            random.shuffle(solve_board)
            iterations += 1
            continue

        # else make current board the next best state found
        solve_board = next_board.copy()

        # evaluate board
        attacks = evaluate(solve_board)

        # track solution cost
        iterations += 1

        # max acceptable solution cost
        if iterations >= max_iterations:
            return (solve_board, iterations, attacks)

    # return values after solving
    return (solve_board, iterations, attacks)

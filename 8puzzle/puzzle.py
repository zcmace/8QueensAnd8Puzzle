import random

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

test_state = [2, 1, 3, 0, 4, 6, 7, 5, 8]

# evaluate heuristic cost
# we define h to be the amount of numbers not in their correct position


def evaluate(state):
    distance = 0
    for i in range(9):
        if state[i] != goal_state[i] and state[i] != 0:
            distance += 1

    return distance


# index//3 == 0 (first row)
# index//3 == 1 (second row)
# index//3 == 2 (third row)

# index % 3 == 0 ( first col)
# index % 3 == 1 ( second col)
# index % 3 == 2 ( third col)

# 0 1 2
# 3 4 5
# 6 7 8


def generate_next_state(state):

    best_state = state.copy()
    best_state_h = evaluate(state)

    zero_index = best_state.index(0)

    # evaluate left and/or right options
    col = zero_index % 3

    # first column, moving right is a possibility
    if col == 0:

        evaluation_state = state.copy()
        # swap zero with item to right
        evaluation_state[zero_index],
        evaluation_state[zero_index + 1] = evaluation_state[zero_index + 1],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()
    # last column, moving left is a possiblity
    if col == 2:
        evaluation_state = state.copy()
        # swap zero with item to left
        evaluation_state[zero_index],
        evaluation_state[zero_index - 1] = evaluation_state[zero_index - 1],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()

    # middle column, left and right are possibilities
    if col == 1:
        # reset
        evaluation_state = state.copy()

        # left
        evaluation_state[zero_index],
        evaluation_state[zero_index - 1] = evaluation_state[zero_index - 1],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()

        # reset
        evaluation_state = state.copy()

        # right
        evaluation_state[zero_index],
        evaluation_state[zero_index + 1] = evaluation_state[zero_index + 1],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()

    # evaluate up and/or down options

    row = zero_index//3

    # first row, moving down is a possibility
    if row == 0:

        evaluation_state = state.copy()
        # swap zero with item below
        evaluation_state[zero_index],
        evaluation_state[zero_index + 3] = evaluation_state[zero_index + 3],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()

    # last row, moving up is a possiblity
    if row == 2:
        evaluation_state = state.copy()
        # swap zero with item above
        evaluation_state[zero_index],
        evaluation_state[zero_index - 3] = evaluation_state[zero_index - 3],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()

    # middle row, up and down are possibilities
    if row == 1:
        # reset
        evaluation_state = state.copy()

        # up
        evaluation_state[zero_index],
        evaluation_state[zero_index - 3] = evaluation_state[zero_index - 3],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()

        # reset
        evaluation_state = state.copy()

        # down
        evaluation_state[zero_index],
        evaluation_state[zero_index + 3] = evaluation_state[zero_index + 3],
        evaluation_state[zero_index]

        score = evaluate(evaluation_state)
        if score < best_state_h:
            best_state_h = score
            best_state = evaluation_state.copy()
    return best_state


def hill_climbing_solution(state):

    solve_state = state.copy()

    iterations = 0
    score = evaluate(solve_state)

    if solve_state == goal_state:
        return (solve_state, iterations, score)

    while score != 0:

        next_state = generate_next_state(solve_state)
        if next_state == solve_state:
            return (solve_state, iterations, score)

        solve_state = next_state
        score = evaluate(solve_state)

        iterations += 1

    return (solve_state, iterations, score)


def rand_restart_solution(state):

    solve_state = state.copy()
    max_iterations = 10000
    iterations = 0
    score = evaluate(solve_state)

    if solve_state == goal_state:
        return (solve_state, iterations, score)

    while solve_state != goal_state:

        if iterations >= max_iterations:
            return (solve_state, iterations, score)

        next_state = generate_next_state(solve_state)
        if next_state == solve_state:
            random.shuffle(solve_state)
        else:
            solve_state = next_state.copy()

        score = evaluate(solve_state)

        iterations += 1

    return (solve_state, iterations, score)

from queens import hill_climbing_solution, random_restart_solution
import numpy
import matplotlib
from generate_boards import generate
import time


# generate new test data

print('\nNow generating new test cases...')
time.sleep(1)
generate()

print('\n800 Test cases generated. \n')
time.sleep(1)
# solve using hill climbing
print("Solving using hill climbing... \n~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)

with open('./queens_test_cases.txt') as file:

    print('Test Cases located at: ', file.name)

    number_stuck = 0
    total_cost_local_minimum = 0

    number_solved = 0
    total_search_cost = 0
    count = 1

    while True:

        line = file.readline()
        if not line:
            break

        test_case = []

        for number in line:
            if number == '\n':
                continue
            test_case.append(int(number))

        solve_board, iterations, attacks = hill_climbing_solution(
            test_case)
        if (attacks > 0):
            number_stuck += 1
            total_cost_local_minimum += iterations
        else:
            total_search_cost += iterations
            number_solved += 1

            # uncomment for debugging
            # print(
            #     f'Test Case {count}: \nSolution: {solve_board}\nSolve Cost:'
            #     f'{iterations}\nExisting Attacks: {attacks}'
            # )
        count += 1

    percent_solved = (number_solved/800) * 100
    avg_cost_to_solve = total_search_cost/number_solved

    print(
        f"Total number solved out of 800: {number_solved}", f"({percent_solved:.2f}%)")
    print(f"Average Search Cost to solve: {avg_cost_to_solve:.2f}")


# solve using random restart hill climbing
print("\n\nSolving using random restart hill climbing... \n~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)
with open('./queens_test_cases.txt') as file:

    print('Test Cases located at: ', file.name)

    number_stuck = 0
    total_cost_local_minimum = 0

    number_solved = 0
    total_search_cost = 0
    count = 1

    while True:

        line = file.readline()
        if not line:
            break

        test_case = []

        for number in line:
            if number == '\n':
                continue
            test_case.append(int(number))

        solve_board, iterations, attacks = random_restart_solution(
            test_case)
        if (attacks > 0):
            number_stuck += 1
            total_cost_local_minimum += iterations
        else:
            total_search_cost += iterations
            number_solved += 1

            # uncomment for debugging
            # print(
            #     f'Test Case {count}: \nSolution: {solve_board}\nSolve Cost:'
            #     f'{iterations}\nExisting Attacks: {attacks}'
            # )
        count += 1

    percent_solved = (number_solved/800) * 100
    avg_cost_to_solve = total_search_cost/number_solved

    print(
        f"Total number solved out of 800: {number_solved}", f"({percent_solved:.2f}%)")
    print(f"Average Search Cost to solve: {avg_cost_to_solve}")

print('\nDone!\n')

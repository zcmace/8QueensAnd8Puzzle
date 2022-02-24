import queens
import sys
print(sys.executable)
import numpy
import matplotlib

# solve using hill climbing
print("Solving using hill climbing... \n~~~~~~~~~~~~~~~~~~~~~~")

with open('./queens_test_cases.txt') as file:

    print('Solving 8 Queens Problem Test Cases located at ', file.name)

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

        solve_board, iterations, attacks = queens.hill_climbing_solution(
            test_case)
        if (attacks > 0):
            print("Test Case", count, "Failed!", iterations)
        else:
            total_search_cost += iterations
            number_solved += 1

            print(
                f'Test Case {count}: \nSolution: {solve_board}\nSolve Cost:'
                f'{iterations}\nExisting Attacks: {attacks}'
            )
        count += 1
    print("Total number solved:", number_solved)
    print("Average Search Cost to solve: ", total_search_cost/number_solved)

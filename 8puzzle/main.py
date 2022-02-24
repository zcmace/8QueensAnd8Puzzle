from puzzle import hill_climbing_solution, rand_restart_solution, goal_state
from generate_test_cases import generate

print("Generating new test cases... ")

generate()

print("Generated 800 test cases.")

# solving with hill climbing
print("Solving using hill climbing... \n~~~~~~~~~~~~~~~~~~~~~~")
random_solved = 0
solved = 0

total_cost_solved = 0
total_cost_rand_solved = 0

with open('./puzzle_test_cases.txt') as file:
    for line in file:
        test_case_strings = line.split()
        test_case = list(map(int, test_case_strings))

        solution, cost, heuristic = hill_climbing_solution(test_case)

        if (solution == goal_state):
            total_cost_solved += cost
            solved += 1
            print(solution, cost, heuristic)

# solving with random restart hill climbing
print("Solving using random restart hill climbing... \n~~~~~~~~~~~~~~~~~~~~~~")
with open('./puzzle_test_cases.txt') as file:
    for line in file:
        test_case_strings = line.split()
        test_case = list(map(int, test_case_strings))

        solution, cost, heuristic = rand_restart_solution(test_case)

        if (solution == goal_state):
            total_cost_rand_solved += cost
            random_solved += 1
            print(solution, cost, heuristic)

if (random_solved != 0):
    avg_cost_rand = total_cost_rand_solved/random_solved
else:
    avg_cost_rand = 0

if (solved != 0):
    avg_cost = total_cost_solved/solved
else: 
    avg_cost = 0
    
random_percent_solved = random_solved/800 * 100
percent_solved = solved/800 * 100

print(
    f'Results: \n'
    f'# of test cases: 800\n'
    f'Total solved without random restart: {solved} | {percent_solved:.2f}%\n'
    f'Average cost for solution without random restart: {avg_cost:.2f}\n\n'
    f'Total solved with random restart: {random_solved} | {random_percent_solved:.2f}%\n'
    f'Average cost for solution with random restart: {avg_cost_rand:.2f}'
    f''
)

from puzzle import hill_climbing_solution, rand_restart_solution, goal_state
from generate_test_cases import generate
from matplotlib import pyplot

print("Generating new test cases... \n")

generate()

print("Generated 800 test cases.\n")

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
    f'# of test cases: 800\n\n'
    f'Total solved without random restart: {solved} | {percent_solved:.2f}%\n'
    f'Average cost for solution without random restart: {avg_cost:.2f}\n\n'
    f'Total solved with random restart (10,000 cost limit): '
    f'{random_solved} | {random_percent_solved:.2f}%\n'
    f'Average cost for solution with random restart: {avg_cost_rand:.2f}'
    f''
)

cost_graph = pyplot.figure(1)
pyplot.bar(["Hill Climbing",
            "Hill Climnbing w/ Random Restart"],
           [avg_cost,
            avg_cost_rand])
pyplot.title(
    'Solution costs of the 8 Puzzle Problem with Hill Climbing variants')
pyplot.ylabel('Cost in Steps')
pyplot.xlabel('Method Used')

pyplot.savefig('./cost_graph.png')
solved_graph = pyplot.figure(2)
pyplot.bar(["Hill Climbing",
            "Hill Climnbing w/ Random Restart"],
           [percent_solved, random_percent_solved])
pyplot.title(
    'Percentage of 8 Puzzle Problems Solved with Hill Climbing Variants')
pyplot.ylabel('Percentage of Problems Solved')
pyplot.xlabel('Method Used')
pyplot.savefig('./solved_graph.png')

pyplot.show()

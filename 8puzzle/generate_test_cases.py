import random

# simple function to generate test data for the 8 puzzle game
# takes advantage of random library to shuffle a list of integers 0-8
# this guarantees that one of each integer will be included in a random
# order


def generate():
    with open('./puzzle_test_cases.txt', 'w') as file:

        for i in range(800):

            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
            random.shuffle(numbers)
            line = ' '.join(numbers)
            if i == 799:
                file.write(line)
            else:
                file.write(line + '\n')

        file.close()

import random


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
import random

with open('./queens_test_cases.txt', 'w') as file:
    test_cases = ""
    for i in range(800):
        for j in range(1, 9):
            test_cases += str(random.randint(1, 8))
        if i == 799:
            break
        test_cases += '\n'
    file.write(test_cases)
    file.close()

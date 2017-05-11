import sys
import InputLoader

instructions = InputLoader.load_file('Day_1.txt')


def solve_part1():
    floor = 0

    for instruction in instructions:
        # Go Up
        if instruction == '(':
            floor += 1
        # Go Down
        elif instruction == ')':
            floor -= 1
        else:
            sys.exit('Invalid Input')

    return floor


def solve_part2():
    floor = 0
    inst_num = 1

    for instruction in instructions:
        # Go Up
        if instruction == '(':
            floor += 1
        # Go Down
        elif instruction == ')':
            floor -= 1
        else:
            sys.exit('Invalid Input')

        if floor == -1:
            return inst_num

        inst_num += 1


print(solve_part1())
print(solve_part2())


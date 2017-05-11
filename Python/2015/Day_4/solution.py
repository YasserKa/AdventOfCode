import hashlib

puzzle_input = "iwrupvqb"
part = 1

tot_zeroes = 5 if part == 1 else 6


def check_md5(key):
    m = hashlib.md5()
    m.update(key.encode('utf-8'))
    return m.hexdigest()[:tot_zeroes] == '0' * tot_zeroes


def solve_part1(puzzle_input):
    number = 0
    while True:
        key = puzzle_input + str(number)
        if check_md5(key):
            break
        number += 1
    return key

print(solve_part1(puzzle_input))

import InputLoader
from functools import reduce

total_dimensions = InputLoader.load_file('Day_2.txt').splitlines()


def smallest_side(surface_area):
    return min(surface_area)


def solve_part1():
    total_wrapping_paper = 0

    for dimensions in total_dimensions:
        surface_area = []
        array_dimensions = list(map(lambda x: int(x), dimensions.split('x')))
        for dimension in range(-1, len(array_dimensions) - 1):
            surface_area.append(
                                    + 2
                                    * array_dimensions[dimension]
                                    * array_dimensions[dimension + 1]
                            )
        total_wrapping_paper = total_wrapping_paper +\
                               reduce(lambda x, y: x + y, surface_area) +\
                               smallest_side(surface_area)/2

    return total_wrapping_paper


def solve_part2():
    total_wrapping_paper = 0

    for dimensions in total_dimensions:
        surface_area = []
        array_dimensions = list(map(lambda x: int(x), dimensions.split('x')))
        total_wrapping_paper = total_wrapping_paper \
                               + reduce(lambda x, y: x * y, array_dimensions)\

        least_side = smallest_side(array_dimensions)
        total_wrapping_paper = total_wrapping_paper + 2 * least_side
        array_dimensions.remove(least_side)

        total_wrapping_paper = total_wrapping_paper + 2 * smallest_side(array_dimensions)
        # total_wrapping_paper = array_dimensions.remove(2)
    return total_wrapping_paper


#print(solve_part1())
print(solve_part2())

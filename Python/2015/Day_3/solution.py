import InputLoader
from HomeTracker import HomeTracker

directions = InputLoader.load_file('Day_3.txt')
print(directions)

my_homeTracker_1 = HomeTracker(directions)
my_homeTracker_2 = HomeTracker(directions)

def move(part):
    home_tracker = my_homeTracker_1
    turn = 0
    for direction in directions:

        if direction == '^':
            home_tracker.move_up()
        elif direction == 'v':
            home_tracker.move_down()
        elif direction == '<':
            home_tracker.move_left()
        elif direction == '>':
            home_tracker.move_right()

        home_tracker.add_home()
        if turn % 2 == 0:
            home_tracker = my_homeTracker_2
        else:
            home_tracker = my_homeTracker_1
        if part == 2:
            turn = turn + 1


def merge():
    total = 0
    for row in my_homeTracker_1.homes_visited:
        if row in my_homeTracker_2.homes_visited:
            total = total + len(set(my_homeTracker_1.homes_visited[row] + my_homeTracker_2.homes_visited[row]))
            del my_homeTracker_2.homes_visited[row]
        else:
            total = total + len(my_homeTracker_1.homes_visited[row])

    for row in my_homeTracker_2.homes_visited:
        total = total + len(my_homeTracker_2.homes_visited[row])
    return total

part = 1

move(part)
if part == 1:
    print(merge() + 1)
else:
    print(merge())


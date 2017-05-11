from enum import Enum

class HomeTracker:

    class Existence(Enum):
        NOT_IN_X = 1
        NOT_IN_Y = 2

    def __init__(self, directions):
        self.directions = directions
        self.x_position = 0
        self.y_position = 0
        self.homes_visited = {0: [0]}

    def move(self):
        for direction in self.directions:
            if direction == '^':
                self.move_up()
            elif direction == 'v':
                self.move_down()
            elif direction == '<':
                self.move_left()
            elif direction == '>':
                self.move_right()
            self.add_home()

    def move_up(self):
        self.y_position = self.y_position + 1

    def move_down(self):
        self.y_position = self.y_position - 1

    def move_right(self):
        self.x_position = self.x_position + 1

    def move_left(self):
        self.x_position = self.x_position - 1

    def add_home(self):
        home_exists = self.check_home()
        if home_exists == self.Existence.NOT_IN_Y:
            self.homes_visited[self.y_position] = [self.x_position]
        if home_exists == self.Existence.NOT_IN_X:
            self.homes_visited[self.y_position].append(self.x_position)

    def check_home(self):
        if self.y_position not in self.homes_visited:
            return self.Existence.NOT_IN_Y

        if self.x_position not in self.homes_visited[self.y_position]:
            return self.Existence.NOT_IN_X


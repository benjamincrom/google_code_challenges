'''
https://code.google.com/archive/p/marsrovertechchallenge/
'''
import collections

Grid = collections.namedtuple('Grid', 'x y')


class Rover(object):
    def __init__(self, grid_obj, x_loc, y_loc, orientation):
        self.grid = grid_obj
        self.position = (int(x_loc), int(y_loc))
        self.orientation_deque = collections.deque([
            ('N', self.go_north),
            ('E', self.go_east),
            ('S', self.go_south),
            ('W', self.go_west)
        ])

        while self.orientation_deque[0][0] != orientation:
            self.orientation_deque.rotate(1)

    def go_north(self):
        assert self.position[1] < self.grid.y
        self.position = (self.position[0], self.position[1] + 1)

    def go_south(self):
        assert self.position[1] > 0
        self.position = (self.position[0], self.position[1] - 1)

    def go_east(self):
        assert self.position[0] < self.grid.x
        self.position = (self.position[0] + 1, self.position[1])

    def go_west(self):
        assert self.position[0] > 0
        self.position = (self.position[0] - 1, self.position[1])

    def rotate(self, direction):
        if direction == 'L':
            self.orientation_deque.rotate(1)
        elif direction == 'R':
            self.orientation_deque.rotate(-1)
        else:
            raise Exception('Invalid direction: {}'.format(direction))

    def move(self):
        self.orientation_deque[0][1]()

    def __repr__(self):
        return 'Position: {}, Orientation: {}'.format(
            self.position,
            self.orientation_deque[0][0]
        )


def move_rovers(grid_str, rover_1_pos_str, rover_1_command_str, rover_2_pos_str,
                rover_2_command_str):
    grid = Grid(*(int(s) for s in grid_str.split()))
    rover_1 = Rover(grid, *rover_1_pos_str.split())
    rover_2 = Rover(grid, *rover_2_pos_str.split())

    rover_tup_list = [(rover_1, rover_1_command_str),
                      (rover_2, rover_2_command_str)]

    for rover, command_list_str in rover_tup_list:
        for command in command_list_str:
            if command == 'L' or command == 'R':
                rover.rotate(command)
            elif command == 'M':
                rover.move()
            else:
                raise Exception(
                    'Invalid commmand {} in command list {}'.format(
                        command,
                        command_list_str
                    )
                )

    return [t[0] for t in rover_tup_list]

print(move_rovers('5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'))

from matplotlib import pyplot as plt
from graph import init_graph
import numpy as np

# Class representing the robot
class Robot:
    def __init__(self, position, direction, mv_speed, rot_speed):
        self.position = position
        self.direction = direction
        self.mv_speed = mv_speed
        self.rot_speed = rot_speed

    def __str__(self):
        return "The robot is in " + str(self.position) + " in direction " + str(
            self.direction) + " at a mv speed " + str(self.mv_speed) + " and rot speed " + str(self.rot_speed)


# Initialize world
def init_world(filename, n=30, mv=2, rot=3):

    global robot

    # Init list of balls with no balls
    list_balls = []
    size = 0

    # Create n*n field
    plt.xlim(0, n)
    plt.ylim(0, n)

    with open(filename, 'r') as f:

        for line in f:

            line = line.strip()

            # Manage comments
            if not line or line.startswith('#'):
                continue

            # Parse coordinates
            name, coords = line.split(':')
            name = name.strip()
            coords = coords.strip()

            # Robot
            if name == 'R':
                x, y = map(int, coords[1:-1].split(','))
                robot = Robot(np.array([x, y]), 0, mv, rot)

            # Ball
            elif name.isdigit():
                x, y = map(int, coords[1:-1].split(','))
                new_ball = np.array([x, y])

                # if balls not in world, and not in the list (avoid duplicates)
                if np.all(new_ball <= np.array([n, n])) and not np.array_equal(new_ball, list_balls):
                    list_balls.append(new_ball)
                    size += 1

    # if no instruction about the robot, place it at [n/2, n/2]
    if 'robot' not in globals():
        robot = Robot(np.array([n//2, n//2]), 0, mv, rot)

    # delete balls at robot.position (zero time to pick up)
    for b in list_balls:
        if np.all(b == robot.position):
            list_balls.remove(b)
            print(b)

    print("World generated : Number of balls to pick : " + str(len(list_balls)))

    return robot, list_balls


# Print a world

def print_world(graph, robot, list_balls, passed_balls,previous,frompoint):
    print(len(list_balls))
    list_balls=list_balls+[robot.position]

    if(frompoint >= len(list_balls)-1):
        plt.plot(robot.position[0], robot.position[1], marker="o", label='robot')
        plt.text(robot.position[0] + 0.5, robot.position[1] + 0.5, str(len(list_balls)-1))
        startpos = robot.position
    else:
        startpos = list_balls[frompoint]

    # ¨Print each ball and weight between
    for i in range(len(list_balls)-1):
        
        plt.plot(list_balls[i][0], list_balls[i][1], marker="o", label='ball')
        plt.text(list_balls[i][0] + 0.5, list_balls[i][1] + 0.5, i)

        x_values = [startpos[0], list_balls[i][0]]
        y_values = [startpos[1], list_balls[i][1]]

        appartenance=[(list_balls[i]==x).all() for x in passed_balls]
        value=True
        for bool in appartenance:
            if bool==False:
                value=False
                break
        
        if i==frompoint or value:# or (list_balls[i] in passed_balls).all():

            continue

        plt.plot(x_values, y_values, 'b-')

        mat = graph
        val = mat[previous][frompoint][i]
        plt.text((startpos[0] + list_balls[i][0]) / 2, (startpos[1] + list_balls[i][1]) / 2, str(val))

    # Launch print
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("This file is not runable\n")
    
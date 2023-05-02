from matplotlib import pyplot as plt
from graph import *
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
def init_world(filename, n, mv, rot):

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
                robot = Robot([x, y], 0, mv, rot)

            # Ball
            elif name.isdigit():
                x, y = map(int, coords[1:-1].split(','))
                list_balls.append(np.array([x, y]))
                size += 1

    print("World generated : Number of balls to pick : " + str(len(list_balls)))

    return robot, list_balls


# Print a world
def print_world(graph, robot, list_balls, frompoint):

    if(frompoint >= len(list_balls)):
        plt.plot(robot.position[0], robot.position[1], marker="o", label='robot')
        plt.text(robot.position[0] + 0.5, robot.position[1] + 0.5, str(len(list_balls)))
        startpos = robot.position
    else:
        startpos = list_balls[frompoint]

    # ¨Print each ball and weight between
    for i in range(len(list_balls)):

        plt.plot(list_balls[i][0], list_balls[i][1], marker="o", label='ball')
        plt.text(list_balls[i][0] + 0.5, list_balls[i][1] + 0.5, i)

        x_values = [startpos[0], list_balls[i][0]]
        y_values = [startpos[1], list_balls[i][1]]

        plt.plot(x_values, y_values, 'b-')

        for j in range(len(list_balls)):

            if j != i:

                #x_values = [list_balls[i][0], list_balls[j][0]]
                #y_values = [list_balls[i][1], list_balls[j][1]]

                #plt.plot(x_values, y_values, 'b-')

                val = graph[frompoint][i][j]
                plt.text((list_balls[i][0] + list_balls[j][0]) / 2, (list_balls[i][1] + list_balls[j][1]) / 2, str(val))

    # Launch print
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("This file is not runable\n")
    
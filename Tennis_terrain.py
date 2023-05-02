from matplotlib import pyplot as plt
import numpy as np


class Robot:
    def __init__(self, position, direction, mv_speed, rot_speed):
        self.position = position
        self.direction = direction
        self.mv_speed = mv_speed
        self.rot_speed = rot_speed

    def __str__(self):
        return "The robot is in " + str(self.position) + " in direction " + str(
            self.direction) + " at a mv speed " + str(self.mv_speed) + " and rot speed " + str(self.rot_speed)


def init_world(filename, n, mv, rot):

    global robot

    list_balls = []

    size = 0

    plt.xlim(0, n)
    plt.ylim(0, n)

    with open(filename, 'r') as f:

        for line in f:

            line = line.strip()

            if not line or line.startswith('#'):
                continue

            name, coords = line.split(':')

            name = name.strip()
            coords = coords.strip()

            if name == 'R':
                x, y = map(int, coords[1:-1].split(','))
                plt.plot(x, y, marker="o", label='robot')

                robot = Robot([x, y], 0, mv, rot)
                plt.text(x+0.5,y+0.5,str(size))
                size+=1

            elif name.isdigit():
                x, y = map(int, coords[1:-1].split(','))
                plt.plot(x, y, marker="o", label='ball')
                plt.text(x+0.5,y+0.5,str(size))
                size += 1
                list_balls.append(np.array([x, y]))

    print("World generated : Number of balls to pick : " + str(len(list_balls)))

    for i in range(len(list_balls)):

        x_values = [robot.position[0], list_balls[i][0]]
        y_values = [robot.position[1], list_balls[i][1]]

        plt.plot(x_values, y_values, 'b-')

        for j in range(len(list_balls)):

            if j != i:

                x_values = [list_balls[i][0], list_balls[j][0]]
                y_values = [list_balls[i][1], list_balls[j][1]]

                plt.plot(x_values, y_values, 'b-')

                value = abs(list_balls[i][0] - list_balls[j][0]) + \
                    abs(list_balls[i][1] - list_balls[j][1])
                plt.text((list_balls[i][0] + list_balls[j][0]) / 2,
                         (list_balls[i][1] + list_balls[j][1]) / 2, str(value))


    return robot, list_balls


if __name__ == "__main__":
    n = 30
    robot, list_balls = init_world('terrain.csv', n, 4, 2)

    plt.legend()
    plt.show()

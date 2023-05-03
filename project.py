from world import *
from graph import *
import sys

def print_path(path):
    
    x_values = [point[0] for point in path]
    y_values = [point[1] for point in path]
    plt.plot(x_values[1],y_values[1], "r",marker="x",markersize=20)
    plt.plot(x_values[0],y_values[0], "g",marker="*",markersize=20)
    plt.plot(x_values,y_values, "b--")
    plt.plot(x_values, y_values,marker="o", label='ball')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Missing arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed)")
        exit(1)

    if len(sys.argv) > 5:
        print("To much arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed)")
        exit(1)

    data = init_world(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

    robot = data[0]
    list_balls = data[1]
    graph = init_graph(list_balls + [robot.position])

    print(path_opt(graph, list_balls, robot))
    
    # print(graph)
    # print(robot)
    # print(list_balls)

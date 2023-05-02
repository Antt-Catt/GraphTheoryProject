from graph import *
import sys

if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("Missing arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed)")
        exit(1)

    if len(sys.argv) > 5:
        print("To much arguments (1- world filename, 2- world size, 3- robot mv_speed, 4- robot rot_speed)")
        exit(1)

    G, robot, list_balls = init_world(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

    graph = init_graph(list_balls)

    print_world(G, robot, list_balls, len(G)-1)

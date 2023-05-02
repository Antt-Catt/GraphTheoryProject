from world import *
from graph import *
import sys
import itertools

def path_opt(graph, list_balls, robot):
    init_pos = robot.position
    perm = itertools.permutations(range(len(list_balls)))
    weight_min = float('inf')
    exceed_weight = False
    path_min = []
    list_balls.append(init_pos)

    # for all possible paths (p is list of balls)
    for p in perm:
        p = list(p)
        p.insert(0, len(list_balls) - 1)
        p.insert(0, len(list_balls) - 1)
        p.append(len(list_balls) - 1)

        path = [init_pos]
        
        weight = 0

        # get total weight
        # if weight > weight_min : STOP
        for i in range(len(list_balls)):
            weight += graph[p[i]][p[i + 1]][p[i + 2]]
            path.append(list_balls[i])
            
            if weight > weight_min:
                exceed_weight = True
                break
                
        if exceed_weight:
            exceed_weight = False
        else:
            weight_min = weight
            path_min = path

    return path_min

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

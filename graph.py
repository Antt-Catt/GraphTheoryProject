import numpy as np
import itertools



# Initializes the graph
def init_graph(list_nodes, robot):

    list_nodes = list_nodes+[robot.position]
    size = len(list_nodes)

    # First fill with zeros
    graph = np.zeros((size, size, size))

    # Foreach couple (i,j) where i different j initialize lenght to -1
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if i != j:
                    graph[layer][i][j] = -1

    # If from pos equals to end pos set lenght to 0
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if i == layer or j == layer:
                    if (i == (size - 1) or j == (size - 1)):
                        # graph[layer][i][j] = weight((list_nodes[layer] - [0, 1]), i, j, list_nodes, robot)
                        graph[layer][i][j] = 0
                    else:
                        graph[layer][i][j] = 0

    # filling the graph with angles
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if layer != i and i != j and layer != j:
                    if graph[layer][i][j] == -1:
                        graph[layer][i][j] = weight(
                            layer, i, j, list_nodes, robot)

    return graph


# Calculate the time it takes to go from current to future node coming from previous node.
def weight(previous_node, current_node, future_node, list_nodes, robot):
    # calculate angle between 3 points a,b,c
    if isinstance(previous_node, int):
        a = list_nodes[previous_node]
    else:
        a = previous_node
    b = list_nodes[current_node]
    c = list_nodes[future_node]

    ba = b - a
    bc = c - b

    # print(np.linalg.norm(ba), np.linalg.norm(bc))

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    if (cosine_angle > 1):
        cosine_angle = 1
    elif (cosine_angle < -1):
        cosine_angle = -1
    angle = np.arccos(cosine_angle)

    # distance between current and future point
    distance = np.linalg.norm(bc)
    # print("angle =", angle, "; distance =", distance)
    return angle / robot.rot_speed + distance / robot.mv_speed


def path_opt(graph, list_balls, robot):
    init_pos = robot.position
    perm = itertools.permutations(range(len(list_balls)))
    weight_min = float('inf')
    exceed_weight = False
    path_min = []
    list_balls.append(init_pos)

    # for all possible paths (p is list idx of balls in list_balls)
    for p in perm:
        p = list(p)
        # len(list_balls) - 1 is for init_pos (robot initial position)
        p.insert(0, len(list_balls) - 1)
        # adding because we start from here and we have to finish here
        p.insert(0, len(list_balls) - 1)
        p.append(len(list_balls) - 1)

        path = [init_pos]

        weight = 0

        # get total weight
        # if weight > weight_min : STOP
        for i in range(len(list_balls)):
            # weight of the edge for coming from p[i], is in p[i + 1] and going to p[i + 2]
            weight += graph[p[i]][p[i + 1]][p[i + 2]]
            # + 2 because the first 2 idx are for init_pos
            path.append(list_balls[p[i + 2]])

            if weight > weight_min:
                exceed_weight = True
                break

        if exceed_weight:
            exceed_weight = False
        else:
            weight_min = weight
            path_min = path
            

    print(weight_min)
    return path_min


def shortest_path(graph, list_balls, robot):
    path_min = []
    init_pos = robot.position
    list_nodes = list_balls+[init_pos] + \
        [np.array([init_pos[0], init_pos[1]-0.5])]
    passed_balls = [np.array([init_pos[0], init_pos[1]-0.5])]
    already_chosen_balls = []
    (previous, current, next) = (-1, -1, -1)

    sum=0

    min = float('inf')
    for i in range(len(list_balls)):
        # print(i,"is",weight(len(list_nodes)-1,len(list_nodes)-2,i,list_nodes,robot))
        if (weight(len(list_nodes)-1, len(list_nodes)-2, i, list_nodes, robot) < min):
            min = weight(len(list_nodes)-1, len(list_nodes) -
                         2, i, list_nodes, robot)
            (previous, current, next) = (len(list_nodes)-1, len(list_nodes)-2, i)
            sum+=min

    passed_balls.append(init_pos)
    already_chosen_balls.append(current)
    already_chosen_balls.append(next)

    goto_node = 0
    while (len(already_chosen_balls)-1 < len(list_balls)):
        #print("selecting in :",layer_selector)
        layer = graph[current]
        weights = layer[next]
        min = float('inf')
        for i in range(len(weights)-1):
            if i not in already_chosen_balls:
                if weights[i] < min:
                    min = weights[i]
                    goto_node = i
                    sum+=min

        (previous, current, next) = (current, next, goto_node)
        already_chosen_balls.append(next)


    already_chosen_balls.append(already_chosen_balls[0])
    path_min=[list_nodes[i] for i in already_chosen_balls]
    print(sum)
    return path_min


if __name__ == "__main__":
    from world import *

    robot,list_balls=init_world("terrain.csv")
    graph = init_graph(list_balls,robot)
    path=shortest_path(graph,list_balls,robot)
    print(path)
    print("This file is not runable\n")

import numpy as np
import itertools


# Initializes the graph
def init_graph(list_nodes, robot):
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
                    if i == (size - 1) or j == (size - 1):
                        graph[layer][i][j] = weight((list_nodes[layer] - [0, 1]), i, j, list_nodes, robot) 
                    else:
                        graph[layer][i][j] = 0

    # filling the graph with angles
    for layer in range(len(graph)):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if layer != i and i != j and layer != j:
                    if graph[layer][i][j] == -1:
                        graph[layer][i][j] = weight(layer, i, j, list_nodes, robot)
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
        p.insert(0, len(list_balls) - 1)
        p.insert(0, len(list_balls) - 1)
        p.append(len(list_balls) - 1)

        path = [init_pos]
        
        weight = 0

        # get total weight
        # if weight > weight_min : STOP
        for i in range(len(list_balls)):
            weight += graph[p[i]][p[i + 1]][p[i + 2]]
            path.append(list_balls[p[i + 2]]) # + 2 because the first 2 idx are for init_pos
            
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
    from world import *
    robot, list_balls = init_world("terrain.csv")

    graph = init_graph(list_balls+[robot.position])

    print(graph)
    print("This file is not runable\n")

from Tennis_terrain import *
import numpy as np

# Initializes the graph
def init_graph(graph, list_nodes):
    # setting line and collumn to zero
    for layer in range(len(graph)):
        for i in range(len(G[0])):
            for j in range(len(G[0])):
                if i==layer or j==layer:
                    graph[layer][i][j]=0
    #print(graph)

    # filling the graph with angles
    for layer in range(len(graph)):
        for i in range(len(G[0])):
            for j in range(len(G[0])):
                if layer != i and i != j and layer != j :
                    if graph[layer][i][j] == -1:
                        #print(layer,i,j,"for angle",weight(layer,i,j,list_nodes))
                        graph[layer][i][j]=weight(layer,i,j,list_nodes)
    print(graph)
    return graph

# Calculate the time it takes to go from current to future node coming from previous node.
def weight(previous_node,current_node,future_node,list_nodes):
    # calculate angle between 3 points a,b,c
    a = list_nodes[previous_node]
    b = list_nodes[current_node]
    c = list_nodes[future_node]

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    #print(np.degrees(angle))
    
    # distance between current and future point
    distance=np.linalg.norm(bc)
    return np.degrees(angle)+distance


if __name__ == "__main__":
    n = 30
    G, robot, list_balls = init_world(n, 'terrain.csv')
    init_graph(G, list_balls)
    #print(list_balls)
    weight(0,1,3,list_balls)



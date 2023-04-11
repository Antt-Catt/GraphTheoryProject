from matplotlib import pyplot as plt
import numpy as np

class robot:                               #class item
    def __init__(self,position,direction=0,mv_speed=0,rot_speed=0):          #id and price are atributes of the item class
        self.position=position
        self.direction=direction
        self.mv_speed=mv_speed
        self.rot_speed=rot_speed

    def __str__(self):
        return "The robot is in "+str(self.position)+" in direction "+str(self.direction)+" at a mv speed "+str(self.mv_speed)+" and rot speed "+str(self.rot_speed)


def read_world_file(N, filename):
    global robot
    
    list_balls=[]
    
    size=0

    plt.xlim(0, N)
    plt.ylim(0, N)
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
                robot=robot((x,y),0,4)  ###############################################################

            elif name.isdigit():
                x, y = map(int, coords[1:-1].split(','))
                plt.plot(x, y, marker="o", label='balls')
                size+=1
                list_balls.append((x,y))

    # plt.show()
    print(len(list_balls))
    for i in range(len(list_balls)):
        for j in range(i+1, len(list_balls)):
            x_values = [list_balls[i][0], list_balls[j][0]]
            y_values = [list_balls[i][1], list_balls[j][1]]
            plt.plot(x_values, y_values, 'b-')  # 'b-' means blue lines
            value = abs(list_balls[i][0] - list_balls[j][0]) + abs(list_balls[i][1] - list_balls[j][1])
            plt.text((list_balls[i][0] + list_balls[j][0])/2, (list_balls[i][1] + list_balls[j][1])/2, str(value))

    G=np.zeros((size,size))

    return G,robot,list_balls


if __name__ == "__main__":
    N = 30
    G = read_world_file(
        N, '/home/geekboyboss/Tennis-ball-gathering-robot/terrain.csv')

    plt.legend()
    plt.show()

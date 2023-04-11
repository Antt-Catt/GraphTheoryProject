from matplotlib import pyplot as plt


def read_world_file(N, filename):

    with open(filename, 'r') as f:

        plt.grid()
        plt.xlim(0, N)
        plt.ylim(0, N)
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

            elif name.isdigit():
                x, y = map(int, coords[1:-1].split(','))
                plt.plot(x, y, marker="o", label='dechet')

            """
            elif name == 'X':
                coords1, coords2 = coords[1:].replace(')','').replace('(','').split(';')#.replace(')',' ').split()
                x1, y1 = map(int, coords1[1:-1].split(','))
                x2, y2 = map(int, coords2[1:-1].split(','))
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        
            """
    plt.show()

    return 0


if __name__ == "__main__":
    read_world_file(
        30, '/home/geekboyboss/Tennis-ball-gathering-robot/terrain.csv')

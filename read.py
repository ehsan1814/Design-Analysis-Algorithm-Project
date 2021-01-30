import fileinput

class Map:
    def __init__(self, fires=[], map_size=(0, 0), s=(-1, -1), t=(-1, -1), k=1):
        self.fires = fires
        self.map_size = map_size
        self.s = s
        self.t = t
        self.k = k

    def __str__(self):
        return str("{} - {} - {} - {} - {}".format(self.fires, self.map_size, self.s, self.t, self.k))


def get_each_map(ls):
    fires = []
    pos_s = (-1, -1)
    pos_t = (-1, -1)

    map_size_i, map_size_j, k = ls[0].split()
    map_size_i, map_size_j, k = int(map_size_i), int(map_size_j), int(k)

    for i in range(1, map_size_i+1):
        for j in range(len(ls[i])):
            if(ls[i][j] == 'f'):
                fires.append((i-1, j))
            elif(ls[i][j] == 's' or ls[i][j] == 't'):
                if(ls[i][j] == 's'):
                    pos_s = (i-1, j)
                else:
                    pos_t = (i-1, j)

    map_size = (map_size_i, map_size_j)
    return Map(fires=fires, map_size=map_size, s=pos_s, t=pos_t, k=k)


def get_all_map(file_content):
    i = 0
    maps = []
    inp = file_content

    while(i < len(inp)):
        data = inp[i].split()
        length_map = int(data[0])

        # end of file condition
        if(length_map != 0):
            maps.append(get_each_map(inp[i:i + length_map+1]))

        i = i + length_map + 1
    

    return maps


def write_on_file(file_name, data):
    file = open(file_name, 'w')
    for a in data:
        file.write("{} {}\n".format(a[0], a[1]))
    file.close()


def prints(f):
    for a in f:
        print(a, end="\n")


if __name__ == "__main__":
    
    file_content = []
    file_name_output = 'ehsan.txt'

    for a in fileinput.input():
        file_content.append(a)

    maps = get_all_map(file_content)
    prints(maps)


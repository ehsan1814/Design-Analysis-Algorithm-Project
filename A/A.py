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


def get_all_map(file_name='C:/Users/Ehsan/Desktop/Ehsan/Design and Analysis of Algorithms/Design-Analysis-Algorithm-Project/A/sample.in'):
    i = 0
    maps = []
    file = open(file_name, 'r')
    inp = file.readlines()

    while(i < len(inp)):
        data = inp[i].split()
        length_map = int(data[0])

        if(length_map != 0):
            maps.append(get_each_map(inp[i:i + length_map+1]))

        i = i + length_map + 1
    
    file.close()

    return maps


def operation_on_map(fires, map_size, k):

    map_i = map_size[0]
    map_j = map_size[1]
    my_map = [[(0, False) for x in range(map_j)] for z in range(map_i)]
    adjacent_vertices = [(0, 1), (1, 1), (1, 0), (1, -1),
                         (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for fire in fires:
        q = []
        q.append(fire)
        #print(my_map, end="\n")
        while(len(q) != 0):
            #print(q, end="\n")
            #q = list(dict.fromkeys(q))
            current_point = q.pop(0)
            # my_map[current_point[0]][current_point[1]] = (
            #    current_point[0], True)

            for adj in adjacent_vertices:

                new_point = (current_point[0] + adj[0],
                             current_point[1] + adj[1])

                if(is_inside(new_point, map_size)):

                    new_value = my_map[current_point[0]][current_point[1]]
                    old_value = my_map[new_point[0]][new_point[1]]

                    if(not my_map[new_point[0]][new_point[1]][1] or (new_value[0] + k < old_value[0])):

                        # q.append(new_point)
                        if(new_point in fires):
                            continue
                        else:
                            current_value = my_map[current_point[0]
                                                   ][current_point[1]][0]
                            my_map[new_point[0]][new_point[1]] = (
                                current_value + k, True)
                            q.append(new_point)
        # prints(my_map)

    return my_map


def part_a(fires, map_size, k):

    result_map = operation_on_map(fires, map_size, k)
    prints(result_map)
    max_value = 0
    max_place = (0, 0)
    for i in range(len(result_map)):
        for j in range(len(result_map[i])):

            point = result_map[i][j][0]
            if(point > max_value):
                max_value = point
                max_place = (i, j)

    return max_place


def is_inside(new_point, map_size):
    if(new_point[0] >= 0 and new_point[0] <= map_size[0]-1 and new_point[1] >= 0 and new_point[1] <= map_size[1]-1):
        return True
    return False


def prints(ls):
    for a in ls:
        print(a, end="\n")


fires1 = [(0, 3)]
fires2 = [(1, 0)]
fires3 = [(0, 0), (1, 1), (1, 5), (2, 4), (4, 6), (6, 5)]
map_size1 = (3, 4)
map_size2 = (2, 2)
map_size3 = (7, 7)
#prints(operation_on_map(fires3, map_size3, 2))
print(part_a(fires3, map_size3, 2))
#fires = [(0, 3), (2, 1)]
#map_size = (3, 4)
#k = 1
#
# print(part_b())
#pos_s = (2, 3)
#pos_t = (0, 0)
#map_size = (3, 4)
#fires = [(0, 3), (2, 1)]
#
#print(bfs_s_t((5, 3), (6, 0), (7, 7)))

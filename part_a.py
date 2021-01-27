def operation_on_map(fires, map_size, k):

    map_i = map_size[0]
    map_j = map_size[1]
    my_map = [[(0, False) for x in range(map_j)] for z in range(map_i)]
    adjacent_vertices = [(0, 1), (1, 1), (1, 0), (1, -1),(0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for fire in fires:
        q = []
        q.append(fire)

        while(len(q) != 0):
            current_point = q.pop(0)

            for adj in adjacent_vertices:

                new_point = (current_point[0] + adj[0],current_point[1] + adj[1])

                if(is_inside(new_point, map_size)):

                    new_value = my_map[current_point[0]][current_point[1]]
                    old_value = my_map[new_point[0]][new_point[1]]

                    if(not my_map[new_point[0]][new_point[1]][1] or (new_value[0] + k < old_value[0])):

                        q.append(new_point)
                        if(new_point in fires):
                            continue
                        else:
                            current_value = my_map[current_point[0]][current_point[1]][0]
                            my_map[new_point[0]][new_point[1]] = (current_value + k, True)
    return my_map


def part_a():
    fires = [(0, 3), (2, 1)]
    map_size = (3, 4)
    k = 1
    result_map = operation_on_map(fires, map_size, k)
    return result_map


def bfs_s_t(pos_s, pos_t, map_size):

    map_i = map_size[0]
    map_j = map_size[1]
    map_bfs = [[(0, False) for x in range(map_j)] for z in range(map_i)]
    adjacent_vertices = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    q = []
    q.append(pos_s)
    while(len(q) != 0):
        current_point = q.pop(0)
        if(current_point == pos_t):
            return map_bfs[pos_t[0]][pos_t[1]][0]

        for adj in adjacent_vertices:
            new_point = (current_point[0] + adj[0],current_point[1] + adj[1])

            if(is_inside(new_point, map_size) and not map_bfs[new_point[0]][new_point[1]][1]):
                current_value = map_bfs[current_point[0]][current_point[1]][0]
                map_bfs[new_point[0]][new_point[1]] = (current_value + 1, True)
                q.append(new_point)

    return -1


def part_b():
    pos_s = (2, 3)
    pos_t = (0, 0)
    map_size = (3, 4)
    fires = [(0, 3), (2, 1)]
    value_from_s_to_t = bfs_s_t(pos_s, pos_t, map_size)
    map_part_a = operation_on_map(fires, map_size, 1)

    if(value_from_s_to_t < map_part_a[pos_t[0]][pos_t[1]][0]):
        return value_from_s_to_t
    return 'Impossible'


def is_inside(new_point, map_size):
    if(new_point[0] >= 0 and new_point[0] <= map_size[0]-1 and new_point[1] >= 0 and new_point[1] <= map_size[1]-1):
        return True
    return False


fires1 = [(0, 3), (2, 1), (0, 0)]
fires2 = [(1, 0)]
fires3 = [(0, 0), (1, 1), (1, 5), (2, 4), (4, 6), (6, 5)]
map_size1 = (3, 4)
map_size2 = (2, 2)
map_size3 = (7, 7)
print(operation_on_map(fires3, map_size3, 1))
# print(part_b())

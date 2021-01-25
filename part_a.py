from queue import Queue


def part_a():
    
    
    fires = [(0, 3), (2, 1)]

    map_i = 3
    map_j = 4

    my_map = [[(0, False), (0, False), (0, False), (0, False)],
              [(0, False), (0, False), (0, False), (0, False)],
              [(0, False), (0, False), (0, False), (0, False)]]

    adjacent_points = [(0, 1), (1, 1), (1, 0), (1, -1),
                       (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for fire in fires:
        q = []
        q.append(fire)
        while(not len(q) == 0):
            # print(q,end="\n")
            # print(my_map,end="\n")
            current_point = q.pop(0)
            for i in adjacent_points:

                new_i = current_point[0] + i[0]
                new_j = current_point[1] + i[1]

                if(is_inside(new_i, new_j, map_i, map_j)):

                    new_value = my_map[current_point[0]][current_point[1]]
                    old_value = my_map[new_i][new_j]

                    if(not my_map[new_i][new_j][1] or (new_value[0] + 1 < old_value[0])):

                        q.append((new_i, new_j))
                        if((new_i, new_j) in fires):
                            continue
                        else:
                            a = my_map[current_point[0]][current_point[1]]
                            my_map[new_i][new_j] = (a[0] + 1, True)
    return my_map


def is_inside(new_i, new_j, size_of_map_i, size_of_map_j):
    if(new_i >= 0 and new_i <= size_of_map_i-1 and new_j >= 0 and new_j <= size_of_map_j-1):
        return True
    return False


print(part_a())

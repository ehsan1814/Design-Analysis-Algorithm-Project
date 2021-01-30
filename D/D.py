import os
import sys 
import fileinput
import itertools

class Test:
    def __init__(self,N,M,edges,treasure_no,treasures_in_cage,power):
        self.N = N
        self.M = M
        self.edges = edges
        self.treasure_no = treasure_no
        self.treasures_in_cage = treasures_in_cage
        self.power = power

    def __str__(self):
        return str("{} | {} | {} | {} | {} | {}\n".format(self.N,self.M,self.edges,self.treasure_no,self.treasures_in_cage,self.power))


def get_each_test(ls):
    N = 0
    M = 0 
    edges = []
    treasure_no = 0
    treasures_in_cage = []
    power = 0

    N, M = ls[0].split()
    N, M = int(N), int(M)

    for i in range(1,M + 1):
        edge = ls[i].split()
        for counter in range(3):
            edge[counter] = int(edge[counter])
        edges.append(edge)
    
    treasure_no = ls[M+1].split()
    treasure_no = int(treasure_no[0])

    treasure_ls = ls[M+2].split()
    for a in treasure_ls:
        treasures_in_cage.append(int(a))

    power = ls[M+3].split()
    power = int(power[0])


    return Test(N=N,M=M,edges=edges,treasure_no=treasure_no,treasures_in_cage=treasures_in_cage,power=power)


def get_all_tests(file_content):

    i = 1 
    tests = []
    inp = file_content

    len_inp = len(inp)
    while(i < len_inp):
        data = inp[i].split()
        length_test = int(data[1])

        tests.append(get_each_test(inp[i:i + length_test + 4]))
        i = i + length_test + 4

    return tests


def write_on_file(file_name, data):
    file = open(file_name, 'w')
    for a in data:
        file.write("{}\n".format(a))
    file.close()


class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

  
    
    def minDistance(self, dist, sptSet): 
  
        min = sys.maxsize
        min_index = -1
  
  
        for v in range(self.V): 
            if(dist[v] < min and sptSet[v] == False): 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
  
    
            for v in range(self.V): 
                if (self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]): 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        return dist


def main(N,M,edges,treasure_no,treasures_in_cage,power):
    '''
        N : tedad qar ha 
        M : tedad tonel ha

        edges : tonel ha dar yek array
        example : [[a,b,l]]

        treasure_no : tedad ganj ha
        treasures_in_cage : qar hayi ke ganj daran

        power : tavan poaro 
    '''

    V = N
    E = M
    alpha = power
    tn = treasures_in_cage

    g = Graph(V) 
    distances = [[-1 for column in range(V)] for row in range(V)]

    #calculate the graph matrix
    for counter in range(E):
        g.graph[edges[counter][0]][edges[counter][1]] = edges[counter][2]
        g.graph[edges[counter][1]][edges[counter][0]] = edges[counter][2]


    #to calculate dijkstra for all treasure nodes
    distances[0] = g.dijkstra(0)
    for i in tn:
        distances[i] = g.dijkstra(i)

    # for multi chest in one node
    # treasure = [0] * tn.__len__()
    treasureDict = {}
    for c in tn:
        treasureDict[c] = 0
    for c in tn:
        treasureDict[c] += 1
    treasureList = list(treasureDict.keys())


    ptn = itertools.permutations(treasureList)
    permutatedNodes = list(ptn)

    tnumMax = 0
    for k in permutatedNodes:
        d = 0
        tnum = 0
        j = 0
        for i in k:
            if(distances[j][i] + distances[i][0] + d <= alpha):
                tnum += treasureDict[i]
                d += distances[j][i]
                j = i
        if(tnum > tnumMax):
            tnumMax = tnum

    return tnumMax



if __name__ == "__main__":
    
    file_content = []
    output_name = "ehsan.txt"

    for f in fileinput.input():
        file_content.append(f)



    all_tests = get_all_tests(file_content)
    result_of_test = []
    for test in all_tests:
        result_of_test.append(main(test.N,test.M,test.edges,test.treasure_no,test.treasures_in_cage,test.power))
    
    write_on_file(output_name,result_of_test)


    
                     
